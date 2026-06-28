# Phase 5 Demo Workflow And Test Review Packet

## Role

Read-only workflow and robustness test reviewer for the Phase 5 demo.

## Assigned Agent

- nickname: Aristotle
- agent id: `019f0d48-3fbb-7011-b98b-d7e6fdc34560`

## Required Skills

- `verification-before-completion`
- `systematic-debugging`

## Required Context

- `AGENTS.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/verification.md`
- `README.md`
- `backend/tests/conftest.py`
- `backend/tests/test_demo_page.py`
- `backend/tests/test_phase5_boundaries.py`
- `backend/tests/test_generation_api.py`
- `backend/app/static/demo.html`

## Objective

Audit whether the tests and smoke checks adequately cover the demo workflow:
upload, parse, retrieve, generate, raw JSON display, citations, risks,
`need_human_review`, expected error paths, and Phase 5 boundary constraints.

## Forbidden Actions

- Do not edit files.
- Do not run destructive commands.
- Do not require real LLM credentials for automated tests.
- Do not require OCR, Qdrant, Haystack, embeddings, export, or user accounts.

## Expected Output

Concrete proposed tests or verification commands with priority and evidence.
If current coverage is enough for Phase 5 minimal scope, explain why.

## Return Format

```text
role: workflow-test-reviewer
status: complete | blocked
findings:
proposed_tests:
verification_commands:
verification_gaps:
blockers:
residual_risks:
```
