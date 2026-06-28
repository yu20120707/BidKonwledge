# Spec - Phase 2 Document Parsing And Chunking

## Objective

Implement the smallest backend-only Phase 2 capability for parsing already-uploaded
documents into normalized sections and chunks.

Phase 2 proves that the service can trigger parsing for uploaded `.docx` and
text-based `.pdf` files, persist parser output in SQLite, and expose the parsed
document/chunk state through minimal APIs.

## Required Execution Mode

This task must run under Auto_AICoding_Harness `large` mode with the
`python-backend-service` profile.

Initial evidence:

- `ai-status`: passed, `mode: large`, `status: DONE`.
- `ai-doctor`: passed, working tree clean before Phase 2 edits.

## In Scope

Implement only:

1. Docling adapter, imported lazily through a backend adapter boundary.
2. Parsing for already-uploaded `.docx` and text-based `.pdf` documents.
3. Normalized section and chunk schemas.
4. SQLite persistence for sections and chunks.
5. Minimal deterministic tag rules.
6. Parse status transitions:
   - `pending`
   - `parsing`
   - `parsed`
   - `failed`
7. Minimal APIs:
   - `POST /api/documents/{document_id}/parse`
   - `GET /api/documents/{document_id}`
   - `GET /api/documents/{document_id}/chunks`
8. Pytest coverage for successful parsing, failed parsing, status transitions,
   chunk persistence, and no RAG/LLM dependency.
9. README local startup, parse testing, and Phase 2 command updates.
10. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.

## Out Of Scope

Do not implement:

1. OCR or PaddleOCR.
2. Embeddings.
3. Vector store or Qdrant.
4. Haystack retrieval pipeline.
5. LLM generation.
6. Full knowledge-card generation.
7. Deep tender analysis.
8. Frontend Demo.
9. User system.
10. Word or PDF export.
11. Vendoring reference repositories.

## Expected File Scope

Implementation files:

```text
pyproject.toml
backend/app/main.py
backend/app/api/documents.py
backend/app/adapters/docling_parser.py
backend/app/schemas/document.py
backend/app/services/document_parsing.py
backend/app/services/section_chunker.py
backend/app/services/tagger.py
backend/app/storage/database.py
```

Test files:

```text
backend/tests/conftest.py
backend/tests/test_document_parse_api.py
backend/tests/test_document_chunks.py
backend/tests/test_phase2_boundaries.py
```

Documentation and evidence files:

```text
README.md
docs/ai/03-data-model.md
docs/ai/04-api-contract.md
.ai/affected-files.md
.ai/run-trace.md
.ai/verification.md
.ai/evaluation.md
.ai/handoff.md
```

## Reference Repository Rule

Reference repositories under `F:\BidKonwledge_refs` remain reference-only.
Do not copy or vendor RAGFlow or Haystack demo source into this repository.

## Acceptance Criteria

Phase 2 is accepted when:

1. Uploaded `.docx` and text-based `.pdf` records can be parsed through the
   parsing service when Docling is available.
2. Unsupported parse inputs fail with `parse_status = failed` and an
   `error_message`.
3. Status transitions are persisted as `pending -> parsing -> parsed` on success
   and `pending -> parsing -> failed` on failure.
4. Sections and chunks are persisted in SQLite with deterministic ordering.
5. Chunks include normalized fields and deterministic tags.
6. `GET /api/documents/{document_id}` returns document metadata and parse status.
7. `GET /api/documents/{document_id}/chunks` returns persisted chunks without
   invoking RAG, LLM, embeddings, vector stores, or external services.
8. Automated tests use temporary upload roots and SQLite databases.
9. README and `.ai` files record real command evidence and residual risks.

## Required Verification Commands

Run before completion:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
.\scripts\ai_check.ps1
python -m pytest backend/tests
```

Run local uvicorn plus `curl.exe --noproxy "*"` smoke if the app and parser
dependencies are available.

Run `bash ./scripts/ai_check.sh` if shell tooling is available. If WSL/bash is
unavailable, record the blocker and do not claim it passed.
