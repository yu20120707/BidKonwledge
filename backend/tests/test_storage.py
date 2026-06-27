from __future__ import annotations

from backend.tests.conftest import document_rows, upload


def test_file_write_failure_does_not_insert_metadata(client, test_settings, monkeypatch):
    def fail_write(*args, **kwargs):
        raise OSError("forced write failure")

    monkeypatch.setattr(
        "backend.app.api.files.file_storage.write_uploaded_bytes", fail_write
    )

    response = upload(client)

    assert response.status_code == 500
    assert response.json()["error_code"] == "FILE_WRITE_FAILED"
    assert document_rows(test_settings) == []
    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())


def test_metadata_write_failure_cleans_up_stored_file(client, test_settings, monkeypatch):
    def fail_insert(*args, **kwargs):
        raise OSError("forced metadata failure")

    monkeypatch.setattr("backend.app.api.files.database.insert_document", fail_insert)

    response = upload(client)

    assert response.status_code == 500
    assert response.json()["error_code"] == "METADATA_WRITE_FAILED"
    assert document_rows(test_settings) == []
    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())


def test_upload_directory_is_created(client, test_settings):
    assert not test_settings.upload_root.exists()

    response = upload(client)

    assert response.status_code == 201
    assert test_settings.upload_root.exists()


def test_stored_file_bytes_match_upload(client, test_settings):
    content = b"stored bytes"

    response = upload(client, content=content)

    assert response.status_code == 201
    files = list(test_settings.upload_root.iterdir())
    assert len(files) == 1
    assert files[0].read_bytes() == content


def test_stored_file_remains_under_upload_root(client, test_settings):
    response = upload(client)

    assert response.status_code == 201
    stored_file = next(test_settings.upload_root.iterdir()).resolve()
    upload_root = test_settings.upload_root.resolve()
    assert upload_root == stored_file.parent


def test_stored_filename_is_backend_generated(client, test_settings):
    response = upload(client, filename="raw-name.txt")

    assert response.status_code == 201
    row = document_rows(test_settings)[0]
    assert row["stored_filename"] != "raw-name.txt"
    assert row["stored_filename"].endswith(".txt")
    assert row["id"] in row["stored_filename"]


def test_duplicate_original_filenames_do_not_overwrite(client, test_settings):
    first = upload(client, filename="same.txt", content=b"first")
    second = upload(client, filename="same.txt", content=b"second")

    assert first.status_code == 201
    assert second.status_code == 201
    rows = document_rows(test_settings)
    assert len(rows) == 2
    stored_names = {row["stored_filename"] for row in rows}
    assert len(stored_names) == 2
    stored_bytes = sorted(path.read_bytes() for path in test_settings.upload_root.iterdir())
    assert stored_bytes == [b"first", b"second"]


def test_failed_validation_leaves_no_orphan_file(client, test_settings):
    response = upload(client, filename="payload.exe")

    assert response.status_code == 400
    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())
