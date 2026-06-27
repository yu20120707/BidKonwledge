# Phase 1 Development Spec

## Objective

Build the smallest runnable backend foundation for the 投标智能知识库能力验证版 Demo.

Phase 1 proves that the service can start, accept an uploaded file, save it locally, and persist document metadata. It does not parse document content.

Phase 1 is a backend foundation milestone. It is not the customer-facing Demo and does not prove the knowledge-base capability by itself.

## Required Harness Mode

All Phase 1 development must run under Auto_AICoding_Harness `large` mode.

Before implementation:

1. Run `ai-status` or `ai-doctor`.
2. Confirm `.ai/state.json` reports `"mode": "large"`.
3. Keep `.ai/implementation-plan.md`, `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` current.

## In Scope

Implement only:

1. FastAPI application startup.
2. `GET /health`.
3. `POST /api/files/upload`.
4. Local file saving under `data/uploads`.
5. Document metadata schema.
6. SQLite initialization.
7. Basic configuration management.
8. Minimal smoke tests.
9. README local startup and test commands.

## Out Of Scope

Do not implement:

1. OCR.
2. LLM calls.
3. Embeddings.
4. Vector store.
5. Knowledge card generation.
6. Tender analysis.
7. Demo page.
8. User login or permission system.
9. Word/PDF export.
10. Production deployment.

## Recommended File Scope

Phase 1 may add or edit:

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   └── files.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── document.py
│   └── storage/
│       ├── __init__.py
│       ├── database.py
│       └── file_storage.py
├── tests/
│   ├── test_health.py
│   └── test_upload.py
└── pyproject.toml or requirements.txt
```

Repository-level files that may be updated:

- `README.md`
- `.gitignore`
- `scripts/ai_build.sh`
- `scripts/ai_test.sh`
- `scripts/ai_check.sh`
- `scripts/ai_check.ps1`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

## Completion Definition

Phase 1 is complete only when:

1. The app can be imported.
2. `GET /health` returns `{"status": "ok"}`.
3. `POST /api/files/upload` returns `201 Created` for valid uploads.
4. Uploading a small file saves it under configured upload root using a backend-generated stored filename.
5. Uploading a file creates a SQLite metadata row following `docs/ai/12-phase1-api-persistence.md`.
6. Invalid uploads return the documented structured error JSON.
7. Invalid uploads do not leave orphan files or metadata rows.
8. Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
9. Project scripts were run and results were recorded.
10. Deferred RAG/OCR/LLM functionality remains unimplemented.
