from __future__ import annotations

import sqlite3

from backend.tests.conftest import document_rows, upload


REQUIRED_COLUMNS = {
    "id",
    "original_filename",
    "stored_filename",
    "stored_path",
    "file_ext",
    "content_type",
    "file_size",
    "doc_role",
    "created_at",
    "updated_at",
    "parse_status",
    "error_message",
}


def test_database_initializes_and_documents_table_exists(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    assert test_settings.database_path.exists()
    connection = sqlite3.connect(test_settings.database_path)
    try:
        rows = connection.execute("PRAGMA table_info(documents)").fetchall()
    finally:
        connection.close()
    assert {row[1] for row in rows} == REQUIRED_COLUMNS


def test_valid_upload_inserts_one_metadata_row(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    assert len(document_rows(test_settings)) == 1


def test_metadata_row_stores_required_fields(client, test_settings):
    response = upload(client, filename="sample.txt", content=b"hello")

    assert response.status_code == 201
    row = document_rows(test_settings)[0]
    assert set(row.keys()) == REQUIRED_COLUMNS
    assert row["id"] == response.json()["document_id"]
    assert row["original_filename"] == "sample.txt"
    assert row["stored_path"] == row["stored_filename"]
    assert row["file_ext"] == ".txt"
    assert row["file_size"] == 5
    assert row["doc_role"] == "historical_bid"
    assert row["created_at"]
    assert row["updated_at"]


def test_nullable_metadata_defaults_are_safe(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    row = document_rows(test_settings)[0]
    assert row["content_type"] == "text/plain"
    assert row["error_message"] is None


def test_parse_status_remains_pending(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    assert document_rows(test_settings)[0]["parse_status"] == "pending"


def test_failed_upload_does_not_insert_metadata_row(client, test_settings):
    response = upload(client, filename="payload.exe")

    assert response.status_code == 400
    assert document_rows(test_settings) == []


def test_multiple_uploads_create_multiple_rows(client, test_settings):
    first = upload(client, filename="one.txt", content=b"one")
    second = upload(client, filename="two.txt", content=b"two")

    assert first.status_code == 201
    assert second.status_code == 201
    rows = document_rows(test_settings)
    assert len(rows) == 2
    assert len({row["id"] for row in rows}) == 2
