# Spec - Phase 5 Demo Page And Script

## Objective

Prepare the final MVP demo layer that presents the completed backend chain to a
stakeholder.

Phase 5 should expose a minimal demo page and a repeatable demo script over the
existing upload, parse, retrieve, and generate APIs. It should make the raw JSON,
citations, risks, and `need_human_review = true` visible.

This file is a pre-development spec. Phase 5 code has not been implemented yet.

## Required Execution Mode

This task must run under Auto_AICoding_Harness `large` mode with the
`python-backend-service` profile.

Current baseline:

- Phase 1 upload and SQLite metadata are implemented.
- Phase 2 parsing/chunking is implemented for small `.docx` and text-based
  `.pdf`; OCR/scanned PDFs remain out of scope.
- Phase 3 local deterministic retrieval is implemented through
  `POST /api/retrieve`.
- Phase 4 candidate generation is implemented through `POST /api/generate`.
- Current harness state remains the previous completed task state:
  `current_gate: none`. Do not claim a Phase 5 gate transition unless a harness
  command succeeds.

## In Scope For Phase 5

Implement only:

1. Minimal FastAPI-hosted demo page.
2. Demo page controls for upload, parse, retrieve, and generate.
3. Raw JSON display for API responses.
4. Visible citations, risks, and `need_human_review` status.
5. Demo script or runbook using selected small sample files.
6. Tests for demo route availability and non-regression of existing APIs.
7. README Phase 5 demo commands.
8. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.

## Out Of Scope For Phase 5

Do not implement:

1. OCR or PaddleOCR.
2. Qdrant, Haystack, embeddings, dense retrieval, or hybrid retrieval.
3. Production authentication or user management.
4. Word or PDF export.
5. Full tender deep analysis workflow.
6. Polished product frontend or multi-page application.
7. Treating generated content as final approved bidding text.
8. Vendoring `F:\BidKonwledge_refs` repositories.

## Expected File Scope For Phase 5

Implementation files:

```text
backend/app/main.py
backend/app/api/demo.py
backend/app/static/demo.html
```

Test files:

```text
backend/tests/test_demo_page.py
backend/tests/test_phase5_boundaries.py
```

Documentation and evidence files:

```text
README.md
docs/ai/09-phase-roadmap.md
.ai/spec.md
.ai/implementation-plan.md
.ai/affected-files.md
.ai/run-trace.md
.ai/verification.md
.ai/evaluation.md
.ai/handoff.md
```

## Acceptance Criteria For Phase 5

Phase 5 is accepted when:

1. A user can open a local demo page from the running FastAPI app.
2. The page can drive the existing upload, parse, retrieve, and generate APIs.
3. Raw JSON responses are visible.
4. Citations, risks, and `need_human_review = true` are visible.
5. The demo does not require OCR, Qdrant, Haystack, embeddings, export, or a
   production user system.
6. Automated tests cover route availability and boundary constraints.
7. README and `.ai` files record real command evidence and residual risks.

## Required Verification Commands

Run before Phase 5 completion:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
.\scripts\ai_check.ps1
python -m pytest backend/tests
```

Run local uvicorn plus `curl.exe --noproxy "*"` smoke for the demo route. Use a
real browser screenshot only if the demo page layout becomes non-trivial.

Run `bash ./scripts/ai_check.sh` if shell tooling is available. If WSL/bash is
unavailable, record the blocker and do not claim it passed.
