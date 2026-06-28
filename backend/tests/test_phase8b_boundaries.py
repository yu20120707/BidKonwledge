from __future__ import annotations

from pathlib import Path

from backend.app.adapters.ocr_adapter import OCRPageText
from backend.app.api.documents import get_document_parser, get_ocr_adapter
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


def test_phase8b_ocr_tests_do_not_require_paddle_vector_or_llm(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("HAYSTACK_URL", raising=False)
    monkeypatch.delenv("PADDLEOCR_HOME", raising=False)

    class BoundaryParser:
        def parse(self, file_path: Path) -> list[NormalizedSection]:
            raise RuntimeError("force OCR fallback without external services")

    class BoundaryOCR:
        def extract(self, file_path: Path) -> list[OCRPageText]:
            return [
                OCRPageText(
                    page_number=1,
                    text="OCR fake result for isolated automated test.",
                    confidence=0.9,
                    engine="boundary_fake_ocr",
                )
            ]

    app.dependency_overrides[get_document_parser] = lambda: BoundaryParser()
    app.dependency_overrides[get_ocr_adapter] = lambda: BoundaryOCR()
    upload_response = upload(client, filename="scan.pdf", content=b"%PDF scan")
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    assert response.json()["parse_status"] == "parsed"
    assert response.json()["parse_metadata"]["ocr_engine"] == "boundary_fake_ocr"
