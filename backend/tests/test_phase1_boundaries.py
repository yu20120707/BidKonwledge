from __future__ import annotations

from backend.tests.conftest import document_rows, upload


def test_phase1_does_not_require_vector_service(client, monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "")

    response = upload(client)

    assert response.status_code == 201


def test_phase1_does_not_require_llm_credentials(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    response = upload(client)

    assert response.status_code == 201


def test_phase1_upload_does_not_parse_documents(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    row = document_rows(test_settings)[0]
    assert row["parse_status"] == "pending"
    assert row["error_message"] is None


def test_non_phase1_routes_are_not_exposed_as_complete_features(client):
    response = client.get("/api/knowledge-cards")

    assert response.status_code == 404
