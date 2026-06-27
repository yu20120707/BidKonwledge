from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import JSONResponse

from backend.app.config import Settings, get_settings
from backend.app.schemas.document import DocumentRecord, DocumentUploadResponse
from backend.app.storage import database, file_storage

router = APIRouter(prefix="/api/files")
logger = logging.getLogger(__name__)

ALLOWED_DOC_ROLES = {"historical_bid", "tender"}


def error_response(
    status_code: int,
    error_code: str,
    message: str,
    details: dict[str, object] | None = None,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "error_code": error_code,
            "message": message,
            "details": details or {},
        },
    )


@router.post(
    "/upload",
    status_code=201,
    response_model=DocumentUploadResponse,
    responses={
        400: {"description": "Upload validation error"},
        413: {"description": "Upload exceeds configured size limit"},
        500: {"description": "Upload persistence error"},
    },
)
async def upload_file(
    file: UploadFile | None = File(default=None),
    doc_role: str | None = Form(default=None),
    settings: Settings = Depends(get_settings),
) -> DocumentUploadResponse | JSONResponse:
    if file is None:
        return error_response(400, "MISSING_FILE", "Uploaded file is required")
    if doc_role is None:
        return error_response(400, "MISSING_DOC_ROLE", "Document role is required")
    if doc_role not in ALLOWED_DOC_ROLES:
        return error_response(
            400,
            "INVALID_DOC_ROLE",
            "Unsupported document role",
            {"allowed": sorted(ALLOWED_DOC_ROLES)},
        )

    original_filename = file.filename or ""
    if file_storage.is_unsafe_filename(original_filename):
        return error_response(400, "UNSAFE_FILENAME", "Unsafe filename")

    file_ext = file_storage.normalized_extension(original_filename)
    if file_ext not in settings.allowed_extensions:
        return error_response(
            400,
            "UNSUPPORTED_FILE_TYPE",
            "Unsupported file extension",
            {"allowed": list(settings.allowed_extensions)},
        )

    content = await file.read()
    if len(content) == 0:
        return error_response(400, "EMPTY_FILE", "Uploaded file is empty")
    if len(content) > settings.max_upload_bytes:
        return error_response(
            413,
            "FILE_TOO_LARGE",
            "Uploaded file exceeds the configured size limit",
            {"max_upload_bytes": settings.max_upload_bytes},
        )

    document_id = uuid4().hex
    generated_filename = file_storage.stored_filename(document_id, file_ext)

    try:
        stored_path = file_storage.write_uploaded_bytes(
            settings, generated_filename, content
        )
    except OSError:
        logger.exception("Failed to write uploaded file")
        return error_response(500, "FILE_WRITE_FAILED", "Failed to store uploaded file")

    created_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    record = DocumentRecord(
        id=document_id,
        original_filename=original_filename,
        stored_filename=generated_filename,
        stored_path=file_storage.relative_stored_path(settings, stored_path),
        file_ext=file_ext,
        content_type=file.content_type,
        file_size=len(content),
        doc_role=doc_role,
        created_at=created_at,
        updated_at=created_at,
        parse_status="pending",
        error_message=None,
    )

    try:
        database.insert_document(settings, record)
    except Exception:
        try:
            Path(stored_path).unlink(missing_ok=True)
        except OSError:
            logger.exception("Failed to clean up stored file after metadata failure")
        logger.exception("Failed to insert document metadata")
        return error_response(
            500,
            "METADATA_WRITE_FAILED",
            "Failed to persist document metadata",
        )

    return DocumentUploadResponse(
        document_id=document_id,
        original_filename=original_filename,
        doc_role=doc_role,
        parse_status="pending",
        file_size=len(content),
        created_at=created_at,
    )
