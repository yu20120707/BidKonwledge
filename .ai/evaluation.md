# Evaluation

## Phase 10 PRD-shaped Demo Page Flow Evaluation

Status: implemented locally and verified.

Implemented:

1. Rebuilt `/demo` into a PRD-shaped narrative page.
2. Split the page into historical ingestion, knowledge cards, tender analysis,
   PRD tag selection, retrieval evidence, candidate generation, review
   evidence, and OCR status.
3. Added explicit page-layer mapping from PRD labels to existing deterministic
   retrieval tags.
4. Kept Raw JSON visible for each stage.
5. Limited OCR copy to Phase 9 smoke evidence only.
6. Expanded targeted tests to cover the new static page boundary and the Phase
   10 API chain.

Scope control:

1. No route change.
2. No backend API/schema change.
3. No dependency change.
4. No PyMuPDF project dependency addition.
5. No semantic retrieval, table reconstruction, login, export, or certificate
   validation.

Verification summary:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed.
- targeted pytest final rerun: `6 passed, 1 warning`.
- targeted regression after boundary-test update: `8 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed with `111 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: not verified because WSL/Linux distro is
  unavailable.
- `/demo` HTTP smoke through FastAPI TestClient: HTTP `200`, with Phase 10
  title and OCR boundary copy present.

Residual risk:

1. `bash ./scripts/ai_check.sh` remains blocked by missing WSL/Linux distro on
   this Windows machine.
2. `.ai/state.json` remains `DONE/current_gate: none`; no new harness gate
   transition is claimed.
