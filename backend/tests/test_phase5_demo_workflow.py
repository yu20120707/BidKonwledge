from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.api.generation import get_llm_client
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class Phase10DemoWorkflowParser:
    def __init__(self) -> None:
        self.calls = 0

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        self.calls += 1
        if self.calls == 1:
            return [
                NormalizedSection(
                    title="历史投标运维方案",
                    level=1,
                    order_index=0,
                    text="运维服务实施方案覆盖应急响应、故障处理、值守保障和服务质量承诺。",
                    page_start=1,
                    page_end=2,
                )
            ]
        return [
            NormalizedSection(
                title="招标需求与评分标准",
                level=1,
                order_index=0,
                text="项目需求包括运维实施。评分标准技术分20分。废标情形包括不符合资格审查要求。",
                page_start=1,
                page_end=2,
            )
        ]


class Phase10DemoWorkflowLLM:
    def __init__(self) -> None:
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return "候选内容：建立运维实施与应急响应机制，并保留人工复核。"


def test_phase10_demo_api_chain_upload_parse_build_analyze_retrieve_generate(client):
    parser = Phase10DemoWorkflowParser()
    app.dependency_overrides[get_document_parser] = lambda: parser
    fake_llm = Phase10DemoWorkflowLLM()
    app.dependency_overrides[get_llm_client] = lambda: fake_llm

    historical_upload = upload(client, filename="historical-phase10.docx", doc_role="historical_bid")
    assert historical_upload.status_code == 201
    historical_document_id = historical_upload.json()["document_id"]

    historical_parse = client.post(f"/api/documents/{historical_document_id}/parse")
    assert historical_parse.status_code == 200
    assert historical_parse.json()["parse_status"] == "parsed"

    knowledge_build = client.post("/api/knowledge/build", json={"document_id": historical_document_id})
    assert knowledge_build.status_code == 200
    knowledge_body = knowledge_build.json()
    assert knowledge_body["cards_count"] == 1
    assert knowledge_body["tags"] == ["突发应急方案和措施"]

    knowledge_list = client.get(f"/api/documents/{historical_document_id}/knowledge-cards")
    assert knowledge_list.status_code == 200
    knowledge_cards = knowledge_list.json()["cards"]
    assert len(knowledge_cards) == 1
    assert knowledge_cards[0]["source_filename"] == "historical-phase10.docx"

    tender_upload = upload(client, filename="tender-phase10.docx", doc_role="tender")
    assert tender_upload.status_code == 201
    tender_document_id = tender_upload.json()["document_id"]

    tender_parse = client.post(f"/api/documents/{tender_document_id}/parse")
    assert tender_parse.status_code == 200
    assert tender_parse.json()["parse_status"] == "parsed"

    tender_analysis = client.post("/api/tender/analyze", json={"document_id": tender_document_id})
    assert tender_analysis.status_code == 200
    tender_body = tender_analysis.json()
    assert len(tender_body["project_requirements"]) == 1
    assert len(tender_body["scoring_items"]) == 1
    assert len(tender_body["disqualification_risks"]) == 1
    assert tender_body["need_human_review"] is True

    retrieve_response = client.post(
        "/api/retrieve",
        json={"tag": "突发应急方案和措施", "query": "应急", "top_k": 5},
    )
    assert retrieve_response.status_code == 200
    retrieve_body = retrieve_response.json()
    assert len(retrieve_body["results"]) == 1
    assert retrieve_body["results"][0]["document_id"] == historical_document_id

    generate_response = client.post(
        "/api/generate",
        json={
            "target_tag": "突发应急方案和措施",
            "query": f"应急\n招标需求: {tender_body['project_requirements'][0]['description']}",
            "top_k": 5,
        },
    )
    assert generate_response.status_code == 200
    generate_body = generate_response.json()
    assert generate_body["need_human_review"] is True
    assert generate_body["risks"] == []
    assert len(generate_body["citations"]) == 1
    assert generate_body["citations"][0]["document_id"] == historical_document_id
    assert "招标需求:" in fake_llm.prompts[0]
    assert "项目需求包括运维实施" in fake_llm.prompts[0]
