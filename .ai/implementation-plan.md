# Implementation Plan - Phase 2 Document Parsing And Chunking

## Execution Classification

- Harness mode: `large`
- Task level: Level 3 / complex
- Reason: this task changes backend API surface, SQLite persistence, document
  parse-status semantics, and cross-module parser/chunker behavior.
- Rollback: normal Git revert before commit; SQLite schema changes are additive
  and local to MVP metadata.

## Target Outcome

Implement Phase 2 backend parsing only:

1. Lazy Docling adapter for `.docx` and text-based `.pdf`.
2. Document parse orchestration service.
3. Normalized section/chunk persistence.
4. Deterministic minimal tags.
5. Minimal document parse/read/chunk APIs.
6. Pytest coverage using temp upload roots and SQLite DBs.
7. README and `.ai` evidence updates.

## Non-Goals

No OCR, embeddings, vector store, Haystack pipeline, LLM generation, full
knowledge cards, tender deep analysis, frontend, user system, or export.

## Subagent Plan

No subagent is used at task start.

Reason: the write scope is one coupled backend data flow where API, parser,
database, and tests must evolve together. The main agent owns all writes and
will perform a mid-task self-review checkpoint after the API/service/test path
is implemented.

## Implementation Stages

### Stage 1 - Persistence And Schemas

1. Add additive SQLite tables for `document_sections` and `document_chunks`.
2. Add document status update helpers and section/chunk query helpers.
3. Add Pydantic response/schema models for document detail, parse response, and
   chunks.

Verification:

```powershell
python -m pytest backend/tests/test_database.py
```

### Stage 2 - Parser Adapter, Chunker, Tagger

1. Add `DoclingParserAdapter` behind `backend/app/adapters`.
2. Normalize Docling markdown/text output into parser sections.
3. Add deterministic section/chunk splitting.
4. Add minimal keyword-based tag rules.

Verification:

```powershell
python -m pytest backend/tests/test_document_chunks.py
```

### Stage 3 - Document APIs

1. Add `POST /api/documents/{document_id}/parse`.
2. Add `GET /api/documents/{document_id}`.
3. Add `GET /api/documents/{document_id}/chunks`.
4. Wire router into `backend/app/main.py`.

Verification:

```powershell
python -m pytest backend/tests/test_document_parse_api.py
```

### Stage 4 - Boundaries And Documentation

1. Add tests proving Phase 2 does not require RAG/LLM/vector dependencies.
2. Update README with Phase 2 local usage and parse commands.
3. Update `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.
4. Update durable docs only where current Phase 2 API/status semantics would
   otherwise be stale.

Verification:

```powershell
python -m pytest backend/tests
.\scripts\ai_check.ps1
```

### Stage 5 - Required Checks And Smoke

1. Run harness status checks.
2. Run project scripts and pytest.
3. Attempt local uvicorn + curl smoke for upload, parse, document read, and
   chunks when dependencies are usable.
4. Attempt bash check if shell tooling is available, otherwise record the
   Windows/WSL blocker.

## Mid-Task Review Checkpoint

After Stage 3, perform a self-review:

1. Status versus this plan.
2. Scope changes since start.
3. Newly discovered risks.
4. Decision: keep plan, revise plan, or escalate.

## Escalation Triggers

Pause or escalate if:

1. Docling cannot install or import and the requested real parser support cannot
   be demonstrated.
2. Parser behavior requires OCR, LLM, vector services, or large samples.
3. SQLite schema changes become non-additive or risky to roll back.
4. Tests would need real `data/uploads` or customer sample folders.
5. API semantics conflict with the user's Phase 2 status contract.
