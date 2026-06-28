from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256

from backend.app.config import Settings
from backend.app.schemas.document import (
    KnowledgeBuildResponse,
    KnowledgeCardRecord,
)
from backend.app.services.tagger import prd_knowledge_tag
from backend.app.storage import database


class DocumentNotFoundError(Exception):
    pass


class DocumentNotParsedError(Exception):
    pass


class UnsupportedDocumentRoleError(Exception):
    pass


def build_knowledge_cards(settings: Settings, document_id: str) -> KnowledgeBuildResponse:
    document = database.get_document(settings, document_id)
    if document is None:
        raise DocumentNotFoundError
    if document.parse_status != "parsed":
        raise DocumentNotParsedError
    if document.doc_role != "historical_bid":
        raise UnsupportedDocumentRoleError

    chunks = database.list_document_chunks(settings, document_id)
    created_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    cards = [
        _card_from_chunk(
            document_id=document_id,
            source_filename=document.original_filename,
            source_chunk=chunk,
            created_at=created_at,
        )
        for chunk in chunks
        if chunk.text.strip()
    ]
    database.replace_document_knowledge_cards(settings, document_id, cards)
    return KnowledgeBuildResponse(
        document_id=document_id,
        cards_count=len(cards),
        tags=_unique_tags(cards),
    )


def _card_from_chunk(
    document_id: str,
    source_filename: str,
    source_chunk,
    created_at: str,
) -> KnowledgeCardRecord:
    tag, matched_keywords = prd_knowledge_tag(
        f"{source_chunk.section_title}\n{source_chunk.text}"
    )
    card_id = _deterministic_card_id(document_id, source_chunk.id, tag)
    confidence = 0.8 if matched_keywords else 0.3
    return KnowledgeCardRecord(
        id=card_id,
        document_id=document_id,
        source_chunk_id=source_chunk.id,
        title=source_chunk.section_title,
        tag=tag,
        content=source_chunk.text,
        source_filename=source_filename,
        source_section_title=source_chunk.section_title,
        source_section_path=source_chunk.section_path,
        page_start=source_chunk.page_start,
        page_end=source_chunk.page_end,
        confidence=confidence,
        metadata={
            "tagger": "prd_deterministic_v1",
            "matched_keywords": matched_keywords,
            "source_chunk_metadata": source_chunk.metadata,
        },
        created_at=created_at,
    )


def _deterministic_card_id(document_id: str, chunk_id: str, tag: str) -> str:
    digest = sha256(f"{document_id}:{chunk_id}:{tag}".encode("utf-8")).hexdigest()
    return f"kc_{digest[:24]}"


def _unique_tags(cards: list[KnowledgeCardRecord]) -> list[str]:
    tags: list[str] = []
    for card in cards:
        if card.tag not in tags:
            tags.append(card.tag)
    return tags
