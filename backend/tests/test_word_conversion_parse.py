from __future__ import annotations

from pathlib import Path

from backend.app.adapters.word_converter import WordConversionError, WordConversionResult
from backend.app.api.documents import get_document_parser, get_word_converter
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.app.storage import database
from backend.tests.conftest import upload


LEGACY_OLE_BYTES = bytes.fromhex("D0 CF 11 E0") + b"legacy word bytes"


class RecordingParser:
    def __init__(self):
        self.paths: list[Path] = []

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        self.paths.append(file_path)
        return [
            NormalizedSection(
                title="转换后内容",
                level=1,
                order_index=0,
                text="转换后的 DOCX 进入现有解析链路。",
            )
        ]


class FakeWordConverter:
    method = "fake_word_converter"

    def __init__(self):
        self.calls: list[tuple[Path, Path]] = []

    def convert_to_docx(self, source_path: Path, target_path: Path) -> WordConversionResult:
        self.calls.append((source_path, target_path))
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(b"PK converted docx")
        return WordConversionResult(converted_path=target_path, method=self.method)


class FailingWordConverter:
    def convert_to_docx(self, source_path: Path, target_path: Path) -> WordConversionResult:
        raise WordConversionError(
            rf"failed near C:\Users\26561\secret\legacy.doc and {source_path}"
        )


def override_parse_dependencies(parser, converter) -> None:
    app.dependency_overrides[get_document_parser] = lambda: parser
    app.dependency_overrides[get_word_converter] = lambda: converter


def test_mislabeled_docx_uses_converted_file_for_parse(client, test_settings):
    parser = RecordingParser()
    converter = FakeWordConverter()
    override_parse_dependencies(parser, converter)
    upload_response = upload(
        client,
        filename="mislabeled.docx",
        content=LEGACY_OLE_BYTES,
        doc_role="tender",
    )
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert body["sections_count"] == 1
    assert len(converter.calls) == 1
    assert converter.calls[0][0].name.endswith(".docx")
    assert parser.paths[0].name == f"{document_id}.converted.docx"
    assert parser.paths[0].read_bytes().startswith(b"PK")
    assert body["parse_metadata"]["detected_format"] == "legacy_ole_word"
    assert body["parse_metadata"]["is_mislabeled"] is True
    assert body["parse_metadata"]["conversion_required"] is True
    assert body["parse_metadata"]["conversion_method"] == "fake_word_converter"
    assert body["parse_metadata"]["converted_path"] == (
        f"_derived/{document_id}.converted.docx"
    )

    document = database.get_document(test_settings, document_id)
    assert document is not None
    assert document.parse_metadata == body["parse_metadata"]


def test_legacy_doc_extension_uses_converter_before_parse(client):
    parser = RecordingParser()
    converter = FakeWordConverter()
    override_parse_dependencies(parser, converter)
    upload_response = upload(client, filename="legacy.doc", content=LEGACY_OLE_BYTES)
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    assert response.json()["parse_status"] == "parsed"
    assert len(converter.calls) == 1
    assert parser.paths[0].suffix == ".docx"
    assert response.json()["parse_metadata"]["is_mislabeled"] is False


def test_true_docx_does_not_call_converter(client):
    parser = RecordingParser()

    class ShouldNotRunConverter:
        def convert_to_docx(self, source_path: Path, target_path: Path):
            raise AssertionError("converter should not run for true docx")

    override_parse_dependencies(parser, ShouldNotRunConverter())
    upload_response = upload(client, filename="true.docx", content=b"PK true docx")
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert parser.paths[0].name.endswith(".docx")
    assert ".converted." not in parser.paths[0].name
    assert body["parse_metadata"]["detected_format"] == "docx_zip"
    assert body["parse_metadata"]["conversion_required"] is False
    assert body["parse_metadata"]["converted_path"] is None


def test_converter_failure_marks_parse_failed_without_absolute_path_leak(
    client, test_settings
):
    parser = RecordingParser()
    override_parse_dependencies(parser, FailingWordConverter())
    upload_response = upload(client, filename="legacy.doc", content=LEGACY_OLE_BYTES)
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "failed"
    assert body["sections_count"] == 0
    assert body["chunks_count"] == 0
    assert body["parse_metadata"]["detected_format"] == "legacy_ole_word"
    assert body["parse_metadata"]["conversion_required"] is True
    assert "C:\\" not in body["error_message"]
    assert str(test_settings.upload_root) not in body["error_message"]
    assert "<local_path>" in body["error_message"]
    assert parser.paths == []


def test_get_document_includes_safe_parse_metadata(client):
    parser = RecordingParser()
    converter = FakeWordConverter()
    override_parse_dependencies(parser, converter)
    upload_response = upload(client, filename="mislabeled.docx", content=LEGACY_OLE_BYTES)
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.get(f"/api/documents/{document_id}")

    assert response.status_code == 200
    metadata = response.json()["parse_metadata"]
    assert metadata["converted_path"] == f"_derived/{document_id}.converted.docx"
    assert ":\\" not in " ".join(str(value) for value in metadata.values())
