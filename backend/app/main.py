from __future__ import annotations

from fastapi import FastAPI

from backend.app.api import demo, documents, files, generation, health, retrieval


def create_app() -> FastAPI:
    app = FastAPI(title="BidKnowledge Backend")
    app.include_router(health.router)
    app.include_router(files.router)
    app.include_router(documents.router)
    app.include_router(retrieval.router)
    app.include_router(generation.router)
    app.include_router(demo.router)
    return app


app = create_app()
