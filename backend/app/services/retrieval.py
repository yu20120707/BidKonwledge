from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from backend.app.config import Settings
from backend.app.schemas.document import (
    RetrievalResponse,
    RetrievalResult,
    RetrievalSourceMetadata,
)
from backend.app.storage import database


class InvalidRetrievalRequestError(ValueError):
    pass


@dataclass(frozen=True)
class ScoredChunk:
    row: dict[str, Any]
    score: float


def retrieve_chunks(
    settings: Settings,
    query: str | None,
    tag: str | None,
    top_k: int,
) -> RetrievalResponse:
    normalized_query = _normalize_optional_text(query)
    normalized_tag = _normalize_optional_text(tag)
    if normalized_query is None and normalized_tag is None:
        raise InvalidRetrievalRequestError("At least one of query or tag is required")
    if top_k < 1:
        raise InvalidRetrievalRequestError("top_k must be greater than zero")

    query_terms = _query_terms(normalized_query)
    scored_by_chunk_id: dict[str, ScoredChunk] = {}
    rows = database.list_retrievable_chunks(settings)
    if normalized_tag is not None:
        rows = [
            *rows,
            *[
                row
                for row in database.list_retrievable_knowledge_card_chunks(settings)
                if row.get("knowledge_card_tag") == normalized_tag
            ],
        ]
    for row in rows:
        score = _score_row(row, query_terms, normalized_tag)
        if score is not None:
            _keep_best_score(scored_by_chunk_id, ScoredChunk(row=row, score=score))

    scored = list(scored_by_chunk_id.values())
    scored.sort(
        key=lambda item: (
            -item.score,
            int(item.row["order_index"]),
            int(item.row["chunk_index"]),
            str(item.row["id"]),
        )
    )
    results = [_to_result(item) for item in scored[:top_k]]
    return RetrievalResponse(query=normalized_query, tag=normalized_tag, results=results)


def _score_row(
    row: dict[str, Any],
    query_terms: list[str],
    tag: str | None,
) -> float | None:
    score = 0.0
    tags = [str(value) for value in row["tags"]]
    if tag is not None:
        if tag not in tags:
            return None
        score += 1.0

    if query_terms:
        searchable = _searchable_text(row)
        query_score = sum(searchable.count(term) for term in query_terms)
        if query_score == 0:
            return None
        score += float(query_score)

    return score


def _keep_best_score(
    scored_by_chunk_id: dict[str, ScoredChunk],
    item: ScoredChunk,
) -> None:
    chunk_id = str(item.row["id"])
    current = scored_by_chunk_id.get(chunk_id)
    if current is None or item.score > current.score:
        scored_by_chunk_id[chunk_id] = item
        return
    if item.score == current.score and _has_knowledge_card(item.row):
        scored_by_chunk_id[chunk_id] = item


def _has_knowledge_card(row: dict[str, Any]) -> bool:
    metadata = row.get("metadata")
    return isinstance(metadata, dict) and "knowledge_card" in metadata


def _to_result(item: ScoredChunk) -> RetrievalResult:
    row = item.row
    return RetrievalResult(
        chunk_id=row["id"],
        document_id=row["document_id"],
        section_id=row["section_id"],
        section_title=row["section_title"],
        section_path=row["section_path"],
        text=row["text"],
        tags=row["tags"],
        score=item.score,
        source=RetrievalSourceMetadata(
            original_filename=row["original_filename"],
            doc_role=row["doc_role"],
            file_ext=row["file_ext"],
            page_start=row["page_start"],
            page_end=row["page_end"],
            chunk_metadata=row["metadata"],
        ),
    )


def _query_terms(query: str | None) -> list[str]:
    if query is None:
        return []
    return [term.lower() for term in re.split(r"\s+", query) if term]


def _normalize_optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def _searchable_text(row: dict[str, Any]) -> str:
    parts = [
        row["text"],
        row["section_title"],
        row["section_path"],
        " ".join(row["tags"]),
    ]
    return "\n".join(str(part).lower() for part in parts)
