from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.api.generation import get_llm_client
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class DemoWorkflowParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="运维服务应急",
                level=1,
                order_index=0,
                text="运维服务支持应急响应、故障处理和值守保障。",
                page_start=1,
                page_end=2,
            )
        ]


class DemoWorkflowLLM:
    def generate(self, prompt: str) -> str:
        return "候选内容：建立应急响应机制，提供故障处理和值守保障。"


def test_phase5_demo_api_chain_upload_parse_retrieve_generate(client):
    app.dependency_overrides[get_document_parser] = lambda: DemoWorkflowParser()
    app.dependency_overrides[get_llm_client] = lambda: DemoWorkflowLLM()

    upload_response = upload(client, filename="demo-workflow.docx")
    assert upload_response.status_code == 201
    document_id = upload_response.json()["document_id"]

    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"

    retrieve_response = client.post(
        "/api/retrieve",
        json={"tag": "运维服务", "query": "应急", "top_k": 5},
    )
    assert retrieve_response.status_code == 200
    retrieve_body = retrieve_response.json()
    assert len(retrieve_body["results"]) == 1
    assert retrieve_body["results"][0]["document_id"] == document_id

    generate_response = client.post(
        "/api/generate",
        json={
            "target_tag": "运维服务",
            "query": "应急",
            "top_k": 5,
        },
    )
    assert generate_response.status_code == 200
    generate_body = generate_response.json()
    assert generate_body["need_human_review"] is True
    assert generate_body["risks"] == []
    assert len(generate_body["citations"]) == 1
    assert generate_body["citations"][0]["document_id"] == document_id
