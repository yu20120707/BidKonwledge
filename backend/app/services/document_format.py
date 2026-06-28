from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


DOCX_ZIP_SIGNATURE = b"PK"
LEGACY_OLE_SIGNATURE = bytes.fromhex("D0 CF 11 E0")
PDF_SIGNATURE = b"%PDF"


@dataclass(frozen=True)
class DocumentFormatInfo:
    original_extension: str
    detected_format: str
    is_mislabeled: bool
    requires_conversion: bool

    def to_metadata(self) -> dict[str, object]:
        return {
            "original_extension": self.original_extension,
            "detected_format": self.detected_format,
            "is_mislabeled": self.is_mislabeled,
            "requires_conversion": self.requires_conversion,
        }


def detect_document_format(file_path: Path) -> DocumentFormatInfo:
    original_extension = file_path.suffix.lower()
    header = file_path.read_bytes()[:8]

    if header.startswith(DOCX_ZIP_SIGNATURE):
        detected_format = "docx_zip"
        expected_extensions = {".docx"}
    elif header.startswith(LEGACY_OLE_SIGNATURE):
        detected_format = "legacy_ole_word"
        expected_extensions = {".doc"}
    elif header.startswith(PDF_SIGNATURE):
        detected_format = "pdf"
        expected_extensions = {".pdf"}
    elif original_extension == ".txt":
        detected_format = "text"
        expected_extensions = {".txt"}
    else:
        detected_format = "unknown"
        expected_extensions = {original_extension}

    return DocumentFormatInfo(
        original_extension=original_extension,
        detected_format=detected_format,
        is_mislabeled=original_extension not in expected_extensions,
        requires_conversion=detected_format == "legacy_ole_word",
    )
