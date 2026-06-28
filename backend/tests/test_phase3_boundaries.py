from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class LocalRetrievalParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="项目管理",
                level=1,
                order_index=0,
                text="项目管理包括进度、质量和服务保障。",
            )
        ]


def test_phase3_retrieval_does_not_require_llm_or_vector_env(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("HAYSTACK_API_KEY", raising=False)
    app.dependency_overrides[get_document_parser] = lambda: LocalRetrievalParser()
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.post("/api/retrieve", json={"tag": "项目管理", "top_k": 5})

    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 1
    assert results[0]["document_id"] == document_id
    assert results[0]["source"]["chunk_metadata"]["tagger"] == "deterministic_v1"
