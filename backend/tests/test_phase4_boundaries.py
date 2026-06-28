from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.api.generation import get_llm_client
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class LocalGenerationParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="项目管理",
                level=1,
                order_index=0,
                text="项目管理包括进度、质量和服务保障。",
            )
        ]


class BoundaryLLM:
    def generate(self, prompt: str) -> str:
        return "候选内容：项目管理覆盖进度、质量和服务保障。"


def test_phase4_generation_uses_fake_llm_without_external_services(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("HAYSTACK_API_KEY", raising=False)
    app.dependency_overrides[get_document_parser] = lambda: LocalGenerationParser()
    app.dependency_overrides[get_llm_client] = lambda: BoundaryLLM()
    upload_response = upload(client, filename="proposal.docx")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.post(
        "/api/generate",
        json={"target_tag": "项目管理", "query": "质量", "top_k": 5},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["need_human_review"] is True
    assert body["citations"][0]["document_id"] == document_id
    assert body["risks"] == []
