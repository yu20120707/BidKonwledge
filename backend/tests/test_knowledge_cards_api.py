from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class KnowledgeCardParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="运维服务实施方案",
                level=1,
                order_index=0,
                text="本项目提供运维服务实施、日常维护和服务台支持。",
                page_start=1,
                page_end=2,
            ),
            NormalizedSection(
                title="突发应急方案",
                level=1,
                order_index=1,
                text="发生故障时启动应急响应，处理突发事件并恢复服务。",
                page_start=3,
                page_end=3,
            ),
            NormalizedSection(
                title="其他说明",
                level=1,
                order_index=2,
                text="这里是没有明显业务关键词的补充文字。",
                page_start=4,
                page_end=4,
            ),
        ]


def parse_knowledge_fixture(client, doc_role: str = "historical_bid") -> str:
    app.dependency_overrides[get_document_parser] = lambda: KnowledgeCardParser()
    upload_response = upload(client, filename="knowledge.docx", doc_role=doc_role)
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"
    return document_id


def test_build_cards_from_parsed_historical_bid(client):
    document_id = parse_knowledge_fixture(client)

    response = client.post("/api/knowledge/build", json={"document_id": document_id})

    assert response.status_code == 200
    body = response.json()
    assert body["document_id"] == document_id
    assert body["cards_count"] == 3
    assert body["tags"] == [
        "运维服务实施方案",
        "突发应急方案和措施",
        "未分类",
    ]


def test_list_cards_preserves_source_traceability(client):
    document_id = parse_knowledge_fixture(client)
    build_response = client.post("/api/knowledge/build", json={"document_id": document_id})
    assert build_response.status_code == 200

    response = client.get(f"/api/documents/{document_id}/knowledge-cards")

    assert response.status_code == 200
    body = response.json()
    assert body["document_id"] == document_id
    cards = body["cards"]
    assert len(cards) == 3
    first = cards[0]
    assert first["card_id"].startswith("kc_")
    assert first["document_id"] == document_id
    assert first["source_chunk_id"]
    assert first["tag"] == "运维服务实施方案"
    assert first["source_filename"] == "knowledge.docx"
    assert first["source_section_title"] == "运维服务实施方案"
    assert first["source_section_path"] == "运维服务实施方案"
    assert first["page_start"] == 1
    assert first["page_end"] == 2
    assert first["confidence"] == 0.8
    assert first["metadata"]["tagger"] == "prd_deterministic_v1"
    assert "运维" in first["metadata"]["matched_keywords"]

    fallback = cards[2]
    assert fallback["tag"] == "未分类"
    assert fallback["confidence"] == 0.3
    assert fallback["metadata"]["matched_keywords"] == []


def test_rebuild_replaces_existing_cards_deterministically(client):
    document_id = parse_knowledge_fixture(client)

    first_build = client.post("/api/knowledge/build", json={"document_id": document_id})
    first_list = client.get(f"/api/documents/{document_id}/knowledge-cards")
    second_build = client.post("/api/knowledge/build", json={"document_id": document_id})
    second_list = client.get(f"/api/documents/{document_id}/knowledge-cards")

    assert first_build.status_code == 200
    assert second_build.status_code == 200
    assert first_build.json()["cards_count"] == 3
    assert second_build.json()["cards_count"] == 3
    first_cards = first_list.json()["cards"]
    second_cards = second_list.json()["cards"]
    assert [card["card_id"] for card in second_cards] == [
        card["card_id"] for card in first_cards
    ]
    assert [card["tag"] for card in second_cards] == [
        "运维服务实施方案",
        "突发应急方案和措施",
        "未分类",
    ]


def test_build_missing_document_returns_structured_404(client):
    response = client.post("/api/knowledge/build", json={"document_id": "missing"})

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"


def test_build_unparsed_document_returns_structured_error(client):
    upload_response = upload(client, filename="pending.docx")
    document_id = upload_response.json()["document_id"]

    response = client.post("/api/knowledge/build", json={"document_id": document_id})

    assert response.status_code == 409
    assert response.json()["error_code"] == "DOCUMENT_NOT_PARSED"


def test_build_tender_document_is_rejected(client):
    document_id = parse_knowledge_fixture(client, doc_role="tender")

    response = client.post("/api/knowledge/build", json={"document_id": document_id})

    assert response.status_code == 409
    assert response.json()["error_code"] == "UNSUPPORTED_DOCUMENT_ROLE"


def test_list_missing_document_returns_structured_404(client):
    response = client.get("/api/documents/missing/knowledge-cards")

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"
