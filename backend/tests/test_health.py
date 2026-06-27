from __future__ import annotations


def test_health_returns_stable_shallow_status(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_does_not_create_database(client, test_settings):
    response = client.get("/health")

    assert response.status_code == 200
    assert not test_settings.database_path.exists()


def test_health_content_type_is_json(client):
    response = client.get("/health")

    assert "application/json" in response.headers["content-type"]
