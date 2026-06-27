# Plan Review

## Status

WAITING_HUMAN_PLAN_APPROVAL

## Source

.ai/implementation-plan.md

## Plan Summary

```text
# Implementation Plan - Phase 1 Backend Foundation

## Execution Classification

- Harness mode: `large`
- Task level: Level 3 / complex
- Reason: this task introduces the backend app entrypoint, upload API contract, local file persistence, SQLite metadata persistence, project scripts, and P0 automated tests for a complete backend workflow.
- Rollback: normal Git revert before commit; no migrations beyond local SQLite initialization.

## Target Outcome

Implement the Phase 1 backend foundation only:

1. FastAPI app startup.
2. `GET /health`.
3. `POST /api/files/upload`.
4. HTTP `201 Created` upload success contract.
5. Structured upload error contract.
6. Configurable local upload root and SQLite database path.
7. Backend-generated stored filenames.
8. `documents` SQLite table matching `docs/ai/12-phase1-api-persistence.md`.
9. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md`.
10. README and `.ai` evidence updates.

## Non-Goals

Do not implement OCR, LLM calls, embedding, Qdrant/vector store, Haystack pipeline execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.

## Expected File Scope

Implementation files:

```text
backend/app/__init__.py
backend/app/main.py
backend/app/config.py
backend/app/api/__init__.py
backend/app/api/health.py
backend/app/api/files.py
backend/app/schemas/__init__.py
backend/app/schemas/document.py
backend/app/storage/__init__.py
backend/app/storage/database.py
backend/app/storage/file_storage.py
```

Test files:

```text
backend/tests/conftest.py
backend/tests/test_health.py
backend/tests/test_upload_contract.py
backend/tests/test_upload_validation.py
backend/tests/test_storage.py
backend/tests/test_database.py
backend/tests/test_phase1_boundaries.py
```

Project files:

```text
pyproject.toml
README.md
scripts/ai_check.ps1
scripts/ai_check.sh
.ai/affected-files.md
.ai/run-trace.md
.ai/verification.md
.ai/evaluation.md
.ai/handoff.md
```

## Subagent Plan

Use subagents for read-only and review work only. Main agent owns all writes to avoid conflicting edits.

1. Explorer Hooke: read-only API/persistence/test-contract scan.
2. Explorer Meitner: read-only script/README/verification-artifact scan.
3. After implementation, use reviewer/evaluator subagent only if useful for final contract review.

## Implementation Stages

### Stage 1 - Package And App Skeleton

1. Add a single dependency file, `pyproject.toml`, with FastAPI, Uvicorn, Pydantic, pytest, and HTTPX.
2. Add FastAPI app factory/import entrypoint in `backend/app/main.py`.
3. Add `GET /health` router.

Verification:

```powershell
python -m compileall backend/app
python -m pytest backend/tests/test_health.py
```

### Stage 2 - Configuration, SQLite, And File Storage

1. Add settings object with configurable upload root, database path, allowed extensions, and max upload size.
2. Add SQLite initialization and `documents` insert/query helpers.
3. Add file-storage helper that generates stored filenames using backend document ids and writes only under upload root.

Verification:

```powershell
python -m pytest backend/tests/test_storage.py backend/tests/test_database.py
```

### Stage 3 - Upload API And Error Contract

1. Add `POST /api/files/upload`.
2. Validate missing file, missing/invalid doc role, empty file, unsafe filename, unsupported extension, and file-too-large.
3. Save file before metadata insert.
4. Clean up stored file if metadata insert fails.
5. Return only documented success fields.
6. Return fixed error fields: `error_code`, `message`, `details`.

Verification:

```powershell
python -m pytest backend/tests/test_upload_contract.py backend/tests/test_upload_validation.py
```

### Stage 4 - Boundary Tests And Scripts

1. Add tests proving Phase 1 does not require OCR, LLM credentials, vector service, or parser output.
2. Replace PowerShell project check placeholder with real compile and pytest commands.
3. Replace bash project check placeholder with the same real check sequence for shell
...[truncated]
```

## Implementation Check

- [ ] Call chain is identified
- [ ] Affected files are listed
- [ ] Change scope is minimal
- [ ] Validation commands are defined
- [ ] Rollback or fallback is considered

## C++ / System Check

- [ ] Resource lifetime considered
- [ ] Error propagation considered
- [ ] Concurrency and locking considered
- [ ] API / ABI compatibility considered
- [ ] Performance impact considered

## Human Decision

- [ ] Approved
- [ ] Needs replan
- [ ] Rejected

## Human Notes
