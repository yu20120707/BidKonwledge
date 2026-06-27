from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from backend.app.config import Settings, get_settings
from backend.app.main import app


@pytest.fixture
def test_settings(tmp_path: Path) -> Settings:
    return Settings(
        upload_root=tmp_path / "uploads",
        database_path=tmp_path / "app.sqlite3",
        max_upload_bytes=1024,
    )


@pytest.fixture
def client(test_settings: Settings) -> Iterator[TestClient]:
    app.dependency_overrides[get_settings] = lambda: test_settings
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def upload(
    client: TestClient,
    filename: str = "sample.txt",
    content: bytes = b"hello bid knowledge",
    doc_role: str = "historical_bid",
):
    return client.post(
        "/api/files/upload",
        data={"doc_role": doc_role},
        files={"file": (filename, content, "text/plain")},
    )


def document_rows(settings: Settings) -> list[sqlite3.Row]:
    if not settings.database_path.exists():
        return []
    connection = sqlite3.connect(settings.database_path)
    connection.row_factory = sqlite3.Row
    try:
        return list(connection.execute("SELECT * FROM documents ORDER BY created_at"))
    finally:
        connection.close()
