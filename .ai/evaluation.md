# Evaluation

## Phase 2 Document Parsing And Chunking Evaluation

Status: implemented and locally verified for API/state/persistence/chunking with injected parser, real Docling `.docx` smoke, and real Docling text-based `.pdf` smoke.

Implemented:

1. `POST /api/documents/{document_id}/parse`.
2. `GET /api/documents/{document_id}`.
3. `GET /api/documents/{document_id}/chunks`.
4. Lazy `DoclingParserAdapter` for `.docx` and `.pdf`.
5. PDF parsing explicitly disables OCR with `PdfPipelineOptions(do_ocr=False)` to keep Phase 2 limited to text-based PDFs.
6. Additive SQLite tables: `document_sections` and `document_chunks`.
7. Parse status transitions: `pending`, `parsing`, `parsed`, `failed`.
8. Parse orchestration with old parse-output replacement on reparse and cleanup on failure.
9. Normalized section and chunk schemas.
10. Deterministic keyword tags with `deterministic_v1` metadata.
11. Pytest coverage for success parse, failed parse, unsupported parse type, status transition, chunk persistence, reparse replacement, pending chunks, not-found errors, and no RAG/LLM/vector dependency.
12. README Phase 2 local commands and docs updates for API/data model status.
13. Parser failure messages redact local paths before being returned or persisted.
14. Parse outputs and final `parsed` / `failed` status updates use atomic SQLite helpers.

Scope control:

- OCR / PaddleOCR: not implemented.
- Embeddings: not implemented.
- Qdrant/vector store: not implemented.
- Haystack retrieval pipeline: not implemented.
- LLM generation: not implemented.
- Full knowledge-card generation: not implemented.
- Deep tender analysis: not implemented.
- Frontend Demo: not implemented.
- User system: not implemented.
- Word/PDF export: not implemented.
- Reference repo vendoring: not done.

Verification summary:

- `ai-status`: passed, large mode confirmed.
- `ai-doctor`: passed with expected active-worktree warning.
- `compileall backend/app`: passed.
- `pip install -e '.[dev]'`: passed.
- Targeted Phase 2 pytest: `13 passed, 1 warning`.
- Full `python -m pytest backend/tests`: `50 passed, 1 warning`.
- Final full `python -m pytest backend/tests` after CR fixes: `51 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed and runs compile/test checks.
- Explicit `python -m pytest backend/tests`: passed, `50 passed, 1 warning`.
- `git diff --check`: passed with line-ending warnings only.
- uvicorn + `curl.exe --noproxy "*"` smoke: health/upload/parse/document/chunks API path verified with a real synthetic `.docx`; parse returned `parsed`, one section, and one chunk.
- uvicorn + `curl.exe --noproxy "*"` smoke: health/upload/parse/document/chunks API path verified with a generated text-layer `.pdf`; parse returned `parsed`, one section, and one chunk.
- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.
- CR subagent final review: no blocking findings and no remaining findings.

Residual risk:

1. The current pytest success path uses injected parser output for deterministic coverage; it intentionally avoids large samples and external parser runtime.
2. Third-party FastAPI/Starlette `httpx` deprecation warning remains from Phase 1.
3. Docling PDF parsing still initializes layout models and may download/cache model weights on first run; OCR remains disabled for Phase 2.

## Phase 1 Backend Foundation Evaluation

Status: implemented and locally verified, pending any required human diff/final gate decision.

Implemented:

1. FastAPI app entrypoint at `backend.app.main:app`.
2. `GET /health` returning exactly `{"status": "ok"}`.
3. `POST /api/files/upload` returning HTTP `201 Created` for valid uploads.
4. Fixed success fields: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`.
5. Fixed error response shape: `error_code`, `message`, `details`.
6. Configurable upload root and SQLite path through settings.
7. Backend-generated stored filenames based on server-generated document ids.
8. SQLite `documents` table with Phase 1 required fields.
9. Pytest coverage for health, upload contract, validation, storage, database, and Phase 1 boundaries.
10. Real PowerShell project check script.
11. README local setup, startup, test, and smoke commands.

Scope control:

- OCR: not implemented.
- LLM: not implemented.
- Embeddings: not implemented.
- Qdrant/vector store: not implemented.
- Haystack pipeline execution: not implemented.
- Knowledge cards: not implemented.
- Tender analysis: not implemented.
- Frontend Demo: not implemented.
- User system: not implemented.
- Word/PDF export: not implemented.

Verification summary:

- `ai-status`: large mode confirmed.
- `ai-doctor`: large-mode state valid; only active-worktree warning.
- `compileall backend/app`: passed.
- `pytest backend/tests`: `37 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed and runs real compile/test checks.
- `python -m pytest backend/tests`: passed after temporarily placing bundled Python on PATH.
- `curl.exe --noproxy "*"` health smoke: HTTP 200.
- `curl.exe --noproxy "*"` upload smoke: HTTP 201.
- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.

Residual risk:

1. Test run has a third-party deprecation warning from FastAPI/Starlette test client and `httpx`; no functional failure observed.
2. The repository still has many untracked files because it appears to be a newly initialized working tree.

## Phase 0 Evaluation

Status: verified.

Verified on 2026-06-27:

1. `F:\BidKonwledge` is a Git repository.
2. Auto_AICoding_Harness baseline files are present.
3. `docs/ai` contains the project brief, scope boundary, architecture, data model, API contract, dev rules, verification notes, and source-material notes.
4. `.ai` contains spec, implementation plan, verification, evaluation, and handoff files.
5. Backend and frontend directories contain only scaffold placeholders; no business code was implemented.

## Scope Control

Phase 0 should only initialize repository context and task planning. It must not implement backend business code.

## Review Questions

1. Do `docs/ai` files match the PRD boundary?
2. Does `.ai/implementation-plan.md` keep Phase 1 narrow?
3. Are OCR, LLM, embeddings, vector store, and demo page explicitly deferred?
4. Is the source material path recorded without copying large sample files into the repository?

Current answers: yes to all four.

## Harness Configuration Evaluation

Status: verified.

Verified on 2026-06-27:

1. `Auto_AICoding_Harness` upstream URL is `https://github.com/yu20120707/Auto_AICoding_Harness.git`.
2. Upstream `HEAD` and local source checkout both resolve to `b961e9171ebdfed7ec39491da821cbe0fbca8912`.
3. Current project is initialized by harness in `medium` mode with `python-backend-service` profile.
4. `.ai/state.json` exists and is schema-valid according to `ai-doctor`.
5. Python backend profile docs were generated under `docs/ai/`.

## Source Material Organization Evaluation

Status: verified.

1. Original PRD PDF and deep research report are stored under `docs/source-materials/originals/`.
2. Large sample files remain at `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`.
3. `docs/source-materials/sample-catalog.md` records recommended early samples and deferred large files.
4. `docs/ai/08-tech-selection.md` captures the technical route from the research report.
5. `docs/ai/09-phase-roadmap.md` separates Phase 1 from later Docling/Qdrant/Haystack/LLM work.

## Large-Mode Prep Evaluation

Status: verified.

Review criteria:

1. `.ai/state.json` reports `mode = large`.
2. `.ai/state.json` reports `profile = python-backend-service`.
3. `AGENTS.md` requires large mode and script execution for future development.
4. Phase 1 docs cover spec, local environment, API/persistence details, and verification.
5. No business code was implemented.

Current answers: yes to all five.

## Script Execution Evaluation

Status: partially verified for cross-shell scripts.

1. PowerShell project check script ran successfully.
2. Bash check script was attempted and failed because WSL is not installed.
3. Since this is a Windows-local repo and no backend code exists yet, the PowerShell check is the valid current script evidence.
4. Phase 1 must replace placeholder script output with real Python compile/test commands.

## Reference Reuse Evaluation

Status: verified.

1. Reference repositories were cloned outside the business repo.
2. RAGFlow is documented as product reference, not mainline fork.
3. Haystack demos are documented as engineering reference.
4. Target architecture is documented in `docs/ai/15-target-architecture.md`.
5. The direct二开 decision is documented in `docs/ai/14-reference-reuse-strategy.md`.

Decision: use our business repo as the mainline, with dependency-based reuse and reference-guided implementation. Direct RAGFlow customization remains a separate spike option, not the default path.

## Phase 1 Test-Case Documentation Evaluation

Status: contract-hardened, implementation pending.

1. `docs/ai/16-phase1-test-cases.md` now provides detailed P0/P1/P2 cases for health, upload success contract, structured error contract, file storage, SQLite persistence, atomicity, configuration, boundary checks, delivery command checks, and manual smoke.
2. `docs/ai/12-phase1-api-persistence.md` and `docs/ai/04-api-contract.md` now fix the upload success response as HTTP `201 Created`.
3. Error responses now use a stable JSON shape: `error_code`, `message`, and `details`.
4. The SQLite `documents` table fields are now fixed for Phase 1.
5. File safety rules now require backend-generated stored filenames and cleanup on validation or persistence failures.
6. Harness/script checks are documented as delivery checks, not core business pytest cases.
7. The test cases intentionally stay inside Phase 1 and do not require OCR, LLM, embeddings, Qdrant, Haystack, frontend Demo, export, or customer sample files.
8. Actual pytest code is not written yet because Phase 1 implementation has not started.

Decision: the next development session should implement backend code and tests together, using `docs/ai/16-phase1-test-cases.md` as the acceptance source.
