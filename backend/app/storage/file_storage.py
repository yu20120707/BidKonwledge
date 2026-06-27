from __future__ import annotations

from pathlib import Path, PurePosixPath, PureWindowsPath

from backend.app.config import Settings


def normalized_extension(filename: str) -> str:
    return Path(filename).suffix.lower()


def is_unsafe_filename(filename: str) -> bool:
    if not filename or filename in {".", ".."}:
        return True
    posix_parts = PurePosixPath(filename).parts
    windows_parts = PureWindowsPath(filename).parts
    if len(posix_parts) > 1 or len(windows_parts) > 1:
        return True
    return ".." in posix_parts or ".." in windows_parts


def stored_filename(document_id: str, file_ext: str) -> str:
    return f"{document_id}{file_ext}"


def resolve_upload_path(settings: Settings, filename: str) -> Path:
    upload_root = settings.upload_root.resolve()
    target = (upload_root / filename).resolve()
    if upload_root != target and upload_root not in target.parents:
        raise ValueError("stored path escapes upload root")
    return target


def write_uploaded_bytes(settings: Settings, filename: str, content: bytes) -> Path:
    target = resolve_upload_path(settings, filename)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    return target


def relative_stored_path(settings: Settings, path: Path) -> str:
    return path.resolve().relative_to(settings.upload_root.resolve()).as_posix()
