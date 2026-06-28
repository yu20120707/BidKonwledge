from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.api.generation import get_llm_client
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class GenerationParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="运维服务应急",
                level=1,
                order_index=0,
                text="运维服务支持应急响应，包含突发事件处理和服务保障。",
                page_start=5,
                page_end=6,
            ),
            NormalizedSection(
                title="商务报价",
                level=1,
                order_index=1,
                text="报价费用说明和价格构成。",
            ),
        ]


class FakeLLM:
    def __init__(self, output: str = "候选内容：提供应急响应和值守保障。"):
        self.output = output
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return self.output


def parse_generation_fixture(client) -> str:
    app.dependency_overrides[get_document_parser] = lambda: GenerationParser()
    upload_response = upload(client, filename="generation.docx")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"
    return document_id


def test_generate_returns_content_citations_risks_and_human_review(client):
    document_id = parse_generation_fixture(client)
    fake_llm = FakeLLM()
    app.dependency_overrides[get_llm_client] = lambda: fake_llm

    response = client.post(
        "/api/generate",
        json={"target_tag": "运维服务", "query": "应急", "top_k": 5},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["target_tag"] == "运维服务"
    assert body["generated_content"] == "候选内容：提供应急响应和值守保障。"
    assert body["need_human_review"] is True
    assert body["risks"] == []
    assert len(body["citations"]) == 1
    citation = body["citations"][0]
    assert citation["source_filename"] == "generation.docx"
    assert citation["source_section_title"] == "运维服务应急"
    assert citation["document_id"] == document_id
    assert citation["chunk_id"]
    assert "应急响应" in citation["content_snippet"]


def test_generate_prompt_preserves_source_chunk_context(client):
    parse_generation_fixture(client)
    fake_llm = FakeLLM()
    app.dependency_overrides[get_llm_client] = lambda: fake_llm

    response = client.post(
        "/api/generate",
        json={"target_tag": "运维服务", "query": "应急", "top_k": 5},
    )

    assert response.status_code == 200
    prompt = fake_llm.prompts[0]
    assert "chunk_id=" in prompt
    assert "source_filename=generation.docx" in prompt
    assert "section_title=运维服务应急" in prompt
    assert "目标标签: 运维服务" in prompt
    assert "用户需求: 应急" in prompt


def test_generate_empty_output_and_no_citations_returns_risks(client):
    parse_generation_fixture(client)
    fake_llm = FakeLLM(output="   ")
    app.dependency_overrides[get_llm_client] = lambda: fake_llm

    response = client.post(
        "/api/generate",
        json={"target_tag": "商务报价", "query": "巡检", "top_k": 5},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["generated_content"] == ""
    assert body["citations"] == []
    assert body["need_human_review"] is True
    assert {risk["risk_type"] for risk in body["risks"]} == {
        "EMPTY_GENERATION",
        "MISSING_CITATIONS",
    }


def test_generate_validates_required_fields(client):
    fake_llm = FakeLLM()
    app.dependency_overrides[get_llm_client] = lambda: fake_llm

    response = client.post(
        "/api/generate",
        json={"target_tag": "   ", "query": "应急", "top_k": 5},
    )

    assert response.status_code == 400
    assert response.json()["error_code"] == "INVALID_GENERATION_REQUEST"


def test_generate_without_configured_llm_returns_structured_503(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    response = client.post(
        "/api/generate",
        json={"target_tag": "运维服务", "query": "应急", "top_k": 5},
    )

    assert response.status_code == 503
    assert response.json()["error_code"] == "LLM_NOT_CONFIGURED"
