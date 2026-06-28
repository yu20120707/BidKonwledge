from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class BoundaryParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="网络和数据安全防护保障措施",
                level=1,
                order_index=0,
                text="网络安全、数据安全、防护和保密要求均纳入服务保障。",
            )
        ]


def test_phase6_knowledge_cards_do_not_require_external_services(client, monkeypatch):
    for name in (
        "OPENAI_API_KEY",
        "QDRANT_URL",
        "HAYSTACK_API_KEY",
        "PADDLEOCR_HOME",
        "OCR_MODEL_DIR",
    ):
        monkeypatch.delenv(name, raising=False)

    app.dependency_overrides[get_document_parser] = lambda: BoundaryParser()
    upload_response = upload(client, filename="boundary.docx")
    document_id = upload_response.json()["document_id"]
    parse_response = client.post(f"/api/documents/{document_id}/parse")
    assert parse_response.status_code == 200

    response = client.post("/api/knowledge/build", json={"document_id": document_id})

    assert response.status_code == 200
    body = response.json()
    assert body["cards_count"] == 1
    assert body["tags"] == ["网络和数据安全防护保障措施"]
