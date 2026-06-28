from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


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
    parse_metadata: dict[str, Any] = Field(default_factory=dict)


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


class KnowledgeCardRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    document_id: str
    source_chunk_id: str
    title: str
    tag: str
    content: str
    source_filename: str
    source_section_title: str
    source_section_path: str
    page_start: int | None = None
    page_end: int | None = None
    confidence: float
    metadata: dict[str, Any]
    created_at: str


class TenderEvidenceItem(BaseModel):
    item_id: str
    item_type: str
    title: str
    description: str
    source_filename: str
    source_chunk_id: str
    source_section_title: str
    source_section_path: str
    page_start: int | None = None
    page_end: int | None = None
    matched_keywords: list[str]
    severity: str | None = None
    score: float | None = None


class TenderAnalysisRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    document_id: str
    project_requirements: list[TenderEvidenceItem]
    scoring_items: list[TenderEvidenceItem]
    disqualification_risks: list[TenderEvidenceItem]
    raw_text_summary: str
    analysis_method: str
    need_human_review: bool
    metadata: dict[str, Any]
    created_at: str


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
    parse_metadata: dict[str, Any] = Field(default_factory=dict)


class ParseDocumentResponse(BaseModel):
    document_id: str
    sections_count: int
    chunks_count: int
    parse_status: str
    error_message: str | None = None
    parse_metadata: dict[str, Any] = Field(default_factory=dict)


class ParseDocumentRequest(BaseModel):
    parse_mode: Literal["auto", "text", "ocr"] = "auto"


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


class KnowledgeBuildRequest(BaseModel):
    document_id: str


class KnowledgeBuildResponse(BaseModel):
    document_id: str
    cards_count: int
    tags: list[str]


class KnowledgeCardResponse(BaseModel):
    card_id: str
    document_id: str
    source_chunk_id: str
    title: str
    tag: str
    content: str
    source_filename: str
    source_section_title: str
    source_section_path: str
    page_start: int | None = None
    page_end: int | None = None
    confidence: float
    metadata: dict[str, Any]
    created_at: str


class KnowledgeCardsResponse(BaseModel):
    document_id: str
    cards: list[KnowledgeCardResponse]


class TenderAnalyzeRequest(BaseModel):
    document_id: str


class TenderAnalysisResponse(BaseModel):
    document_id: str
    project_requirements: list[TenderEvidenceItem]
    scoring_items: list[TenderEvidenceItem]
    disqualification_risks: list[TenderEvidenceItem]
    raw_text_summary: str
    analysis_method: str
    need_human_review: bool
    metadata: dict[str, Any]


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
    llm_config: "GenerationLLMConfig | None" = None


class GenerationLLMConfig(BaseModel):
    api_key: str
    base_url: str | None = None
    model: str | None = None


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
