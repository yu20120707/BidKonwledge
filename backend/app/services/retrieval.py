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
    scored: list[ScoredChunk] = []
    for row in database.list_retrievable_chunks(settings):
        score = _score_row(row, query_terms, normalized_tag)
        if score is not None:
            scored.append(ScoredChunk(row=row, score=score))

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
