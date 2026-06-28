from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import unquote, urlparse

from backend.app.adapters.docling_parser import DoclingParserAdapter, DocumentParser, ParseError
from backend.app.config import Settings
from backend.app.schemas.document import ParseDocumentResponse
from backend.app.services.section_chunker import build_section_and_chunk_records
from backend.app.storage import database, file_storage


SUPPORTED_PARSE_EXTENSIONS = {".docx", ".pdf"}
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

    def to_response(self) -> ParseDocumentResponse:
        return ParseDocumentResponse(
            document_id=self.document_id,
            sections_count=self.sections_count,
            chunks_count=self.chunks_count,
            parse_status=self.parse_status,
            error_message=self.error_message,
        )


def parse_document(
    settings: Settings,
    document_id: str,
    parser: DocumentParser | None = None,
) -> ParseResult:
    document = database.get_document(settings, document_id)
    if document is None:
        raise DocumentNotFoundError(document_id)

    database.update_document_parse_status(settings, document_id, "parsing")

    if document.file_ext not in SUPPORTED_PARSE_EXTENSIONS:
        message = f"Unsupported parse file extension: {document.file_ext}"
        database.complete_document_parse_failure(settings, document_id, message)
        return ParseResult(document_id, 0, 0, "failed", message)

    try:
        stored_path = file_storage.resolve_upload_path(settings, document.stored_path)
        active_parser = parser or DoclingParserAdapter()
        parsed_sections = active_parser.parse(stored_path)
        section_records, chunk_records = build_section_and_chunk_records(
            document_id, parsed_sections
        )
        if not section_records or not chunk_records:
            raise ParseError("Parser output did not produce any chunks")

        database.complete_document_parse_success(
            settings,
            document_id,
            section_records,
            chunk_records,
        )
        return ParseResult(
            document_id,
            len(section_records),
            len(chunk_records),
            "parsed",
        )
    except Exception as exc:
        message = _safe_error_message(settings, exc)
        database.complete_document_parse_failure(settings, document_id, message)
        return ParseResult(document_id, 0, 0, "failed", message)


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
