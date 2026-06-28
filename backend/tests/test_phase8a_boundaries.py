from __future__ import annotations

from pathlib import Path

from backend.app.api.documents import get_document_parser, get_word_converter
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


def test_phase8a_automated_parse_does_not_require_ocr_vector_llm_or_word_com(
    client, monkeypatch
):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("HAYSTACK_URL", raising=False)
    monkeypatch.delenv("PADDLEOCR_HOME", raising=False)

    class BoundaryParser:
        def parse(self, file_path: Path) -> list[NormalizedSection]:
            return [
                NormalizedSection(
                    title="边界测试",
                    level=1,
                    order_index=0,
                    text="自动化测试不依赖 OCR、向量库、LLM 或真实 Word COM。",
                )
            ]

    class BoundaryConverter:
        def convert_to_docx(self, source_path: Path, target_path: Path):
            from backend.app.adapters.word_converter import WordConversionResult

            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_bytes(b"PK converted")
            return WordConversionResult(
                converted_path=target_path, method="boundary_fake"
            )

    app.dependency_overrides[get_document_parser] = lambda: BoundaryParser()
    app.dependency_overrides[get_word_converter] = lambda: BoundaryConverter()
    upload_response = upload(
        client,
        filename="legacy.docx",
        content=bytes.fromhex("D0 CF 11 E0") + b"legacy",
    )
    document_id = upload_response.json()["document_id"]

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    assert response.json()["parse_status"] == "parsed"
    assert response.json()["parse_metadata"]["conversion_method"] == "boundary_fake"
