# Run Trace

Keep a short execution log for large-mode work.

## Phase 10 - PRD-shaped Demo Page Flow

- command: context confirmation
- output: confirmed `git status --short --branch`, `ai-status`, and
  `ai-doctor`; repo is in large mode and `.ai/state.json` remains
  `DONE/current_gate: none`.
- command: required reading
- output: read `AGENTS.md`, `docs/ai/README.md`, `docs/ai/workflow.md`,
  Phase 9/Phase 10-related durable docs, and active `.ai` runtime files before
  editing.
- command: task contract
- output: classified the implementation work as Level 2 / medium under harness
  large mode. Target is a PRD-shaped static demo page, with no API/schema
  changes unless necessary.
- command: demo/API inspection
- output: inspected current `demo.html`, demo route, targeted tests, and
  existing knowledge/tender/retrieval/generation response shapes.
- command: implementation decision
- output: chose page-layer mapping from PRD labels to existing deterministic
  retrieval tags so the page can tell the PRD story without changing backend
  retrieval/generation contracts.
- command: demo page rewrite
- output: rebuilt `backend/app/static/demo.html` into sections for historical
  ingestion, knowledge cards, tender analysis, PRD tag selection, retrieval
  evidence, candidate generation, review evidence, and OCR smoke status.
- command: targeted tests update
- output: updated `test_demo_page.py` static assertions and expanded
  `test_phase5_demo_workflow.py` into a Phase 10 API chain covering upload,
  parse, build knowledge cards, analyze tender, retrieve, and generate.
- mid-task review
- output: no scope expansion beyond static page, targeted tests, and docs. One
  workflow test failed because the fake parser dependency override created a new
  parser instance per request; fixed by sharing one parser instance.
- command: targeted pytest
- output: `backend/tests/test_demo_page.py` and
  `backend/tests/test_phase5_demo_workflow.py` passed: `6 passed, 1 warning`.
- command: docs/runtime update
- output: added Phase 10 durable docs, updated roadmap/docs index, and rewrote
  active `.ai` runtime artifacts for the Phase 10 task.

## Phase 9 Context Carried Forward

- `paddleocr 2.10.0`
- `paddlepaddle 2.6.2`
- `parse_mode=ocr` smoke: `1 section / 1 chunk`
- `parse_mode=auto` smoke: OCR fallback passed
- `PyMuPDF` remains local-smoke-only and is not added to project dependencies
