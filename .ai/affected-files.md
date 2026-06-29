# Affected Files - Phase 12 Semantic Retrieval Adapter Spike

## Added Files

Docs:

- `docs/ai/39-phase12-semantic-retrieval-spike-dev-spec.md`
- `docs/ai/40-phase12-test-cases.md`
- `docs/ai/41-phase12-evaluation-report.md`

## Updated Files

- `docs/ai/README.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/41-phase12-evaluation-report.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`
- `backend/app/storage/database.py`
- `backend/app/services/prompt_builder.py`
- `backend/app/services/retrieval.py`
- `backend/app/static/demo.html`
- `backend/tests/test_retrieval_api.py`
- `backend/tests/test_generation_api.py`
- `backend/tests/test_demo_page.py`
- `backend/tests/test_phase5_demo_workflow.py`

## Intentionally Untouched In Current Slice

- `backend/app/api/retrieval.py`
- `backend/app/schemas/document.py`
- `pyproject.toml`
- database schema
- public API contracts
- normal test dependency setup

## Forbidden Areas Unless Explicitly Approved Later

- replacing deterministic retrieval default
- mandatory Qdrant/Haystack/embedding dependencies
- generated runtime data under `data/`
- customer source files
- local model caches
- Qdrant local storage
- PyMuPDF project dependency
- final document export
