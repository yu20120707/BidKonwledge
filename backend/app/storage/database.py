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
    error_message TEXT
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


def connect(database_path: Path) -> sqlite3.Connection:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_database(settings: Settings) -> None:
    with connect(settings.database_path) as connection:
        connection.execute(CREATE_DOCUMENTS_SQL)
        connection.execute(CREATE_SECTIONS_SQL)
        connection.execute(CREATE_CHUNKS_SQL)
        connection.commit()


def insert_document(settings: Settings, record: DocumentRecord) -> None:
    init_database(settings)
    values: dict[str, Any] = record.model_dump()
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
                error_message
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
                :error_message
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
    return DocumentRecord(**dict(row))


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
) -> None:
    init_database(settings)
    updated_at = _utc_now()
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        _insert_parse_outputs(connection, sections, chunks)
        connection.execute(
            """
            UPDATE documents
            SET parse_status = 'parsed', error_message = NULL, updated_at = ?
            WHERE id = ?
            """,
            (updated_at, document_id),
        )
        connection.commit()


def complete_document_parse_failure(
    settings: Settings,
    document_id: str,
    error_message: str,
) -> None:
    init_database(settings)
    updated_at = _utc_now()
    with connect(settings.database_path) as connection:
        _delete_parse_outputs(connection, document_id)
        connection.execute(
            """
            UPDATE documents
            SET parse_status = 'failed', error_message = ?, updated_at = ?
            WHERE id = ?
            """,
            (error_message, updated_at, document_id),
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


def _chunk_from_row(row: sqlite3.Row) -> DocumentChunkRecord:
    values = dict(row)
    values["tags"] = json.loads(values.pop("tags_json"))
    values["metadata"] = json.loads(values.pop("metadata_json"))
    return DocumentChunkRecord(**values)


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
