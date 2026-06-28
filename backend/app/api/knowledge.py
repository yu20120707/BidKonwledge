from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import (
    KnowledgeBuildRequest,
    KnowledgeBuildResponse,
    KnowledgeCardResponse,
    KnowledgeCardsResponse,
)
from backend.app.services import knowledge_cards
from backend.app.storage import database

router = APIRouter(prefix="/api")


@router.post(
    "/knowledge/build",
    response_model=KnowledgeBuildResponse,
    responses={
        404: {"description": "Document not found"},
        409: {"description": "Document is not ready for knowledge cards"},
    },
)
def build_knowledge_cards(
    request: KnowledgeBuildRequest,
    settings: Settings = Depends(get_settings),
) -> KnowledgeBuildResponse | JSONResponse:
    try:
        return knowledge_cards.build_knowledge_cards(settings, request.document_id)
    except knowledge_cards.DocumentNotFoundError:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    except knowledge_cards.DocumentNotParsedError:
        return error_response(409, "DOCUMENT_NOT_PARSED", "Document is not parsed")
    except knowledge_cards.UnsupportedDocumentRoleError:
        return error_response(
            409,
            "UNSUPPORTED_DOCUMENT_ROLE",
            "Knowledge cards are only supported for historical bid documents",
        )


@router.get(
    "/documents/{document_id}/knowledge-cards",
    response_model=KnowledgeCardsResponse,
    responses={404: {"description": "Document not found"}},
)
def list_knowledge_cards(
    document_id: str,
    settings: Settings = Depends(get_settings),
) -> KnowledgeCardsResponse | JSONResponse:
    if database.get_document(settings, document_id) is None:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    cards = [
        KnowledgeCardResponse(
            card_id=card.id,
            document_id=card.document_id,
            source_chunk_id=card.source_chunk_id,
            title=card.title,
            tag=card.tag,
            content=card.content,
            source_filename=card.source_filename,
            source_section_title=card.source_section_title,
            source_section_path=card.source_section_path,
            page_start=card.page_start,
            page_end=card.page_end,
            confidence=card.confidence,
            metadata=card.metadata,
            created_at=card.created_at,
        )
        for card in database.list_document_knowledge_cards(settings, document_id)
    ]
    return KnowledgeCardsResponse(document_id=document_id, cards=cards)
