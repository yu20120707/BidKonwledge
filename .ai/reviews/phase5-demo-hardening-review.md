# Phase 5 Demo Hardening Review

Date: 2026-06-28

## Scope

Multi-subagent review of the Phase 5 demo page, workflow tests, and harness
documentation evidence.

Harness state remains:

- mode: `large`
- status: `DONE`
- current_gate: none

No new harness gate transition is claimed.

## Subagents

### Bohr - Code And Security Review

Skills:

- `code-review-and-quality`
- `security-review`

Result:

- No blocking findings.
- XSS/output handling is acceptable because the demo uses `textContent` rather
  than `innerHTML`.
- Static file serving is path-safe because `/demo` returns a fixed local asset.
- P2 finding: when `/api/generate` returns `LLM_NOT_CONFIGURED`, the page showed
  raw JSON but did not update the human-review or risks panels.

Action taken:

- Added `renderGenerationError`.
- `LLM_NOT_CONFIGURED` now sets `need_human_review: true` and displays a high
  risk item in the risks panel.
- Added static test coverage for the no-LLM UI handling hook.

### Aristotle - Workflow And Test Review

Skills:

- `verification-before-completion`
- `systematic-debugging`
- `karpathy-guidelines`

Result:

- Current minimal coverage was acceptable for Phase 5.
- Recommended hardening: persist the upload -> parse -> retrieve -> generate
  fake-parser/fake-LLM chain as an automated test.
- Recommended future hardening: browser or JavaScript-level rendering test.

Action taken:

- Added `backend/tests/test_phase5_demo_workflow.py`.
- The new test verifies upload, parse, retrieve, generate, citations, empty
  risks, and `need_human_review = true` using fake parser and fake LLM.
- The first version used a long Chinese generation query and exposed the Phase 3
  deterministic retrieval limitation. The test was narrowed to query `应急`,
  which matches the current lexical retrieval contract.

### Bernoulli - Harness Documentation Review

Skills:

- `task-router`
- `verification-before-completion`

Result:

- Packet prompts were present and correctly shaped.
- Required that subagent completion results be written to a durable review
  artifact and referenced from `.ai/run-trace.md`.
- Required `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` to
  record this review round and state caveats.

Action taken:

- Added this review artifact.
- Updated task evidence files to record subagent dispatch, results, fixes, and
  remaining verification gaps.

## Verification Evidence

Fresh checks run during the hardening round:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py

$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests

.\scripts\ai_check.ps1
```

Observed before fixes:

- Targeted Phase 5 tests: `4 passed, 1 warning`.
- Full backend tests: `68 passed, 1 warning`.
- PowerShell project check: passed.

After fixes:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py backend/tests/test_phase5_demo_workflow.py backend/tests/test_generation_api.py
```

Observed:

- Targeted hardening tests: `11 passed, 1 warning`.

Full final verification is recorded in `.ai/verification.md`.

## Residual Risks

- Browser JavaScript execution is still covered by static hook tests and live
  HTTP smoke, not a real browser automation test.
- Real external LLM provider integration remains optional and unverified.
- `bash ./scripts/ai_check.sh` remains unverified on this Windows machine
  because no usable WSL/Linux distribution is available.
- Phase 3 deterministic retrieval is lexical. Long Chinese sentence queries may
  not retrieve context unless they contain whitespace-separated terms or exact
  substrings matching the current implementation.
