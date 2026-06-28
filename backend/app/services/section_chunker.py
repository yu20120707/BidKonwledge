from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from uuid import uuid4

from backend.app.schemas.document import DocumentChunkRecord, DocumentSectionRecord
from backend.app.services.tagger import deterministic_tags


MAX_CHUNK_CHARS = 1200
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class NormalizedSection:
    title: str
    level: int
    order_index: int
    text: str
    page_start: int | None = None
    page_end: int | None = None


def split_markdown_sections(markdown: str) -> list[NormalizedSection]:
    lines = markdown.splitlines()
    sections: list[NormalizedSection] = []
    current_title = "Document"
    current_level = 1
    current_lines: list[str] = []
    saw_heading = False

    def flush() -> None:
        text = "\n".join(line for line in current_lines).strip()
        if text:
            sections.append(
                NormalizedSection(
                    title=current_title,
                    level=current_level,
                    order_index=len(sections),
                    text=text,
                )
            )

    for line in lines:
        match = HEADING_PATTERN.match(line)
        if match:
            flush()
            saw_heading = True
            current_title = match.group(2).strip()
            current_level = len(match.group(1))
            current_lines = []
            continue
        current_lines.append(line)

    flush()

    if sections:
        return sections

    text = markdown.strip()
    if not text:
        return []
    title = current_title if saw_heading else "Document"
    return [NormalizedSection(title=title, level=current_level, order_index=0, text=text)]


def build_section_and_chunk_records(
    document_id: str,
    sections: list[NormalizedSection],
    max_chunk_chars: int = MAX_CHUNK_CHARS,
    chunk_metadata: dict[str, Any] | None = None,
) -> tuple[list[DocumentSectionRecord], list[DocumentChunkRecord]]:
    section_records: list[DocumentSectionRecord] = []
    chunk_records: list[DocumentChunkRecord] = []

    for section in sections:
        section_id = uuid4().hex
        section_record = DocumentSectionRecord(
            id=section_id,
            document_id=document_id,
            title=section.title,
            level=section.level,
            order_index=section.order_index,
            text=section.text,
            page_start=section.page_start,
            page_end=section.page_end,
        )
        section_records.append(section_record)

        for chunk_index, chunk_text in enumerate(_split_text(section.text, max_chunk_chars)):
            tags = deterministic_tags(f"{section.title}\n{chunk_text}")
            chunk_records.append(
                DocumentChunkRecord(
                    id=uuid4().hex,
                    document_id=document_id,
                    section_id=section_id,
                    section_title=section.title,
                    section_path=section.title,
                    order_index=len(chunk_records),
                    chunk_index=chunk_index,
                    chunk_type="text",
                    text=chunk_text,
                    tags=tags,
                    page_start=section.page_start,
                    page_end=section.page_end,
                    metadata={
                        "section_level": section.level,
                        "tagger": "deterministic_v1",
                        **(chunk_metadata or {}),
                    },
                )
            )

    return section_records, chunk_records


def _split_text(text: str, max_chunk_chars: int) -> list[str]:
    paragraphs = [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text)]
    paragraphs = [paragraph for paragraph in paragraphs if paragraph]
    if not paragraphs:
        return []

    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        if len(paragraph) > max_chunk_chars:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(_split_long_text(paragraph, max_chunk_chars))
            continue
        candidate = paragraph if not current else f"{current}\n\n{paragraph}"
        if len(candidate) <= max_chunk_chars:
            current = candidate
        else:
            chunks.append(current)
            current = paragraph
    if current:
        chunks.append(current)
    return chunks


def _split_long_text(text: str, max_chunk_chars: int) -> list[str]:
    return [
        text[start : start + max_chunk_chars].strip()
        for start in range(0, len(text), max_chunk_chars)
        if text[start : start + max_chunk_chars].strip()
    ]
