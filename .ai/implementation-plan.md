# Implementation Plan - Phase 10 PRD Demo Flow

## Execution Classification

- Harness mode: `large`
- Task level: Level 2 / medium
- Reason: one bounded demo workflow across static page, targeted tests, and
  task evidence files
- Escalation trigger: route/API/schema changes become necessary

## Target Outcome

A stakeholder can walk the PRD story on one static page without pretending the
backend already supports new PRD retrieval contracts or production OCR.

## Plan

1. Confirm current `/demo` baseline and active repo/harness state.
2. Rebuild `demo.html` into a PRD-shaped narrative page.
3. Keep PRD labels on the page, but map them to current deterministic retrieval
   tags at the page layer.
4. Update targeted demo tests to cover new sections, hooks, OCR boundary copy,
   and the API chain.
5. Run a Level 2 mid-task self-review.
6. Add Phase 10 durable docs and update `.ai` runtime artifacts.
7. Run required verification and record any blocker honestly.

## Mid-Task Review

Status versus original plan:

- `demo.html` has been restructured into the intended PRD flow.
- No route, schema, database, or dependency changes were required.
- One targeted workflow test failed due to parser dependency override lifetime,
  not due to business logic; fixed by sharing one fake parser instance.

Decision: keep plan. The task remains Level 2.

## Verification Plan

Required:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
.\scripts\ai_check.ps1
git diff --check
```

Also attempt:

```powershell
bash ./scripts/ai_check.sh
```

If WSL/Linux distro is unavailable, record the blocker and do not claim bash
verification passed.
