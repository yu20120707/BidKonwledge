from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.app.storage import database
from backend.tests.conftest import upload


class MultiSectionParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="运维服务方案",
                level=1,
                order_index=0,
                text="运维服务覆盖日常巡检、故障处理和质量管理。",
            ),
            NormalizedSection(
                title="安全与应急",
                level=1,
                order_index=1,
                text="安全保障包括数据安全，应急响应包括突发事件处理。",
            ),
        ]


def test_chunks_are_persisted_with_normalized_schema(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    app.dependency_overrides[get_document_parser] = lambda: MultiSectionParser()

    parse_response = client.post(f"/api/documents/{document_id}/parse")
    chunks_response = client.get(f"/api/documents/{document_id}/chunks")

    assert parse_response.status_code == 200
    assert parse_response.json()["chunks_count"] == 2
    assert chunks_response.status_code == 200
    chunks = chunks_response.json()["chunks"]
    assert len(chunks) == 2
    assert chunks[0]["document_id"] == document_id
    assert chunks[0]["section_title"] == "运维服务方案"
    assert chunks[0]["section_path"] == "运维服务方案"
    assert chunks[0]["chunk_type"] == "text"
    assert chunks[0]["order_index"] == 0
    assert chunks[0]["chunk_index"] == 0
    assert "运维服务" in chunks[0]["tags"]
    assert chunks[0]["metadata"]["tagger"] == "deterministic_v1"
    assert "安全保障" in chunks[1]["tags"]
    assert "应急响应" in chunks[1]["tags"]


def test_reparse_replaces_old_sections_and_chunks(client, test_settings):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    app.dependency_overrides[get_document_parser] = lambda: MultiSectionParser()

    first = client.post(f"/api/documents/{document_id}/parse")
    second = client.post(f"/api/documents/{document_id}/parse")

    assert first.status_code == 200
    assert second.status_code == 200
    assert database.count_document_parse_outputs(test_settings, document_id) == {
        "sections_count": 2,
        "chunks_count": 2,
    }


def test_get_chunks_for_pending_document_returns_empty_list(client):
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]

    response = client.get(f"/api/documents/{document_id}/chunks")

    assert response.status_code == 200
    assert response.json() == {"document_id": document_id, "chunks": []}


def test_get_chunks_missing_document_returns_structured_404(client):
    response = client.get("/api/documents/missing/chunks")

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"
