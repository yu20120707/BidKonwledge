from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.adapters.docling_parser import DoclingParserAdapter, DocumentParser
from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import (
    DocumentChunkResponse,
    DocumentChunksResponse,
    DocumentDetailResponse,
    ParseDocumentResponse,
)
from backend.app.services import document_parsing
from backend.app.storage import database

router = APIRouter(prefix="/api/documents")


def get_document_parser() -> DocumentParser:
    return DoclingParserAdapter()


@router.post(
    "/{document_id}/parse",
    response_model=ParseDocumentResponse,
    responses={404: {"description": "Document not found"}},
)
def parse_document(
    document_id: str,
    settings: Settings = Depends(get_settings),
    parser: DocumentParser = Depends(get_document_parser),
) -> ParseDocumentResponse | JSONResponse:
    try:
        result = document_parsing.parse_document(settings, document_id, parser)
    except document_parsing.DocumentNotFoundError:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    return result.to_response()


@router.get(
    "/{document_id}",
    response_model=DocumentDetailResponse,
    responses={404: {"description": "Document not found"}},
)
def get_document(
    document_id: str,
    settings: Settings = Depends(get_settings),
) -> DocumentDetailResponse | JSONResponse:
    document = database.get_document(settings, document_id)
    if document is None:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    counts = database.count_document_parse_outputs(settings, document_id)
    return DocumentDetailResponse(
        document_id=document.id,
        original_filename=document.original_filename,
        doc_role=document.doc_role,
        file_ext=document.file_ext,
        file_size=document.file_size,
        parse_status=document.parse_status,
        error_message=document.error_message,
        created_at=document.created_at,
        updated_at=document.updated_at,
        sections_count=counts["sections_count"],
        chunks_count=counts["chunks_count"],
    )


@router.get(
    "/{document_id}/chunks",
    response_model=DocumentChunksResponse,
    responses={404: {"description": "Document not found"}},
)
def get_document_chunks(
    document_id: str,
    settings: Settings = Depends(get_settings),
) -> DocumentChunksResponse | JSONResponse:
    if database.get_document(settings, document_id) is None:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    chunks = [
        DocumentChunkResponse(
            chunk_id=chunk.id,
            document_id=chunk.document_id,
            section_id=chunk.section_id,
            section_title=chunk.section_title,
            section_path=chunk.section_path,
            order_index=chunk.order_index,
            chunk_index=chunk.chunk_index,
            chunk_type=chunk.chunk_type,
            text=chunk.text,
            tags=chunk.tags,
            page_start=chunk.page_start,
            page_end=chunk.page_end,
            metadata=chunk.metadata,
        )
        for chunk in database.list_document_chunks(settings, document_id)
    ]
    return DocumentChunksResponse(document_id=document_id, chunks=chunks)
