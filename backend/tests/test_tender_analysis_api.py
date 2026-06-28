from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class TenderAnalysisParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="项目需求",
                level=1,
                order_index=0,
                text="本项目需求包括系统运维服务内容、现场实施和日常巡检。",
                page_start=1,
                page_end=2,
            ),
            NormalizedSection(
                title="评分标准",
                level=1,
                order_index=1,
                text="技术评分标准满分30分，评审重点包含服务方案和人员配置。",
                page_start=3,
                page_end=3,
            ),
            NormalizedSection(
                title="资格审查",
                level=1,
                order_index=2,
                text="投标文件不符合资格审查要求或出现无效投标情形将被否决。",
                page_start=4,
                page_end=4,
            ),
        ]


class LowSignalTenderParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="说明",
                level=1,
                order_index=0,
                text="这里是没有明显招标分析关键词的普通说明。",
            )
        ]


def parse_tender_fixture(client, doc_role: str = "tender", parser=None) -> str:
    app.dependency_overrides[get_document_parser] = lambda: parser or TenderAnalysisParser()
    upload_response = upload(client, filename="tender.docx", doc_role=doc_role)
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200
    assert parse_response.json()["parse_status"] == "parsed"
    return document_id


def test_analyze_parsed_tender_returns_evidence_items(client):
    document_id = parse_tender_fixture(client)

    response = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert response.status_code == 200
    body = response.json()
    assert body["document_id"] == document_id
    assert body["analysis_method"] == "deterministic_tender_v1"
    assert body["need_human_review"] is True
    assert body["metadata"]["source_chunks_count"] == 3

    requirement = body["project_requirements"][0]
    assert requirement["item_id"].startswith("tai_")
    assert requirement["item_type"] == "requirement"
    assert requirement["source_filename"] == "tender.docx"
    assert requirement["source_section_title"] == "项目需求"
    assert requirement["source_section_path"] == "项目需求"
    assert requirement["page_start"] == 1
    assert "需求" in requirement["matched_keywords"]

    scoring_item = body["scoring_items"][0]
    assert scoring_item["item_type"] == "scoring_item"
    assert scoring_item["score"] == 30.0
    assert "评分" in scoring_item["matched_keywords"]

    risk = body["disqualification_risks"][0]
    assert risk["item_type"] == "disqualification_risk"
    assert risk["severity"] == "high"
    assert "否决" in risk["matched_keywords"]
    assert "无效投标" in risk["matched_keywords"]
    assert "系统运维服务内容" in body["raw_text_summary"]


def test_get_existing_tender_analysis_returns_latest_result(client):
    document_id = parse_tender_fixture(client)
    analyze_response = client.post("/api/tender/analyze", json={"document_id": document_id})
    assert analyze_response.status_code == 200

    response = client.get(f"/api/documents/{document_id}/tender-analysis")

    assert response.status_code == 200
    assert response.json() == analyze_response.json()


def test_reanalyze_replaces_existing_analysis_deterministically(client):
    document_id = parse_tender_fixture(client)

    first = client.post("/api/tender/analyze", json={"document_id": document_id})
    second = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert first.status_code == 200
    assert second.status_code == 200
    first_body = first.json()
    second_body = second.json()
    assert [item["item_id"] for item in second_body["project_requirements"]] == [
        item["item_id"] for item in first_body["project_requirements"]
    ]
    assert len(second_body["project_requirements"]) == 1
    assert len(second_body["scoring_items"]) == 1
    assert len(second_body["disqualification_risks"]) == 1


def test_analyze_missing_document_returns_structured_404(client):
    response = client.post("/api/tender/analyze", json={"document_id": "missing"})

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"


def test_analyze_unparsed_tender_returns_structured_error(client):
    upload_response = upload(client, filename="pending.docx", doc_role="tender")
    document_id = upload_response.json()["document_id"]

    response = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert response.status_code == 409
    assert response.json()["error_code"] == "DOCUMENT_NOT_PARSED"


def test_analyze_historical_bid_is_rejected(client):
    document_id = parse_tender_fixture(client, doc_role="historical_bid")

    response = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert response.status_code == 409
    assert response.json()["error_code"] == "UNSUPPORTED_DOCUMENT_ROLE"


def test_low_signal_tender_keeps_human_review_marker(client):
    document_id = parse_tender_fixture(client, parser=LowSignalTenderParser())

    response = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert response.status_code == 200
    body = response.json()
    assert body["project_requirements"] == []
    assert body["scoring_items"] == []
    assert body["disqualification_risks"] == []
    assert body["need_human_review"] is True
    assert body["metadata"]["no_match"] is True


def test_get_missing_tender_analysis_returns_structured_404(client):
    document_id = parse_tender_fixture(client)

    response = client.get(f"/api/documents/{document_id}/tender-analysis")

    assert response.status_code == 404
    assert response.json()["error_code"] == "TENDER_ANALYSIS_NOT_FOUND"


def test_get_analysis_for_missing_document_returns_structured_404(client):
    response = client.get("/api/documents/missing/tender-analysis")

    assert response.status_code == 404
    assert response.json()["error_code"] == "DOCUMENT_NOT_FOUND"
