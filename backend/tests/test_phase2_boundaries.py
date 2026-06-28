from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class BoundaryParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="项目管理",
                level=1,
                order_index=0,
                text="项目管理包括进度、质量和服务保障。",
            )
        ]


def test_phase2_parse_does_not_require_llm_or_vector_env(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    app.dependency_overrides[get_document_parser] = lambda: BoundaryParser()
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]

    parse_response = client.post(f"/api/documents/{document_id}/parse")
    chunks_response = client.get(f"/api/documents/{document_id}/chunks")

    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"
    assert chunks_response.status_code == 200
    assert chunks_response.json()["chunks"][0]["tags"] == ["运维服务", "项目管理"]


def test_app_import_and_health_do_not_require_docling(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
