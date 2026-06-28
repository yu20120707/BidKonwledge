# Implementation Plan - Phase 9 Real OCR Smoke

## Execution Classification

- Harness mode: `large`
- Task level: Level 2 / medium
- Reason: Phase 9 verifies a real optional runtime and may require narrow
  dependency/runtime fixes, but it does not change public API shape or core data
  model.
- Escalation trigger: adding image ingestion, table reconstruction, vector
  retrieval, or committing a new license-sensitive dependency to the project
  dependency set.

## Target Outcome

Real PaddleOCR can be exercised through the existing parse API for one scanned
PDF smoke, or the exact blocker is recorded with sanitized failure behavior.

## Plan

1. Confirm harness and clean baseline.
2. Run fake-OCR targeted regression tests.
3. Install `.[ocr]` and verify imports.
4. Fix only runtime dependency issues discovered by the real smoke.
5. Select a small indexed image sample and create a temporary PDF outside Git.
6. Run forced OCR API smoke.
7. Run `auto` fallback API smoke.
8. Update `.ai` evidence and active runtime files.
9. Run targeted tests, full project check, `pip check`, and diff hygiene.

## Mid-Task Review

Status versus original plan:

- The task stayed focused on real OCR smoke.
- Scope expanded narrowly to add `paddlepaddle>=2.6,<3.0` to the OCR optional
  dependency group and to preload Torch before PaddleOCR import on Windows.
- PyMuPDF was needed by PaddleOCR for PDF input, but it is not added to
  project dependencies because the repo guardrail says to avoid AGPL
  dependencies without explicit approval.

Decision: keep Phase 9 plan. Record PyMuPDF as local smoke-only and license
risk, not as committed project dependency.

## Verification Plan

Required:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
& $py -m pip check
.\scripts\ai_check.ps1
git diff --check
```

Also attempt `bash ./scripts/ai_check.sh` if WSL/bash becomes available.
