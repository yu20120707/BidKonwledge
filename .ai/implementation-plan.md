# Implementation Plan - Phase 5 Demo Page And Script

## Execution Classification

- Harness mode: `large`
- Task level: Level 3 / complex
- Reason: Phase 5 exposes the full backend chain through a stakeholder-facing
  demo surface and must avoid expanding into production frontend, OCR, export,
  or user-system work.
- Rollback: normal Git revert before commit; no database migration is expected.

Phase 5 implementation has completed against this plan. The harness state still
remains the prior `DONE/current_gate: none` state, so no Phase 5 gate transition
is claimed.

## Target Outcome

Implement Phase 5 demo only:

1. Minimal FastAPI-hosted demo page.
2. Demo interactions for upload, parse, retrieve, and generate.
3. Raw JSON result display.
4. Citation, risk, and human-review status visibility.
5. Demo runbook/script for a small representative workflow.
6. Pytest coverage for demo route and boundary rules.
7. README and `.ai` evidence updates.

## Non-Goals

No OCR, Qdrant, Haystack, embeddings, production authentication, user
management, Word/PDF export, polished frontend product shell, or final approved
bidding output.

## Subagent Plan

No subagent is planned at task start.

Reason: the expected implementation is a small, coupled demo route/page plus
tests. If UI review becomes non-trivial, a read-only reviewer can be added, but
the first pass should stay serial.

## Implementation Stages

### Stage 1 - Demo Route And Static Asset

1. Add a demo route such as `GET /demo`.
2. Serve a minimal static HTML page.
3. Keep layout functional and focused on the existing API chain.

Verification:

```powershell
python -m pytest backend/tests/test_demo_page.py
```

### Stage 2 - Demo Workflow Controls

1. Add upload, parse, retrieve, and generate controls.
2. Display raw JSON responses.
3. Surface citations, risks, and `need_human_review` clearly.

Verification:

```powershell
python -m pytest backend/tests/test_demo_page.py
```

### Stage 3 - Boundaries And Documentation

1. Add tests proving Phase 5 does not require OCR/Qdrant/Haystack/export/user
   system.
2. Update README with demo startup and smoke commands.
3. Update `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.

Verification:

```powershell
python -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py
```

### Stage 4 - Required Checks And Smoke

1. Run harness status checks.
2. Run project scripts and full pytest.
3. Run uvicorn + `curl.exe --noproxy "*"` smoke for `GET /demo`.
4. Attempt bash check if shell tooling is available, otherwise record the
   Windows/WSL blocker.

Verification:

```powershell
python -m pytest backend/tests
.\scripts\ai_check.ps1
```

## Mid-Task Review Checkpoint

After Stage 2, perform a self-review:

1. Status versus this plan.
2. Scope changes since start.
3. Newly discovered risks.
4. Decision: keep plan, revise plan, or escalate.

Checkpoint result:

- Stage 1 and Stage 2 completed with targeted tests passing.
- Scope did not expand beyond the demo route/page/tests/docs surface.
- No OCR, Qdrant, Haystack, embeddings, export, user system, or production
  frontend work was added.
- Decision: keep the original plan.

## Escalation Triggers

Pause or escalate if:

1. The demo starts requiring OCR, Qdrant, Haystack, embeddings, export, or user
   accounts.
2. The frontend grows beyond a minimal stakeholder demo surface.
3. Real external LLM configuration becomes mandatory for automated tests.
4. Generated content could be presented as final approved bidding content.
5. Verification requires real large customer sample files instead of small
   representative samples or fake-test paths.
