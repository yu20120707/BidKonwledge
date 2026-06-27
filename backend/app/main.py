from __future__ import annotations

from fastapi import FastAPI

from backend.app.api import files, health


def create_app() -> FastAPI:
    app = FastAPI(title="BidKnowledge Phase 1 Backend")
    app.include_router(health.router)
    app.include_router(files.router)
    return app


app = create_app()
