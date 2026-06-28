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
