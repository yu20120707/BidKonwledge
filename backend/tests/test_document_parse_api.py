from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.app.storage import database
from backend.tests.conftest import upload


class RecordingParser:
    def __init__(self, settings, document_id: str):
        self.settings = settings
        self.document_id = document_id
        self.status_seen: list[str] = []
        self.paths: list[Path] = []

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        self.paths.append(file_path)
        document = database.get_document(self.settings, self.document_id)
        assert document is not None
        self.status_seen.append(document.parse_status)
        return [
            NormalizedSection(
                title="运维服务实施方案",
                level=1,
                order_index=0,
                text="本项目提供运维服务、项目管理和应急响应能力。",
            )
        ]


class FailingParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        raise RuntimeError("forced parser failure")


class PathLeakingParser:
    def __init__(self, message: str):
        self.message = message

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        raise RuntimeError(self.message)


def override_parser(parser) -> None:
    app.dependency_overrides[get_document_parser] = lambda: parser


def test_parse_docx_transitions_to_parsed_and_persists_counts(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    parser = RecordingParser(test_settings, document_id)
    override_parser(parser)

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["document_id"] == document_id
    assert body["parse_status"] == "parsed"
    assert body["sections_count"] == 1
    assert body["chunks_count"] == 1
    assert body["error_message"] is None
    assert parser.status_seen == ["parsing"]
    assert parser.paths[0].name.endswith(".docx")
    assert database.get_document(test_settings, document_id).parse_status == "parsed"


def test_parse_text_based_pdf_uses_same_phase2_path(client, test_settings):
    upload_response = upload(client, filename="proposal.pdf", content=b"%PDF text")
    document_id = upload_response.json()["document_id"]
    parser = RecordingParser(test_settings, document_id)
    override_parser(parser)

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    assert response.json()["parse_status"] == "parsed"
    assert parser.paths[0].name.endswith(".pdf")


def test_parse_failure_transitions_to_failed_and_clears_outputs(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    override_parser(FailingParser())

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "failed"
    assert body["sections_count"] == 0
    assert body["chunks_count"] == 0
    assert "forced parser failure" in body["error_message"]
    document = database.get_document(test_settings, document_id)
    assert document is not None
    assert document.parse_status == "failed"
    assert "forced parser failure" in document.error_message
    assert database.count_document_parse_outputs(test_settings, document_id) == {
        "sections_count": 0,
        "chunks_count": 0,
    }


def test_parse_failure_does_not_expose_absolute_local_paths(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    override_parser(
        PathLeakingParser(
            rf"failed near C:\Users\26561\secret\sample.docx "
            rf"and C:/Users/26561/secret/sample.pdf "
            rf"and file:///F:/BidKonwledge/data/uploads/sample.docx "
            rf"and {test_settings.upload_root}"
        )
    )

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    error_message = response.json()["error_message"]
    assert "C:\\" not in error_message
    assert "C:/" not in error_message
    assert "file:///" not in error_message
    assert "fil<local_path>" not in error_message
    assert str(test_settings.upload_root) not in error_message
    assert "<local_path>" in error_message
    document = database.get_document(test_settings, document_id)
    assert document is not None
    assert "C:\\" not in document.error_message
    assert "C:/" not in document.error_message
    assert "file:///" not in document.error_message
    assert str(test_settings.upload_root) not in document.error_message


def test_parse_unsupported_uploaded_type_marks_failed_without_parser(client, test_settings):
    class ShouldNotRunParser:
        def parse(self, file_path: Path) -> list[NormalizedSection]:
            raise AssertionError("parser should not run for unsupported parse type")

    upload_response = upload(client, filename="notes.txt")
    document_id = upload_response.json()["document_id"]
    override_parser(ShouldNotRunParser())

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "failed"
    assert "Unsupported parse file extension" in body["error_message"]
    assert database.get_document(test_settings, document_id).parse_status == "failed"


def test_parse_missing_document_returns_structured_404(client):
    response = client.post("/api/documents/missing/parse")

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"


def test_get_document_returns_parse_counts(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    override_parser(RecordingParser(test_settings, document_id))
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.get(f"/api/documents/{document_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["document_id"] == document_id
    assert body["parse_status"] == "parsed"
    assert body["sections_count"] == 1
    assert body["chunks_count"] == 1
    assert "stored_path" not in body


def test_get_missing_document_returns_structured_404(client):
    response = client.get("/api/documents/missing")

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"
