# Implementation Plan - Phase 8B OCR Adapter For Scanned PDFs

## Execution Classification

- Harness mode: `large`
- Task level: Level 3 / complex
- Reason: Phase 8B changes the shared parse path by adding `parse_mode`,
  OCR fallback, optional external OCR dependency boundaries, and OCR metadata.
- Rollback: normal Git revert before commit. Database changes should stay
  within existing parse metadata and section/chunk persistence.

Status: implemented locally on 2026-06-28.

## Target Outcome

Add a replaceable OCR adapter that can turn scanned PDF pages into normal
sections/chunks while keeping existing text parsing behavior intact.

## Non-Goals

No required PaddleOCR install, no OCR for large image batches, no certificate
validation, no table reconstruction, no vector store, no embeddings, no LLM
parsing, no export, and no final bidding output.

## Subagent Plan

No subagent is planned at task start.

Reason: implementation is a single coupled parse-path change. Add a read-only
reviewer only if OCR fallback semantics expand beyond PDF or optional
dependency handling becomes risky.

## Implementation Stages

### Stage 1 - Runtime Artifacts

1. Update `.ai/spec.md`, `.ai/implementation-plan.md`, and
   `.ai/affected-files.md` to Phase 8B.
2. Confirm harness state remains `large`.

Verification:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

### Stage 2 - OCR Adapter Interface

1. Add `backend/app/adapters/ocr_adapter.py`.
2. Define `OCRPageText`, `OCRAdapter`, `OCRError`, and optional
   `PaddleOCRAdapter`.
3. Keep imports lazy.
4. Add fake OCR tests.

Verification:

```powershell
& $py -m pytest backend/tests/test_ocr_adapter_parse.py
```

### Stage 3 - Parse Mode API

1. Add `ParseDocumentRequest`.
2. Accept optional body on `POST /api/documents/{document_id}/parse`.
3. Default missing body to `auto`.
4. Add OCR adapter dependency injection seam.

Verification:

```powershell
& $py -m pytest backend/tests/test_document_parse_api.py backend/tests/test_ocr_adapter_parse.py
```

### Stage 4 - OCR Integration

1. Integrate OCR into `document_parsing.parse_document`.
2. Preserve DOCX and legacy Word conversion behavior.
3. For PDFs:
   - `text`: parser only
   - `ocr`: OCR only
   - `auto`: parser first, OCR fallback on parser failure or empty chunks
4. Convert OCR pages into `NormalizedSection` values.
5. Add OCR metadata to parse metadata.
6. Sanitize OCR errors.

Verification:

```powershell
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
```

### Stage 5 - Docs And Evidence

1. Update README and durable docs.
2. Add Phase 8B dev spec, test cases, and runbook.
3. Update `.ai/run-trace.md`, `.ai/verification.md`, `.ai/evaluation.md`, and
   `.ai/handoff.md`.

Verification:

```powershell
git diff --check
```

### Stage 6 - Final Verification

1. Run harness checks.
2. Run targeted OCR tests.
3. Run PowerShell project check.
4. Run full backend pytest.
5. Attempt bash check if shell tooling exists.
6. Record residual risk and optional PaddleOCR manual-smoke status.

Verification:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
.\scripts\ai_check.ps1
python -m pytest backend/tests
```

## Mid-Task Review Checkpoint

After Stage 4, perform a self-review:

1. Is OCR still limited to scanned PDF parse support?
2. Did PaddleOCR become a required test/default dependency?
3. Did OCR alter the successful text-PDF path?
4. Are OCR errors sanitized?
5. Is verification still sufficient?

Decision must be recorded in `.ai/run-trace.md`.

## Escalation Triggers

Pause or escalate if:

1. Image upload support becomes necessary.
2. PaddleOCR install/model downloads become required for automated tests.
3. OCR output needs table reconstruction or document validation.
4. The parse API change breaks existing no-body parse clients.
5. Error handling risks exposing local paths or OCR model cache paths.
