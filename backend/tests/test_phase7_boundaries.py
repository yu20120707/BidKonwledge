from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class BoundaryTenderParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="评分标准",
                level=1,
                order_index=0,
                text="评分标准包含技术分20分，不符合资格审查要求将被否决。",
            )
        ]


def test_phase7_tender_analysis_does_not_require_external_services(
    client, monkeypatch
):
    for name in (
        "OPENAI_API_KEY",
        "QDRANT_URL",
        "HAYSTACK_API_KEY",
        "PADDLEOCR_HOME",
        "OCR_MODEL_DIR",
    ):
        monkeypatch.delenv(name, raising=False)

    app.dependency_overrides[get_document_parser] = lambda: BoundaryTenderParser()
    upload_response = upload(client, filename="boundary-tender.docx", doc_role="tender")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.post("/api/tender/analyze", json={"document_id": document_id})

    assert response.status_code == 200
    body = response.json()
    assert body["scoring_items"][0]["score"] == 20.0
    assert body["disqualification_risks"][0]["severity"] == "high"
