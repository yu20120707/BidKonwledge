from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import unquote, urlparse

from backend.app.adapters.docling_parser import DoclingParserAdapter, DocumentParser, ParseError
from backend.app.adapters.ocr_adapter import OCRAdapter, OCRPageText, OCRError, PaddleOCRAdapter
from backend.app.adapters.word_converter import (
    WindowsWordComConverter,
    WordConversionError,
    WordConverter,
)
from backend.app.config import Settings
from backend.app.schemas.document import ParseDocumentResponse
from backend.app.services.document_format import detect_document_format
from backend.app.services.section_chunker import build_section_and_chunk_records
from backend.app.storage import database, file_storage


SUPPORTED_DIRECT_FORMATS = {"docx_zip", "pdf"}
PARSE_MODES = {"auto", "text", "ocr"}
MAX_ERROR_MESSAGE_CHARS = 500
WINDOWS_ABSOLUTE_PATH_PATTERN = re.compile(r"[A-Za-z]:[\\/][^\s\"'<>]+")
FILE_URI_WINDOWS_PATH_PATTERN = re.compile(r"file:/+[A-Za-z]:/[^\s\"'<>]+")


class DocumentNotFoundError(RuntimeError):
    pass


@dataclass(frozen=True)
class ParseResult:
    document_id: str
    sections_count: int
    chunks_count: int
    parse_status: str
    error_message: str | None = None
    parse_metadata: dict[str, object] | None = None

    def to_response(self) -> ParseDocumentResponse:
        return ParseDocumentResponse(
            document_id=self.document_id,
            sections_count=self.sections_count,
            chunks_count=self.chunks_count,
            parse_status=self.parse_status,
            error_message=self.error_message,
            parse_metadata=self.parse_metadata or {},
        )


def parse_document(
    settings: Settings,
    document_id: str,
    parser: DocumentParser | None = None,
    word_converter: WordConverter | None = None,
    ocr_adapter: OCRAdapter | None = None,
    parse_mode: str = "auto",
) -> ParseResult:
    document = database.get_document(settings, document_id)
    if document is None:
        raise DocumentNotFoundError(document_id)

    database.update_document_parse_status(settings, document_id, "parsing")

    normalized_parse_mode = parse_mode if parse_mode in PARSE_MODES else "auto"
    parse_metadata: dict[str, object] = {"parse_mode": normalized_parse_mode}

    try:
        stored_path = file_storage.resolve_upload_path(settings, document.stored_path)
        format_info = detect_document_format(stored_path)
        parse_metadata.update(format_info.to_metadata())

        parse_path = stored_path
        if format_info.requires_conversion:
            converter = word_converter or WindowsWordComConverter()
            converted_path = _converted_docx_path(settings, document_id)
            conversion_result = converter.convert_to_docx(stored_path, converted_path)
            parse_path = conversion_result.converted_path
            parse_metadata.update(
                {
                    "conversion_required": True,
                    "conversion_method": conversion_result.method,
                    "converted_path": file_storage.relative_stored_path(
                        settings, parse_path
                    ),
                }
            )
        else:
            parse_metadata.update(
                {
                    "conversion_required": False,
                    "conversion_method": None,
                    "converted_path": None,
                }
            )

        if format_info.detected_format not in SUPPORTED_DIRECT_FORMATS and not (
            format_info.detected_format == "legacy_ole_word"
            and parse_path.suffix.lower() == ".docx"
        ):
            message = (
                "Unsupported parse file extension or format: "
                f"{document.file_ext}/{format_info.detected_format}"
            )
            database.complete_document_parse_failure(
                settings, document_id, message, parse_metadata
            )
            return ParseResult(document_id, 0, 0, "failed", message, parse_metadata)

        active_parser = parser or DoclingParserAdapter()
        parsed_sections = _parse_sections_with_mode(
            parse_path=parse_path,
            detected_format=format_info.detected_format,
            parse_mode=normalized_parse_mode,
            parser=active_parser,
            ocr_adapter=ocr_adapter or PaddleOCRAdapter(),
            parse_metadata=parse_metadata,
        )
        section_records, chunk_records = build_section_and_chunk_records(
            document_id,
            parsed_sections,
            chunk_metadata=_chunk_metadata_from_parse_metadata(parse_metadata),
        )
        if (
            not chunk_records
            and format_info.detected_format == "pdf"
            and normalized_parse_mode == "auto"
            and parse_metadata.get("ocr_attempted") is not True
        ):
            parse_metadata["ocr_fallback_reason"] = "text_parse_produced_no_chunks"
            parsed_sections = _ocr_sections(
                parse_path,
                format_info.detected_format,
                ocr_adapter or PaddleOCRAdapter(),
                parse_metadata,
            )
            section_records, chunk_records = build_section_and_chunk_records(
                document_id,
                parsed_sections,
                chunk_metadata=_chunk_metadata_from_parse_metadata(parse_metadata),
            )
        if not section_records or not chunk_records:
            raise ParseError("Parser output did not produce any chunks")

        database.complete_document_parse_success(
            settings,
            document_id,
            section_records,
            chunk_records,
            parse_metadata,
        )
        return ParseResult(
            document_id,
            len(section_records),
            len(chunk_records),
            "parsed",
            parse_metadata=parse_metadata,
        )
    except Exception as exc:
        message = _safe_error_message(settings, exc)
        if isinstance(exc, WordConversionError):
            parse_metadata.setdefault("conversion_required", True)
            parse_metadata.setdefault("conversion_method", None)
        if isinstance(exc, OCRError):
            parse_metadata.setdefault("ocr_attempted", True)
        database.complete_document_parse_failure(
            settings, document_id, message, parse_metadata
        )
        return ParseResult(document_id, 0, 0, "failed", message, parse_metadata)


def _safe_error_message(settings: Settings, exc: Exception) -> str:
    message = str(exc) or exc.__class__.__name__
    message = FILE_URI_WINDOWS_PATH_PATTERN.sub("<local_path>", message)
    sensitive_paths = {
        str(settings.upload_root),
        str(settings.upload_root.resolve()),
        str(settings.database_path.parent),
        str(settings.database_path.parent.resolve()),
    }
    for path in sorted(sensitive_paths, key=len, reverse=True):
        if path:
            message = message.replace(path, "<local_path>")
            message = message.replace(path.replace("\\", "/"), "<local_path>")
            message = message.replace(_file_uri_for_path(path), "<local_path>")
    message = WINDOWS_ABSOLUTE_PATH_PATTERN.sub("<local_path>", message)
    if len(message) > MAX_ERROR_MESSAGE_CHARS:
        message = f"{message[:MAX_ERROR_MESSAGE_CHARS]}..."
    return message


def _file_uri_for_path(path: str) -> str:
    normalized = path.replace("\\", "/")
    if re.match(r"^[A-Za-z]:/", normalized):
        return f"file:///{normalized}"
    parsed = urlparse(normalized)
    if parsed.scheme == "file":
        return unquote(normalized)
    return f"file://{normalized}"


def _converted_docx_path(settings: Settings, document_id: str):
    return file_storage.resolve_upload_path(
        settings, f"_derived/{document_id}.converted.docx"
    )


def _parse_sections_with_mode(
    parse_path,
    detected_format: str,
    parse_mode: str,
    parser: DocumentParser,
    ocr_adapter: OCRAdapter,
    parse_metadata: dict[str, object],
):
    if parse_mode == "ocr":
        return _ocr_sections(parse_path, detected_format, ocr_adapter, parse_metadata)

    try:
        parse_metadata["ocr_attempted"] = False
        sections = parser.parse(parse_path)
        if not sections:
            raise ParseError("Parser output did not produce any sections")
        return sections
    except Exception as exc:
        if parse_mode == "text" or detected_format != "pdf":
            raise
        parse_metadata["ocr_fallback_reason"] = "text_parse_failed"
        return _ocr_sections(parse_path, detected_format, ocr_adapter, parse_metadata)


def _ocr_sections(
    parse_path,
    detected_format: str,
    ocr_adapter: OCRAdapter,
    parse_metadata: dict[str, object],
):
    if detected_format != "pdf":
        raise OCRError(f"OCR parse is only supported for PDF in Phase 8B: {detected_format}")
    pages = ocr_adapter.extract(parse_path)
    if not pages:
        raise OCRError("OCR produced no parseable text")
    parse_metadata.update(_ocr_metadata(pages))
    return [
        _ocr_page_to_section(page, index)
        for index, page in enumerate(pages)
        if page.text.strip()
    ]


def _ocr_page_to_section(page: OCRPageText, index: int):
    from backend.app.services.section_chunker import NormalizedSection

    return NormalizedSection(
        title=f"OCR Page {page.page_number}",
        level=1,
        order_index=index,
        text=page.text,
        page_start=page.page_number,
        page_end=page.page_number,
    )


def _ocr_metadata(pages: list[OCRPageText]) -> dict[str, object]:
    confidences = [page.confidence for page in pages if page.confidence is not None]
    return {
        "ocr_attempted": True,
        "ocr_engine": pages[0].engine if pages else "unknown",
        "ocr_pages_count": len(pages),
        "ocr_average_confidence": (
            round(sum(confidences) / len(confidences), 4) if confidences else None
        ),
    }


def _chunk_metadata_from_parse_metadata(
    parse_metadata: dict[str, object],
) -> dict[str, object]:
    keys = {
        "parse_mode",
        "ocr_attempted",
        "ocr_engine",
        "ocr_pages_count",
        "ocr_average_confidence",
    }
    return {key: value for key, value in parse_metadata.items() if key in keys}
