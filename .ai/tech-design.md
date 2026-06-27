# Tech Design

## Current Task Design

This task is documentation and workflow configuration only.

The design is to keep the repository as a generated target project for Auto_AICoding_Harness:

- `docs/ai/` stores durable product and engineering context.
- `.ai/` stores current large-mode task runtime artifacts.
- `docs/source-materials/` stores source document copies and sample indexes.
- `backend/` and `frontend/` remain placeholders until Phase 1 implementation begins.

## Phase 1 Design Boundary

Phase 1 will later implement:

- FastAPI app startup.
- `GET /health`.
- `POST /api/files/upload`.
- local file storage.
- SQLite document metadata.
- smoke tests.

Phase 1 will not implement parsing, retrieval, generation, OCR, vector storage, or UI.

## Interface Decisions For Future Implementation

1. Upload status starts as `parse_status = pending`.
2. SQLite table `documents` stores metadata only.
3. Uploaded files are saved under configurable `data/uploads`.
4. User-provided filenames are preserved as metadata but must not be trusted as storage paths.
5. Tests and scripts must be run before completion.
