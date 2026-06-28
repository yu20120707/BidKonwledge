from __future__ import annotations

from typing import Any

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


class DocumentSectionRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    document_id: str
    title: str
    level: int
    order_index: int
    text: str
    page_start: int | None = None
    page_end: int | None = None


class DocumentChunkRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    document_id: str
    section_id: str
    section_title: str
    section_path: str
    order_index: int
    chunk_index: int
    chunk_type: str
    text: str
    tags: list[str]
    page_start: int | None = None
    page_end: int | None = None
    metadata: dict[str, Any]


class DocumentDetailResponse(BaseModel):
    document_id: str
    original_filename: str
    doc_role: str
    file_ext: str
    file_size: int
    parse_status: str
    error_message: str | None
    created_at: str
    updated_at: str
    sections_count: int
    chunks_count: int


class ParseDocumentResponse(BaseModel):
    document_id: str
    sections_count: int
    chunks_count: int
    parse_status: str
    error_message: str | None = None


class DocumentChunkResponse(BaseModel):
    chunk_id: str
    document_id: str
    section_id: str
    section_title: str
    section_path: str
    order_index: int
    chunk_index: int
    chunk_type: str
    text: str
    tags: list[str]
    page_start: int | None = None
    page_end: int | None = None
    metadata: dict[str, Any]


class DocumentChunksResponse(BaseModel):
    document_id: str
    chunks: list[DocumentChunkResponse]


class RetrievalRequest(BaseModel):
    query: str | None = None
    tag: str | None = None
    top_k: int = 5


class RetrievalSourceMetadata(BaseModel):
    original_filename: str
    doc_role: str
    file_ext: str
    page_start: int | None = None
    page_end: int | None = None
    chunk_metadata: dict[str, Any]


class RetrievalResult(BaseModel):
    chunk_id: str
    document_id: str
    section_id: str
    section_title: str
    section_path: str
    text: str
    tags: list[str]
    score: float
    source: RetrievalSourceMetadata


class RetrievalResponse(BaseModel):
    query: str | None
    tag: str | None
    results: list[RetrievalResult]


class GenerationRequest(BaseModel):
    target_tag: str
    query: str
    top_k: int = 5


class Citation(BaseModel):
    source_filename: str
    source_section_title: str
    content_snippet: str
    chunk_id: str
    document_id: str


class RiskItem(BaseModel):
    risk_type: str
    description: str
    severity: str
    source_text: str | None = None


class GenerationResponse(BaseModel):
    target_tag: str
    generated_content: str
    citations: list[Citation]
    risks: list[RiskItem]
    need_human_review: bool
