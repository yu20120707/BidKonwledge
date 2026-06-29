from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class RetrievalParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="运维服务方案",
                level=1,
                order_index=0,
                text="运维服务覆盖日常巡检，运维服务质量管理和项目管理。",
                page_start=1,
                page_end=2,
            ),
            NormalizedSection(
                title="运维服务应急",
                level=1,
                order_index=1,
                text="运维服务支持应急响应和突发事件处理。",
                page_start=3,
                page_end=3,
            ),
            NormalizedSection(
                title="商务报价",
                level=1,
                order_index=2,
                text="报价费用说明和价格构成。",
                page_start=4,
                page_end=4,
            ),
        ]


def parse_retrieval_fixture(client) -> str:
    app.dependency_overrides[get_document_parser] = lambda: RetrievalParser()
    upload_response = upload(client, filename="retrieval.docx")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"
    return document_id


def test_tag_only_retrieval_returns_matching_chunks_with_source_metadata(client):
    document_id = parse_retrieval_fixture(client)

    response = client.post("/api/retrieve", json={"tag": "应急响应", "top_k": 5})

    assert response.status_code == 200
    body = response.json()
    assert body["query"] is None
    assert body["tag"] == "应急响应"
    assert len(body["results"]) == 1
    result = body["results"][0]
    assert result["document_id"] == document_id
    assert result["section_title"] == "运维服务应急"
    assert result["section_path"] == "运维服务应急"
    assert "应急响应" in result["tags"]
    assert result["score"] == 1.0
    assert result["source"]["original_filename"] == "retrieval.docx"
    assert result["source"]["doc_role"] == "historical_bid"
    assert result["source"]["file_ext"] == ".docx"
    assert result["source"]["page_start"] == 3
    assert result["source"]["chunk_metadata"]["tagger"] == "deterministic_v1"


def test_query_only_retrieval_matches_keywords(client):
    parse_retrieval_fixture(client)

    response = client.post("/api/retrieve", json={"query": "巡检", "top_k": 5})

    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 1
    assert results[0]["section_title"] == "运维服务方案"
    assert "巡检" in results[0]["text"]


def test_query_only_retrieval_is_stable_after_knowledge_build(client):
    document_id = parse_retrieval_fixture(client)

    before = client.post("/api/retrieve", json={"query": "运维服务", "top_k": 5})
    assert before.status_code == 200
    build_response = client.post("/api/knowledge/build", json={"document_id": document_id})
    assert build_response.status_code == 200
    after = client.post("/api/retrieve", json={"query": "运维服务", "top_k": 5})

    assert after.status_code == 200
    before_results = before.json()["results"]
    after_results = after.json()["results"]
    assert [result["chunk_id"] for result in after_results] == [
        result["chunk_id"] for result in before_results
    ]
    assert all("knowledge_card" not in result["source"]["chunk_metadata"] for result in after_results)


def test_tag_and_query_retrieval_intersects_filters(client):
    parse_retrieval_fixture(client)

    response = client.post(
        "/api/retrieve",
        json={"tag": "运维服务", "query": "突发", "top_k": 5},
    )

    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 1
    assert results[0]["section_title"] == "运维服务应急"
    assert "运维服务" in results[0]["tags"]
    assert "突发" in results[0]["text"]


def test_prd_knowledge_card_tag_retrieval_returns_source_chunk(client):
    document_id = parse_retrieval_fixture(client)
    build_response = client.post("/api/knowledge/build", json={"document_id": document_id})
    assert build_response.status_code == 200

    response = client.post(
        "/api/retrieve",
        json={"tag": "突发应急方案和措施", "query": "突发", "top_k": 5},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["tag"] == "突发应急方案和措施"
    results = body["results"]
    assert len(results) == 1
    result = results[0]
    assert result["document_id"] == document_id
    assert result["section_title"] == "运维服务应急"
    assert "突发应急方案和措施" in result["tags"]
    card_metadata = result["source"]["chunk_metadata"]["knowledge_card"]
    assert card_metadata["card_id"].startswith("kc_")
    assert card_metadata["tag"] == "突发应急方案和措施"
    assert card_metadata["metadata"]["tagger"] == "prd_deterministic_v1"


def test_prd_tag_collision_prefers_knowledge_card_metadata(client):
    document_id = parse_retrieval_fixture(client)
    build_response = client.post("/api/knowledge/build", json={"document_id": document_id})
    assert build_response.status_code == 200

    response = client.post("/api/retrieve", json={"tag": "商务报价", "top_k": 5})

    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 1
    result = results[0]
    assert result["section_title"] == "商务报价"
    assert "商务报价" in result["tags"]
    assert result["source"]["chunk_metadata"]["knowledge_card"]["tag"] == "商务报价"


def test_tender_documents_are_excluded_from_retrieval_evidence(client):
    app.dependency_overrides[get_document_parser] = lambda: RetrievalParser()
    upload_response = upload(client, filename="tender-retrieval.docx", doc_role="tender")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"

    response = client.post("/api/retrieve", json={"tag": "应急响应", "top_k": 5})

    assert response.status_code == 200
    assert response.json()["results"] == []


def test_retrieval_mixed_historical_and_tender_returns_only_historical(client):
    app.dependency_overrides[get_document_parser] = lambda: RetrievalParser()
    historical_upload = upload(client, filename="historical-retrieval.docx", doc_role="historical_bid")
    historical_document_id = historical_upload.json()["document_id"]
    assert client.post(f"/api/documents/{historical_document_id}/parse").status_code == 200
    tender_upload = upload(client, filename="tender-retrieval.docx", doc_role="tender")
    tender_document_id = tender_upload.json()["document_id"]
    assert client.post(f"/api/documents/{tender_document_id}/parse").status_code == 200

    response = client.post("/api/retrieve", json={"tag": "应急响应", "top_k": 5})

    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 1
    assert results[0]["document_id"] == historical_document_id
    assert results[0]["source"]["doc_role"] == "historical_bid"


def test_retrieval_can_use_multiple_historical_documents(client):
    app.dependency_overrides[get_document_parser] = lambda: RetrievalParser()
    first_upload = upload(client, filename="historical-primary.docx", doc_role="historical_bid")
    first_document_id = first_upload.json()["document_id"]
    assert client.post(f"/api/documents/{first_document_id}/parse").status_code == 200
    second_upload = upload(client, filename="historical-qualification.docx", doc_role="historical_bid")
    second_document_id = second_upload.json()["document_id"]
    assert client.post(f"/api/documents/{second_document_id}/parse").status_code == 200

    response = client.post("/api/retrieve", json={"tag": "应急响应", "top_k": 5})

    assert response.status_code == 200
    results = response.json()["results"]
    assert {result["document_id"] for result in results} == {first_document_id, second_document_id}
    assert {result["source"]["original_filename"] for result in results} == {
        "historical-primary.docx",
        "historical-qualification.docx",
    }
    assert all(result["source"]["doc_role"] == "historical_bid" for result in results)


def test_retrieval_no_match_returns_empty_results(client):
    parse_retrieval_fixture(client)

    response = client.post(
        "/api/retrieve",
        json={"tag": "商务报价", "query": "巡检", "top_k": 5},
    )

    assert response.status_code == 200
    assert response.json()["results"] == []


def test_retrieval_ordering_and_scores_are_deterministic(client):
    parse_retrieval_fixture(client)

    response = client.post(
        "/api/retrieve",
        json={"query": "运维服务", "top_k": 2},
    )

    assert response.status_code == 200
    results = response.json()["results"]
    assert [result["section_title"] for result in results] == [
        "运维服务方案",
        "运维服务应急",
    ]
    assert [result["score"] for result in results] == [5.0, 4.0]


def test_retrieval_requires_query_or_tag(client):
    response = client.post("/api/retrieve", json={"top_k": 5})

    assert response.status_code == 400
    assert response.json()["error_code"] == "INVALID_RETRIEVAL_REQUEST"
