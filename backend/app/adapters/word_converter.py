from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


class WordConversionError(RuntimeError):
    """Raised when a legacy Word document cannot be converted to DOCX."""


@dataclass(frozen=True)
class WordConversionResult:
    converted_path: Path
    method: str


class WordConverter(Protocol):
    def convert_to_docx(self, source_path: Path, target_path: Path) -> WordConversionResult:
        """Convert a local legacy Word file into a true DOCX file."""


class WindowsWordComConverter:
    method = "word_com"

    def convert_to_docx(self, source_path: Path, target_path: Path) -> WordConversionResult:
        try:
            import win32com.client  # type: ignore[import-not-found]
        except ImportError as exc:
            raise WordConversionError(
                "Windows Word COM converter is unavailable. Install pywin32 and "
                "Microsoft Word to convert legacy Word documents locally."
            ) from exc

        target = target_path.resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        source = _word_open_path(source_path.resolve(), target)

        word = None
        document = None
        try:
            word = win32com.client.DispatchEx("Word.Application")
            word.Visible = False
            word.DisplayAlerts = 0
            document = word.Documents.Open(str(source), ReadOnly=True)
            document.SaveAs2(str(target), FileFormat=16)
        except Exception as exc:
            raise WordConversionError(f"Word COM conversion failed: {exc}") from exc
        finally:
            if document is not None:
                try:
                    document.Close(False)
                except Exception:
                    pass
            if word is not None:
                try:
                    word.Quit()
                except Exception:
                    pass

        if not target.exists():
            raise WordConversionError("Word COM conversion did not create DOCX output")
        return WordConversionResult(converted_path=target, method=self.method)


def _word_open_path(source_path: Path, target_path: Path) -> Path:
    if source_path.suffix.lower() == ".doc":
        return source_path
    legacy_copy = target_path.with_name(f"{target_path.stem}.source.doc")
    legacy_copy.write_bytes(source_path.read_bytes())
    return legacy_copy
