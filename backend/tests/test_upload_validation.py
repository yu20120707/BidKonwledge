from __future__ import annotations

from backend.tests.conftest import document_rows, upload


def assert_error_shape(response, code: str):
    body = response.json()
    assert set(body) == {"error_code", "message", "details"}
    assert body["error_code"] == code
    assert isinstance(body["message"], str)
    assert isinstance(body["details"], dict)


def assert_no_persistence(settings):
    assert not settings.upload_root.exists() or not any(settings.upload_root.iterdir())
    assert document_rows(settings) == []


def test_missing_file_is_rejected(client, test_settings):
    response = client.post(
        "/api/files/upload",
        data={"doc_role": "historical_bid"},
    )

    assert response.status_code == 400
    assert_error_shape(response, "MISSING_FILE")
    assert_no_persistence(test_settings)


def test_missing_doc_role_is_rejected(client, test_settings):
    response = client.post(
        "/api/files/upload",
        files={"file": ("sample.txt", b"hello", "text/plain")},
    )

    assert response.status_code == 400
    assert_error_shape(response, "MISSING_DOC_ROLE")
    assert_no_persistence(test_settings)


def test_invalid_doc_role_is_rejected(client, test_settings):
    response = upload(client, doc_role="unknown")

    assert response.status_code == 400
    assert_error_shape(response, "INVALID_DOC_ROLE")
    assert_no_persistence(test_settings)


def test_empty_file_is_rejected(client, test_settings):
    response = upload(client, content=b"")

    assert response.status_code == 400
    assert_error_shape(response, "EMPTY_FILE")
    assert_no_persistence(test_settings)


def test_unsafe_filename_is_rejected(client, test_settings):
    response = upload(client, filename="../evil.txt")

    assert response.status_code == 400
    assert_error_shape(response, "UNSAFE_FILENAME")
    assert_no_persistence(test_settings)


def test_windows_unsafe_filename_is_rejected(client, test_settings):
    response = upload(client, filename="..\\evil.txt")

    assert response.status_code == 400
    assert_error_shape(response, "UNSAFE_FILENAME")
    assert_no_persistence(test_settings)


def test_unsupported_extension_is_rejected(client, test_settings):
    response = upload(client, filename="payload.exe")

    assert response.status_code == 400
    assert_error_shape(response, "UNSUPPORTED_FILE_TYPE")
    assert_no_persistence(test_settings)


def test_oversized_upload_is_rejected(client, test_settings):
    response = upload(client, content=b"x" * (test_settings.max_upload_bytes + 1))

    assert response.status_code == 413
    assert_error_shape(response, "FILE_TOO_LARGE")
    assert_no_persistence(test_settings)


def test_uppercase_extension_is_normalized(client):
    response = upload(client, filename="SAMPLE.TXT")

    assert response.status_code == 201
