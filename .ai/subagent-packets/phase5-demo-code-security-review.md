# Phase 5 Demo Code And Security Review Packet

## Role

Read-only reviewer for Phase 5 demo code correctness and security.

## Assigned Agent

- nickname: Bohr
- agent id: `019f0d48-080d-70a1-9040-3e1526b98920`

## Required Skills

- `code-review-and-quality`
- `security-review`

## Required Context

- `AGENTS.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `README.md`
- `docs/ai/04-api-contract.md`
- `backend/app/api/demo.py`
- `backend/app/static/demo.html`
- `backend/app/main.py`
- `backend/tests/test_demo_page.py`
- `backend/tests/test_phase5_boundaries.py`

## Objective

Review the Phase 5 demo implementation for correctness, regressions, static
file path safety, browser output handling, API hook correctness, scope drift,
and missing tests.

## Forbidden Actions

- Do not edit files.
- Do not run destructive commands.
- Do not approve harness gates.
- Do not expand Phase 5 into OCR, Qdrant, Haystack, embeddings, user system, or
  export work.

## Expected Output

Findings ordered by severity with file and line references, verification gaps,
scope drift, open questions, blockers, and residual risks.

## Return Format

```text
role: code-security-reviewer
status: complete | blocked
findings:
verification_gaps:
scope_drift:
open_questions:
blockers:
residual_risks:
```
