from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from backend.app.config import Settings
from backend.app.schemas.document import DocumentRecord


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


def connect(database_path: Path) -> sqlite3.Connection:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_database(settings: Settings) -> None:
    with connect(settings.database_path) as connection:
        connection.execute(CREATE_DOCUMENTS_SQL)
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


def count_documents(settings: Settings) -> int:
    init_database(settings)
    with connect(settings.database_path) as connection:
        row = connection.execute("SELECT COUNT(*) AS count FROM documents").fetchone()
    return int(row["count"])
