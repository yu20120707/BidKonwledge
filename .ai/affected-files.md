# Affected Files - Phase 10 PRD Demo Flow

## Updated Files

Implementation and tests:

- `backend/app/static/demo.html`
- `backend/tests/test_demo_page.py`
- `backend/tests/test_phase5_boundaries.py`
- `backend/tests/test_phase5_demo_workflow.py`

Durable docs:

- `docs/ai/09-phase-roadmap.md`
- `docs/ai/README.md`
- `docs/ai/33-phase10-prd-demo-flow-dev-spec.md`
- `docs/ai/34-phase10-test-cases.md`
- `docs/ai/35-phase10-demo-runbook.md`

Runtime evidence:

- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

## Scope Boundary

Do not touch unless the current page cannot work without it:

- FastAPI route wiring
- backend API contracts
- database schema
- dependency declarations

## Forbidden Areas

- Qdrant, Haystack, embeddings, semantic retrieval
- table reconstruction
- image batch ingestion
- qualification/certificate validation
- login/user system
- final Word/PDF export
- adding PyMuPDF to project dependencies
