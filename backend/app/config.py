from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


DEFAULT_MAX_UPLOAD_BYTES = 10 * 1024 * 1024
DEFAULT_ALLOWED_EXTENSIONS = (".txt", ".pdf", ".doc", ".docx")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    upload_root: Path
    database_path: Path
    max_upload_bytes: int = DEFAULT_MAX_UPLOAD_BYTES
    allowed_extensions: tuple[str, ...] = DEFAULT_ALLOWED_EXTENSIONS

    @classmethod
    def from_env(cls) -> "Settings":
        root = _repo_root()
        upload_root = Path(
            os.getenv("BIDKNOWLEDGE_UPLOAD_ROOT", str(root / "data" / "uploads"))
        )
        database_path = Path(
            os.getenv("BIDKNOWLEDGE_DB_PATH", str(root / "data" / "app.sqlite3"))
        )
        max_upload_bytes = int(
            os.getenv("BIDKNOWLEDGE_MAX_UPLOAD_BYTES", str(DEFAULT_MAX_UPLOAD_BYTES))
        )
        return cls(
            upload_root=upload_root,
            database_path=database_path,
            max_upload_bytes=max_upload_bytes,
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings.from_env()
