from __future__ import annotations

from backend.app.schemas.document import Citation, RetrievalResult


SNIPPET_CHARS = 120


def build_citations(results: list[RetrievalResult]) -> list[Citation]:
    citations: list[Citation] = []
    for result in results:
        citations.append(
            Citation(
                source_filename=result.source.original_filename,
                source_section_title=result.section_title,
                content_snippet=_snippet(result.text),
                chunk_id=result.chunk_id,
                document_id=result.document_id,
            )
        )
    return citations


def normalize_generated_content(content: str) -> str:
    return content.strip()


def _snippet(text: str) -> str:
    normalized = " ".join(text.split())
    if len(normalized) <= SNIPPET_CHARS:
        return normalized
    return normalized[:SNIPPET_CHARS].rstrip()
