from __future__ import annotations

from backend.app.services.document_format import detect_document_format


def test_detect_true_docx_from_zip_header(tmp_path):
    path = tmp_path / "proposal.docx"
    path.write_bytes(b"PK\x03\x04docx")

    info = detect_document_format(path)

    assert info.original_extension == ".docx"
    assert info.detected_format == "docx_zip"
    assert info.is_mislabeled is False
    assert info.requires_conversion is False


def test_detect_legacy_ole_doc_from_header(tmp_path):
    path = tmp_path / "legacy.doc"
    path.write_bytes(bytes.fromhex("D0 CF 11 E0") + b"legacy")

    info = detect_document_format(path)

    assert info.original_extension == ".doc"
    assert info.detected_format == "legacy_ole_word"
    assert info.is_mislabeled is False
    assert info.requires_conversion is True


def test_detect_mislabeled_docx_as_legacy_ole(tmp_path):
    path = tmp_path / "mislabeled.docx"
    path.write_bytes(bytes.fromhex("D0 CF 11 E0") + b"legacy")

    info = detect_document_format(path)

    assert info.original_extension == ".docx"
    assert info.detected_format == "legacy_ole_word"
    assert info.is_mislabeled is True
    assert info.requires_conversion is True


def test_detect_pdf_from_header(tmp_path):
    path = tmp_path / "tender.pdf"
    path.write_bytes(b"%PDF-1.7 text")

    info = detect_document_format(path)

    assert info.detected_format == "pdf"
    assert info.is_mislabeled is False
    assert info.requires_conversion is False


def test_unknown_binary_format_is_not_conversion_candidate(tmp_path):
    path = tmp_path / "payload.docx"
    path.write_bytes(b"not a real office file")

    info = detect_document_format(path)

    assert info.detected_format == "unknown"
    assert info.is_mislabeled is False
    assert info.requires_conversion is False
