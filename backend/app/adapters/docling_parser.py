from __future__ import annotations

from pathlib import Path
from typing import Protocol

from backend.app.services.section_chunker import NormalizedSection, split_markdown_sections


class DocumentParser(Protocol):
    def parse(self, file_path: Path) -> list[NormalizedSection]:
        """Parse a local document into normalized sections."""


class ParseError(RuntimeError):
    """Raised when a document cannot be parsed into text sections."""


class DoclingParserAdapter:
    supported_extensions = {".docx", ".pdf"}

    def parse(self, file_path: Path) -> list[NormalizedSection]:
        file_ext = file_path.suffix.lower()
        if file_ext not in self.supported_extensions:
            raise ParseError(f"Unsupported parse file extension: {file_ext}")

        try:
            from docling.document_converter import DocumentConverter
            from docling.document_converter import PdfFormatOption
            from docling.datamodel.base_models import InputFormat
            from docling.datamodel.pipeline_options import PdfPipelineOptions
        except ImportError as exc:
            raise ParseError(
                "Docling is not installed. Install the parsing extra with "
                "`pip install -e .[parsing]` before real document parsing."
            ) from exc

        try:
            converter = DocumentConverter(allowed_formats=[InputFormat.DOCX])
            if file_ext == ".pdf":
                pipeline_options = PdfPipelineOptions(do_ocr=False)
                converter = DocumentConverter(
                    allowed_formats=[InputFormat.PDF],
                    format_options={
                        InputFormat.PDF: PdfFormatOption(
                            pipeline_options=pipeline_options
                        )
                    }
                )
            result = converter.convert(file_path)
            markdown = result.document.export_to_markdown()
        except Exception as exc:
            raise ParseError(f"Docling failed to parse document: {exc}") from exc

        sections = split_markdown_sections(markdown)
        if not sections:
            raise ParseError("Docling produced no parseable text sections")
        return sections
