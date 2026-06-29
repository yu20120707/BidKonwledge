# Evaluation

## Phase 11 Sample Outputs And Repeatable Runbook Evaluation

Status: implemented locally and verified.

Implemented:

1. Added fixed Phase 11 sample manifest.
2. Added representative JSON outputs for historical parse, knowledge cards,
   tender analysis, retrieval evidence, candidate generation, no-LLM fallback,
   OCR smoke status, and expected failures.
3. Added Phase 11 dev spec, test cases, and repeatable demo runbook.
4. Added pytest validation for JSON validity, manifest completeness, and
   secret/runtime-path boundaries.
5. Updated roadmap, docs index, lightweight PRD plan, and active `.ai` files.

Scope control:

1. No backend API/schema change.
2. No dependency change.
3. No customer source files committed.
4. No runtime upload/database/temp/OCR cache artifacts committed.
5. No PyMuPDF project dependency addition.
6. No semantic retrieval, table reconstruction, login, export, or certificate
   authenticity validation.

Verification summary:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed.
- targeted pytest final rerun: `3 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed with `114 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: not verified because WSL/Linux distro is
  unavailable.

Residual risk:

1. `bash ./scripts/ai_check.sh` remains blocked by missing WSL/Linux distro on
   this Windows machine.
2. The sample JSON files are representative replay artifacts, not proof that
   every source sample will produce identical counts on every parser/runtime
   version.
