# Handoff

## Current State - Phase 10 PRD-shaped Demo Page Flow

Phase 10 implementation is complete, verified locally, and ready to be committed
before Phase 11 starts.

Current harness state:

- mode: `large`
- profile: `python-backend-service`
- state status: `DONE`
- current gate: none

Important harness note:

- `.ai/state.json` still reflects `DONE/current_gate: none`.
- Do not claim a new gate has opened unless the matching harness command
  succeeds.

Implemented in Phase 10:

1. `/demo` has been rebuilt into a PRD-shaped narrative page.
2. The page now shows:
   - historical bid upload/parse
   - knowledge card build/display
   - tender upload/parse/analysis
   - PRD tag selection
   - retrieval evidence
   - candidate generation
   - citations, risks, human review, raw JSON
   - OCR smoke status
3. PRD labels are mapped at the page layer to the current deterministic
   retrieval tags; backend retrieval/generation contracts were not changed.
4. OCR text is limited to Phase 9 smoke evidence:
   - `paddleocr 2.10.0`
   - `paddlepaddle 2.6.2`
   - `parse_mode=ocr` smoke: `1 section / 1 chunk`
   - `parse_mode=auto` smoke: OCR fallback passed
   - `PyMuPDF` remains local-smoke-only
5. Targeted tests now cover the Phase 10 page structure and API chain.

Latest verification:

- `ai-status`: passed.
- `ai-doctor`: passed.
- targeted pytest:
  `backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py`
  -> `6 passed, 1 warning`
- targeted regression including boundary check:
  `backend/tests/test_phase5_boundaries.py backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py`
  -> `8 passed, 1 warning`
- `.\scripts\ai_check.ps1`: passed with `111 passed, 1 warning`
- `git diff --check`: passed with line-ending normalization warnings only
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distro is
  available
- `/demo` HTTP smoke: HTTP `200`, Phase 10 title present, OCR boundary copy
  present

Outstanding blocker:

1. Bash verification is still unavailable on this Windows machine because WSL
   / Linux distro is not installed.
