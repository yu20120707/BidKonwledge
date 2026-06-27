from __future__ import annotations

from backend.tests.conftest import upload


SUCCESS_FIELDS = {
    "document_id",
    "original_filename",
    "doc_role",
    "parse_status",
    "file_size",
    "created_at",
}


def test_upload_accepts_historical_bid(client):
    response = upload(client, doc_role="historical_bid")

    assert response.status_code == 201
    body = response.json()
    assert set(body) == SUCCESS_FIELDS
    assert body["doc_role"] == "historical_bid"
    assert body["original_filename"] == "sample.txt"


def test_upload_accepts_tender(client):
    response = upload(client, filename="tender.txt", doc_role="tender")

    assert response.status_code == 201
    assert response.json()["doc_role"] == "tender"


def test_upload_response_has_required_fields(client):
    response = upload(client)

    assert response.status_code == 201
    assert set(response.json()) == SUCCESS_FIELDS


def test_upload_response_parse_status_is_pending(client):
    response = upload(client)

    assert response.json()["parse_status"] == "pending"


def test_upload_response_does_not_expose_absolute_paths(client, test_settings):
    response = upload(client)

    body = response.json()
    serialized_values = " ".join(str(value) for value in body.values())
    assert str(test_settings.upload_root) not in serialized_values
    assert ":\\" not in serialized_values


def test_upload_preserves_unicode_original_filename(client):
    response = upload(client, filename="投标 测试 文件.txt")

    assert response.status_code == 201
    assert response.json()["original_filename"] == "投标 测试 文件.txt"
