from __future__ import annotations

from pathlib import Path

from backend.app.adapters.ocr_adapter import OCRError, OCRPageText
from backend.app.api.documents import get_document_parser, get_ocr_adapter
from backend.app.main import app
from backend.app.services.section_chunker import NormalizedSection
from backend.tests.conftest import upload


class TextPdfParser:
    def __init__(self):
        self.paths: list[Path] = []

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        self.paths.append(file_path)
        return [
            NormalizedSection(
                title="Text PDF",
                level=1,
                order_index=0,
                text="文本 PDF 继续走 Docling 文本解析路径，包含运维服务。",
                page_start=1,
                page_end=1,
            )
        ]


class EmptyTextParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        return [
            NormalizedSection(
                title="Empty",
                level=1,
                order_index=0,
                text="",
            )
        ]


class FailingTextParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        raise RuntimeError(r"parser failed near C:\Users\26561\secret\scan.pdf")


class ShouldNotRunParser:
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        raise AssertionError("text parser should not run")


class RecordingOCRAdapter:
    def __init__(self):
        self.paths: list[Path] = []

    def extract(self, file_path: Path) -> list[OCRPageText]:
        self.paths.append(file_path)
        return [
            OCRPageText(
                page_number=1,
                text="OCR 提取的扫描件内容，包含项目需求和运维服务。",
                confidence=0.91,
                engine="fake_ocr",
                blocks=[{"text": "OCR 提取的扫描件内容", "confidence": 0.91}],
            ),
            OCRPageText(
                page_number=2,
                text="第二页包含应急响应和服务质量保障。",
                confidence=0.81,
                engine="fake_ocr",
            ),
        ]


class ShouldNotRunOCR:
    def extract(self, file_path: Path) -> list[OCRPageText]:
        raise AssertionError("OCR should not run")


class FailingOCR:
    def extract(self, file_path: Path) -> list[OCRPageText]:
        raise OCRError(r"ocr failed near C:\Users\26561\secret\scan.pdf")


def override_parse_dependencies(parser, ocr_adapter) -> None:
    app.dependency_overrides[get_document_parser] = lambda: parser
    app.dependency_overrides[get_ocr_adapter] = lambda: ocr_adapter


def upload_pdf(client, filename: str = "scan.pdf") -> str:
    upload_response = upload(client, filename=filename, content=b"%PDF scanned bytes")
    assert upload_response.status_code == 201
    return upload_response.json()["document_id"]


def test_auto_parse_keeps_text_pdf_on_existing_parser_path(client):
    parser = TextPdfParser()
    override_parse_dependencies(parser, ShouldNotRunOCR())
    document_id = upload_pdf(client)

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert body["parse_metadata"]["parse_mode"] == "auto"
    assert body["parse_metadata"]["ocr_attempted"] is False
    assert len(parser.paths) == 1


def test_text_parse_mode_never_runs_ocr_on_parser_failure(client):
    override_parse_dependencies(FailingTextParser(), ShouldNotRunOCR())
    document_id = upload_pdf(client)

    response = client.post(
        f"/api/documents/{document_id}/parse",
        json={"parse_mode": "text"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "failed"
    assert body["parse_metadata"]["parse_mode"] == "text"
    assert body["parse_metadata"]["ocr_attempted"] is False
    assert "C:\\" not in body["error_message"]
    assert "<local_path>" in body["error_message"]


def test_ocr_parse_mode_uses_ocr_without_text_parser(client):
    ocr = RecordingOCRAdapter()
    override_parse_dependencies(ShouldNotRunParser(), ocr)
    document_id = upload_pdf(client)

    response = client.post(
        f"/api/documents/{document_id}/parse",
        json={"parse_mode": "ocr"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert body["sections_count"] == 2
    assert body["chunks_count"] == 2
    assert body["parse_metadata"]["parse_mode"] == "ocr"
    assert body["parse_metadata"]["ocr_attempted"] is True
    assert body["parse_metadata"]["ocr_engine"] == "fake_ocr"
    assert body["parse_metadata"]["ocr_pages_count"] == 2
    assert body["parse_metadata"]["ocr_average_confidence"] == 0.86
    assert len(ocr.paths) == 1

    chunks_response = client.get(f"/api/documents/{document_id}/chunks")
    assert chunks_response.status_code == 200
    chunk = chunks_response.json()["chunks"][0]
    assert chunk["page_start"] == 1
    assert chunk["metadata"]["ocr_attempted"] is True
    assert chunk["metadata"]["ocr_engine"] == "fake_ocr"
    assert "运维服务" in chunk["tags"]


def test_auto_parse_falls_back_to_ocr_when_text_parser_fails(client):
    ocr = RecordingOCRAdapter()
    override_parse_dependencies(FailingTextParser(), ocr)
    document_id = upload_pdf(client)

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert body["parse_metadata"]["parse_mode"] == "auto"
    assert body["parse_metadata"]["ocr_attempted"] is True
    assert body["parse_metadata"]["ocr_fallback_reason"] == "text_parse_failed"
    assert len(ocr.paths) == 1


def test_auto_parse_falls_back_to_ocr_when_text_parser_produces_no_chunks(client):
    ocr = RecordingOCRAdapter()
    override_parse_dependencies(EmptyTextParser(), ocr)
    document_id = upload_pdf(client)

    response = client.post(f"/api/documents/{document_id}/parse")

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "parsed"
    assert body["parse_metadata"]["ocr_attempted"] is True
    assert (
        body["parse_metadata"]["ocr_fallback_reason"]
        == "text_parse_produced_no_chunks"
    )


def test_ocr_failure_marks_parse_failed_without_absolute_path_leak(client):
    override_parse_dependencies(ShouldNotRunParser(), FailingOCR())
    document_id = upload_pdf(client)

    response = client.post(
        f"/api/documents/{document_id}/parse",
        json={"parse_mode": "ocr"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parse_status"] == "failed"
    assert body["sections_count"] == 0
    assert body["chunks_count"] == 0
    assert body["parse_metadata"]["ocr_attempted"] is True
    assert "C:\\" not in body["error_message"]
    assert "<local_path>" in body["error_message"]
