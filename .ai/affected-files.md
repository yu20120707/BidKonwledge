# Affected Files - Phase 1 Backend Foundation

## Expected Added Files

- `pyproject.toml`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/config.py`
- `backend/app/api/__init__.py`
- `backend/app/api/health.py`
- `backend/app/api/files.py`
- `backend/app/schemas/__init__.py`
- `backend/app/schemas/document.py`
- `backend/app/storage/__init__.py`
- `backend/app/storage/database.py`
- `backend/app/storage/file_storage.py`
- `backend/tests/conftest.py`
- `backend/tests/test_health.py`
- `backend/tests/test_upload_contract.py`
- `backend/tests/test_upload_validation.py`
- `backend/tests/test_storage.py`
- `backend/tests/test_database.py`
- `backend/tests/test_phase1_boundaries.py`

## Expected Updated Files

- `README.md`
- `scripts/ai_check.ps1`
- `scripts/ai_check.sh`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`
- `.ai/state.json`
- `.ai/reviews/spec-review.md`
- `.ai/approvals/spec-approval.md`
- large-mode generated files under `docs/ai/tasks/init-large/`

## Forbidden Areas

- Do not vendor `F:\BidKonwledge_refs\ragflow`.
- Do not vendor `F:\BidKonwledge_refs\haystack-demos`.
- Do not copy large customer sample files into the repository.
- Do not implement OCR, LLM, embeddings, vector store, Haystack execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.
