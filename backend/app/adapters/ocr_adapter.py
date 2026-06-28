from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


class OCRError(RuntimeError):
    """Raised when OCR cannot extract usable text."""


@dataclass(frozen=True)
class OCRPageText:
    page_number: int
    text: str
    confidence: float | None = None
    engine: str = "unknown"
    blocks: list[dict[str, object]] = field(default_factory=list)
    metadata: dict[str, object] = field(default_factory=dict)


class OCRAdapter(Protocol):
    def extract(self, file_path: Path) -> list[OCRPageText]:
        """Extract page text from a local document through OCR."""


class PaddleOCRAdapter:
    engine = "paddleocr"

    def extract(self, file_path: Path) -> list[OCRPageText]:
        try:
            from paddleocr import PaddleOCR  # type: ignore[import-not-found]
        except ImportError as exc:
            raise OCRError(
                "PaddleOCR is not installed. Install the OCR optional dependency "
                "before running real OCR parsing."
            ) from exc

        try:
            ocr = PaddleOCR(use_angle_cls=True, lang="ch")
            result = ocr.ocr(str(file_path), cls=True)
        except Exception as exc:
            raise OCRError(f"PaddleOCR failed to extract text: {exc}") from exc

        pages: list[OCRPageText] = []
        for page_index, page_result in enumerate(result or [], start=1):
            lines: list[str] = []
            confidences: list[float] = []
            blocks: list[dict[str, object]] = []
            for item in page_result or []:
                if len(item) < 2:
                    continue
                box = item[0]
                text_info = item[1]
                if not text_info:
                    continue
                text = str(text_info[0]).strip()
                if not text:
                    continue
                confidence = float(text_info[1]) if len(text_info) > 1 else None
                lines.append(text)
                if confidence is not None:
                    confidences.append(confidence)
                blocks.append({"text": text, "box": box, "confidence": confidence})
            page_text = "\n".join(lines).strip()
            if page_text:
                pages.append(
                    OCRPageText(
                        page_number=page_index,
                        text=page_text,
                        confidence=(
                            sum(confidences) / len(confidences)
                            if confidences
                            else None
                        ),
                        engine=self.engine,
                        blocks=blocks,
                    )
                )

        if not pages:
            raise OCRError("PaddleOCR produced no parseable text")
        return pages
