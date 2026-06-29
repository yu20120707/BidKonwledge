from __future__ import annotations

import sqlite3
from datetime import UTC, datetime
import json
from pathlib import Path
from typing import Any

from backend.app.config import Settings
from backend.app.schemas.document import (
    DocumentChunkRecord,
    DocumentRecord,
    DocumentSectionRecord,
    KnowledgeCardRecord,
    TenderAnalysisRecord,
)


CREATE_DOCUMENTS_SQL = """
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    original_filename TEXT NOT NULL,
    stored_filename TEXT NOT NULL,
    stored_path TEXT NOT NULL,
    file_ext TEXT NOT NULL,
    content_type TEXT,
    file_size INTEGER NOT NULL,
    doc_role TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    parse_status TEXT NOT NULL DEFAULT 'pending',
    error_message TEXT,
    parse_metadata_json TEXT NOT NULL DEFAULT '{}'
)
"""

CREATE_SECTIONS_SQL = """
CREATE TABLE IF NOT EXISTS document_sections (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    title TEXT NOT NULL,
    level INTEGER NOT NULL,
    order_index INTEGER NOT NULL,
    text TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE
)
"""

CREATE_CHUNKS_SQL = """
CREATE TABLE IF NOT EXISTS document_chunks (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    section_id TEXT NOT NULL,
    section_title TEXT NOT NULL,
    section_path TEXT NOT NULL,
    order_index INTEGER NOT NULL,
    chunk_index INTEGER NOT NULL,
    chunk_type TEXT NOT NULL,
    text TEXT NOT NULL,
    tags_json TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    metadata_json TEXT NOT NULL,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY(section_id) REFERENCES document_sections(id) ON DELETE CASCADE
)
"""

CREATE_KNOWLEDGE_CARDS_SQL = """
CREATE TABLE IF NOT EXISTS knowledge_cards (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    source_chunk_id TEXT NOT NULL,
    title TEXT NOT NULL,
    tag TEXT NOT NULL,
    content TEXT NOT NULL,
    source_filename TEXT NOT NULL,
    source_section_title TEXT NOT NULL,
    source_section_path TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    confidence REAL NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY(source_chunk_id) REFERENCES document_chunks(id) ON DELETE CASCADE
)
"""

CREATE_TENDER_ANALYSES_SQL = """
CREATE TABLE IF NOT EXISTS tender_analyses (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL UNIQUE,
    project_requirements_json TEXT NOT NULL,
    scoring_items_json TEXT NOT NULL,
    disqualification_risks_json TEXT NOT NULL,
    raw_text_summary TEXT NOT NULL,
    analysis_method TEXT NOT NULL,
    need_human_review INTEGER NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE
)
"""


def connect(database_path: Path) -> sqlite3.Connection:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_database(settings: Settings) -> None:
    with connect(settings.database_path) as connection:
        connection.execute(CREATE_DOCUMENTS_SQL)
        _ensure_documents_parse_metadata_column(connection)
        connection.execute(CREATE_SECTIONS_SQL)
        connection.execute(CREATE_CHUNKS_SQL)
        connection.execute(CREATE_KNOWLEDGE_CARDS_SQL)
        connection.execute(CREATE_TENDER_ANALYSES_SQL)
        connection.commit()


def insert_document(settings: Settings, record: DocumentRecord) -> None:
    init_database(settings)
    values: dict[str, Any] = _document_to_row(record)
    with connect(settings.database_path) as connection:
        connection.execute(
            """
            INSERT INTO documents (
                id,
                original_filename,
                stored_filename,
                stored_path,
                file_ext,
                content_type,
                file_size,
                doc_role,
                created_at,
                updated_at,
                parse_status,
                error_message,
                parse_metadata_json
            ) VALUES (
                :id,
                :original_filename,
                :stored_filename,
                :stored_path,
                :file_ext,
                :content_type,
                :file_size,
                :doc_role,
                :created_at,
                :updated_at,
                :parse_status,
                :error_message,
                :parse_metadata_json
            )
            """,
            values,
        )
        connection.commit()


def get_document(settings: Settings, document_id: str) -> DocumentRecord | None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        row = connection.execute(
            "SELECT * FROM documents WHERE id = ?", (document_id,)
        ).fetchone()
    if row is None:
        return None
    return _document_from_row(row)


def update_document_parse_status(
    settings: Settings,
    document_id: str,
    parse_status: str,
    error_message: str | None = None,
) -> bool:
    init_database(settings)
    updated_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    with connect(settings.database_path) as connection:
        cursor = connection.execute(
            """
            UPDATE documents
            SET parse_status = ?, error_message = ?, updated_at = ?
            WHERE id = ?
            """,
            (parse_status, error_message, updated_at, document_id),
        )
        connection.commit()
        return cursor.rowcount > 0


def complete_document_parse_success(
    settings: Settings,
    document_id: str,
    sections: list[DocumentSectionRecord],
    chunks: list[DocumentChunkRecord],
    parse_metadata: dict[str, Any] | None = None,
) -> None:
    init_database(settings)
    updated_at = _utc_now()
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        _insert_parse_outputs(connection, sections, chunks)
        if parse_metadata is None:
            connection.execute(
                """
                UPDATE documents
                SET parse_status = 'parsed', error_message = NULL, updated_at = ?
                WHERE id = ?
                """,
                (updated_at, document_id),
            )
        else:
            connection.execute(
                """
                UPDATE documents
                SET parse_status = 'parsed',
                    error_message = NULL,
                    updated_at = ?,
                    parse_metadata_json = ?
                WHERE id = ?
                """,
                (updated_at, json.dumps(parse_metadata, ensure_ascii=False), document_id),
            )
        connection.commit()


def complete_document_parse_failure(
    settings: Settings,
    document_id: str,
    error_message: str,
    parse_metadata: dict[str, Any] | None = None,
) -> None:
    init_database(settings)
    updated_at = _utc_now()
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        if parse_metadata is None:
            connection.execute(
                """
                UPDATE documents
                SET parse_status = 'failed', error_message = ?, updated_at = ?
                WHERE id = ?
                """,
                (error_message, updated_at, document_id),
            )
        else:
            connection.execute(
                """
                UPDATE documents
                SET parse_status = 'failed',
                    error_message = ?,
                    updated_at = ?,
                    parse_metadata_json = ?
                WHERE id = ?
                """,
                (
                    error_message,
                    updated_at,
                    json.dumps(parse_metadata, ensure_ascii=False),
                    document_id,
                ),
            )
        connection.commit()


def replace_document_parse_outputs(
    settings: Settings,
    document_id: str,
    sections: list[DocumentSectionRecord],
    chunks: list[DocumentChunkRecord],
) -> None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        _insert_parse_outputs(connection, sections, chunks)
        connection.commit()


def delete_document_parse_outputs(settings: Settings, document_id: str) -> None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        connection.commit()


def count_document_parse_outputs(settings: Settings, document_id: str) -> dict[str, int]:
    init_database(settings)
    with connect(settings.database_path) as connection:
        sections_row = connection.execute(
            "SELECT COUNT(*) AS count FROM document_sections WHERE document_id = ?",
            (document_id,),
        ).fetchone()
        chunks_row = connection.execute(
            "SELECT COUNT(*) AS count FROM document_chunks WHERE document_id = ?",
            (document_id,),
        ).fetchone()
    return {
        "sections_count": int(sections_row["count"]),
        "chunks_count": int(chunks_row["count"]),
    }


def list_document_chunks(
    settings: Settings, document_id: str
) -> list[DocumentChunkRecord]:
    init_database(settings)
    with connect(settings.database_path) as connection:
        rows = connection.execute(
            """
            SELECT * FROM document_chunks
            WHERE document_id = ?
            ORDER BY order_index ASC, chunk_index ASC
            """,
            (document_id,),
        ).fetchall()
    return [_chunk_from_row(row) for row in rows]


def replace_document_knowledge_cards(
    settings: Settings,
    document_id: str,
    cards: list[KnowledgeCardRecord],
) -> None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        connection.execute(
            "DELETE FROM knowledge_cards WHERE document_id = ?", (document_id,)
        )
        connection.executemany(
            """
            INSERT INTO knowledge_cards (
                id,
                document_id,
                source_chunk_id,
                title,
                tag,
                content,
                source_filename,
                source_section_title,
                source_section_path,
                page_start,
                page_end,
                confidence,
                metadata_json,
                created_at
            ) VALUES (
                :id,
                :document_id,
                :source_chunk_id,
                :title,
                :tag,
                :content,
                :source_filename,
                :source_section_title,
                :source_section_path,
                :page_start,
                :page_end,
                :confidence,
                :metadata_json,
                :created_at
            )
            """,
            [_knowledge_card_to_row(card) for card in cards],
        )
        connection.commit()


def list_document_knowledge_cards(
    settings: Settings, document_id: str
) -> list[KnowledgeCardRecord]:
    init_database(settings)
    with connect(settings.database_path) as connection:
        rows = connection.execute(
            """
            SELECT kc.*
            FROM knowledge_cards AS kc
            JOIN document_chunks AS c ON c.id = kc.source_chunk_id
            WHERE kc.document_id = ?
            ORDER BY c.order_index ASC, c.chunk_index ASC, kc.id ASC
            """,
            (document_id,),
        ).fetchall()
    return [_knowledge_card_from_row(row) for row in rows]


def replace_document_tender_analysis(
    settings: Settings,
    analysis: TenderAnalysisRecord,
) -> None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        connection.execute(
            "DELETE FROM tender_analyses WHERE document_id = ?",
            (analysis.document_id,),
        )
        connection.execute(
            """
            INSERT INTO tender_analyses (
                id,
                document_id,
                project_requirements_json,
                scoring_items_json,
                disqualification_risks_json,
                raw_text_summary,
                analysis_method,
                need_human_review,
                metadata_json,
                created_at
            ) VALUES (
                :id,
                :document_id,
                :project_requirements_json,
                :scoring_items_json,
                :disqualification_risks_json,
                :raw_text_summary,
                :analysis_method,
                :need_human_review,
                :metadata_json,
                :created_at
            )
            """,
            _tender_analysis_to_row(analysis),
        )
        connection.commit()


def get_document_tender_analysis(
    settings: Settings, document_id: str
) -> TenderAnalysisRecord | None:
    init_database(settings)
    with connect(settings.database_path) as connection:
        row = connection.execute(
            "SELECT * FROM tender_analyses WHERE document_id = ?",
            (document_id,),
        ).fetchone()
    if row is None:
        return None
    return _tender_analysis_from_row(row)


def list_retrievable_chunks(settings: Settings) -> list[dict[str, Any]]:
    init_database(settings)
    with connect(settings.database_path) as connection:
        rows = connection.execute(
            """
            SELECT
                c.*,
                d.original_filename,
                d.doc_role,
                d.file_ext
            FROM document_chunks AS c
            JOIN documents AS d ON d.id = c.document_id
            WHERE d.parse_status = 'parsed'
              AND d.doc_role = 'historical_bid'
            ORDER BY c.order_index ASC, c.chunk_index ASC, c.id ASC
            """
        ).fetchall()
    records: list[dict[str, Any]] = []
    for row in rows:
        values = dict(row)
        chunk = _chunk_from_row(row)
        values.update(chunk.model_dump())
        values.pop("tags_json", None)
        values.pop("metadata_json", None)
        records.append(values)
    return records


def list_retrievable_knowledge_card_chunks(settings: Settings) -> list[dict[str, Any]]:
    init_database(settings)
    with connect(settings.database_path) as connection:
        rows = connection.execute(
            """
            SELECT
                c.*,
                d.original_filename,
                d.doc_role,
                d.file_ext,
                kc.id AS knowledge_card_id,
                kc.tag AS knowledge_card_tag,
                kc.title AS knowledge_card_title,
                kc.content AS knowledge_card_content,
                kc.confidence AS knowledge_card_confidence,
                kc.metadata_json AS knowledge_card_metadata_json
            FROM knowledge_cards AS kc
            JOIN document_chunks AS c ON c.id = kc.source_chunk_id
            JOIN documents AS d ON d.id = kc.document_id
            WHERE d.parse_status = 'parsed'
              AND d.doc_role = 'historical_bid'
            ORDER BY c.order_index ASC, c.chunk_index ASC, kc.id ASC
            """
        ).fetchall()
    records: list[dict[str, Any]] = []
    for row in rows:
        values = dict(row)
        chunk = _chunk_from_row(row)
        card_tag = str(values["knowledge_card_tag"])
        card_metadata = json.loads(values["knowledge_card_metadata_json"])
        values.update(chunk.model_dump())
        values["tags"] = _append_unique(chunk.tags, card_tag)
        values["metadata"] = {
            **chunk.metadata,
            "knowledge_card": {
                "card_id": values["knowledge_card_id"],
                "tag": card_tag,
                "title": values["knowledge_card_title"],
                "confidence": values["knowledge_card_confidence"],
                "metadata": card_metadata,
            },
        }
        values.pop("tags_json", None)
        values.pop("metadata_json", None)
        values.pop("knowledge_card_metadata_json", None)
        records.append(values)
    return records


def count_documents(settings: Settings) -> int:
    init_database(settings)
    with connect(settings.database_path) as connection:
        row = connection.execute("SELECT COUNT(*) AS count FROM documents").fetchone()
    return int(row["count"])


def _chunk_to_row(chunk: DocumentChunkRecord) -> dict[str, Any]:
    values = chunk.model_dump()
    values["tags_json"] = json.dumps(chunk.tags, ensure_ascii=False)
    values["metadata_json"] = json.dumps(chunk.metadata, ensure_ascii=False)
    values.pop("tags")
    values.pop("metadata")
    return values


def _document_to_row(document: DocumentRecord) -> dict[str, Any]:
    values = document.model_dump()
    values["parse_metadata_json"] = json.dumps(
        document.parse_metadata, ensure_ascii=False
    )
    values.pop("parse_metadata")
    return values


def _document_from_row(row: sqlite3.Row) -> DocumentRecord:
    values = dict(row)
    metadata_json = values.pop("parse_metadata_json", "{}") or "{}"
    values["parse_metadata"] = json.loads(metadata_json)
    return DocumentRecord(**values)


def _ensure_documents_parse_metadata_column(connection: sqlite3.Connection) -> None:
    rows = connection.execute("PRAGMA table_info(documents)").fetchall()
    columns = {row[1] for row in rows}
    if "parse_metadata_json" not in columns:
        connection.execute(
            "ALTER TABLE documents ADD COLUMN parse_metadata_json TEXT NOT NULL DEFAULT '{}'"
        )


def _chunk_from_row(row: sqlite3.Row) -> DocumentChunkRecord:
    values = dict(row)
    values["tags"] = json.loads(values.pop("tags_json"))
    values["metadata"] = json.loads(values.pop("metadata_json"))
    return DocumentChunkRecord(**values)


def _knowledge_card_to_row(card: KnowledgeCardRecord) -> dict[str, Any]:
    values = card.model_dump()
    values["metadata_json"] = json.dumps(card.metadata, ensure_ascii=False)
    values.pop("metadata")
    return values


def _knowledge_card_from_row(row: sqlite3.Row) -> KnowledgeCardRecord:
    values = dict(row)
    values["metadata"] = json.loads(values.pop("metadata_json"))
    return KnowledgeCardRecord(**values)


def _append_unique(values: list[str], value: str) -> list[str]:
    if value in values:
        return list(values)
    return [*values, value]


def _tender_analysis_to_row(analysis: TenderAnalysisRecord) -> dict[str, Any]:
    return {
        "id": analysis.id,
        "document_id": analysis.document_id,
        "project_requirements_json": json.dumps(
            [item.model_dump() for item in analysis.project_requirements],
            ensure_ascii=False,
        ),
        "scoring_items_json": json.dumps(
            [item.model_dump() for item in analysis.scoring_items],
            ensure_ascii=False,
        ),
        "disqualification_risks_json": json.dumps(
            [item.model_dump() for item in analysis.disqualification_risks],
            ensure_ascii=False,
        ),
        "raw_text_summary": analysis.raw_text_summary,
        "analysis_method": analysis.analysis_method,
        "need_human_review": 1 if analysis.need_human_review else 0,
        "metadata_json": json.dumps(analysis.metadata, ensure_ascii=False),
        "created_at": analysis.created_at,
    }


def _tender_analysis_from_row(row: sqlite3.Row) -> TenderAnalysisRecord:
    from backend.app.schemas.document import TenderEvidenceItem

    values = dict(row)
    return TenderAnalysisRecord(
        id=values["id"],
        document_id=values["document_id"],
        project_requirements=[
            TenderEvidenceItem(**item)
            for item in json.loads(values["project_requirements_json"])
        ],
        scoring_items=[
            TenderEvidenceItem(**item)
            for item in json.loads(values["scoring_items_json"])
        ],
        disqualification_risks=[
            TenderEvidenceItem(**item)
            for item in json.loads(values["disqualification_risks_json"])
        ],
        raw_text_summary=values["raw_text_summary"],
        analysis_method=values["analysis_method"],
        need_human_review=bool(values["need_human_review"]),
        metadata=json.loads(values["metadata_json"]),
        created_at=values["created_at"],
    )


def _delete_parse_outputs(connection: sqlite3.Connection, document_id: str) -> None:
    connection.execute("DELETE FROM document_chunks WHERE document_id = ?", (document_id,))
    connection.execute("DELETE FROM document_sections WHERE document_id = ?", (document_id,))


def _insert_parse_outputs(
    connection: sqlite3.Connection,
    sections: list[DocumentSectionRecord],
    chunks: list[DocumentChunkRecord],
) -> None:
    connection.executemany(
        """
        INSERT INTO document_sections (
            id,
            document_id,
            title,
            level,
            order_index,
            text,
            page_start,
            page_end
        ) VALUES (
            :id,
            :document_id,
            :title,
            :level,
            :order_index,
            :text,
            :page_start,
            :page_end
        )
        """,
        [section.model_dump() for section in sections],
    )
    connection.executemany(
        """
        INSERT INTO document_chunks (
            id,
            document_id,
            section_id,
            section_title,
            section_path,
            order_index,
            chunk_index,
            chunk_type,
            text,
            tags_json,
            page_start,
            page_end,
            metadata_json
        ) VALUES (
            :id,
            :document_id,
            :section_id,
            :section_title,
            :section_path,
            :order_index,
            :chunk_index,
            :chunk_type,
            :text,
            :tags_json,
            :page_start,
            :page_end,
            :metadata_json
        )
        """,
        [_chunk_to_row(chunk) for chunk in chunks],
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")
