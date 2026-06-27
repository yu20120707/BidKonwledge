from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class DocumentUploadResponse(BaseModel):
    document_id: str
    original_filename: str
    doc_role: str
    parse_status: str
    file_size: int
    created_at: str


class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: dict[str, object]


class DocumentRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    original_filename: str
    stored_filename: str
    stored_path: str
    file_ext: str
    content_type: str | None
    file_size: int
    doc_role: str
    created_at: str
    updated_at: str
    parse_status: str
    error_message: str | None = None
