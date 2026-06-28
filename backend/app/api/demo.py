from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/demo", include_in_schema=False)
def demo_page() -> FileResponse:
    demo_html = Path(__file__).resolve().parents[1] / "static" / "demo.html"
    return FileResponse(demo_html, media_type="text/html")
