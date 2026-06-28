# Spec - Phase 8B OCR Adapter For Scanned PDFs

## Objective

Implement the next lightweight PRD closure phase: add a replaceable OCR adapter
for scanned or image-heavy PDFs while preserving the existing Docling-first
parse behavior for true `.docx`, legacy-converted Word, and text-based PDFs.

This phase is OCR adapter integration, not full document forensics or
qualification-material validation.

Status: implemented locally on 2026-06-28.

## Required Execution Mode

This task must run under Auto_AICoding_Harness `large` mode with the
`python-backend-service` profile.

Current harness state remains the previous completed state:

- `mode: large`
- `status: DONE`
- `current_gate: none`

Do not claim a Phase 8B gate transition unless a harness command succeeds.

## Baseline

Already implemented locally:

1. Phase 1 upload and SQLite document metadata.
2. Phase 2 Docling parsing for true `.docx` and text-based `.pdf`.
3. Phase 2 section/chunk persistence and parse status handling.
4. Phase 3 local deterministic retrieval.
5. Phase 4 generation with citations, risks, and human review.
6. Phase 5 local demo page.
7. Phase 6 knowledge cards.
8. Phase 7 tender analysis.
9. Phase 8A legacy/mislabeled Word conversion with safe parse metadata.

Current verified baseline:

- `.\scripts\ai_check.ps1`: `102 passed, 1 warning`.
- `python -m pytest backend/tests`: `102 passed, 1 warning`.
- `bash ./scripts/ai_check.sh`: not verified because no usable WSL/Linux
  distribution is available on this Windows machine.

## In Scope For Phase 8B

Implement only:

1. Add a fake-testable OCR adapter interface.
2. Add an optional PaddleOCR-backed implementation behind lazy imports.
3. Add `parse_mode` for `POST /api/documents/{document_id}/parse`:
   - `auto`
   - `text`
   - `ocr`
4. Preserve default behavior: `auto` first tries existing text parsing.
5. For PDFs, `auto` may fallback to OCR when text parsing fails or produces no
   chunks.
6. `text` must never run OCR.
7. `ocr` must force OCR for supported OCR formats.
8. Build normal sections/chunks from OCR page text.
9. Record OCR metadata:
   - parse mode
   - OCR attempted
   - OCR engine
   - page count
   - confidence
   - OCR fallback reason when applicable
10. Keep API and persisted errors sanitized.
11. Add tests using a fake OCR adapter. Automated tests must not require
    PaddleOCR or model downloads.
12. Update README, docs, and `.ai` evidence.

## Out Of Scope For Phase 8B

Do not implement:

1. PaddleOCR as a required default dependency.
2. OCR for every image type or large image batch directory.
3. CA signing, qualification evidence validation, or official certificate
   verification.
4. Table structure reconstruction.
5. Qdrant, Haystack, embeddings, dense retrieval, or hybrid retrieval.
6. LLM-based parsing or tender understanding.
7. User system, export, or final bidding output.
8. Committing customer scanned material or generated runtime OCR outputs.

## OCR Adapter Contract

Expected adapter shape:

```text
OCRAdapter.extract(file_path) -> list[OCRPageText]
```

Recommended fields:

- `page_number`
- `text`
- `confidence`
- `engine`
- `blocks`
- `metadata`

The production implementation can be PaddleOCR-backed, but imports and model
initialization must be lazy. Tests must inject fake adapters.

## Parse Mode Contract

Request shape:

```json
{
  "parse_mode": "auto"
}
```

Rules:

1. Missing body defaults to `auto` for backward compatibility.
2. `auto`:
   - DOCX/converted Word: existing parser only.
   - text PDF: existing parser first.
   - scanned PDF or text parser failure: OCR fallback.
3. `text`: existing parser only; OCR disabled.
4. `ocr`: OCR only for PDF in this phase.

## Expected File Scope

Implementation files:

```text
backend/app/adapters/ocr_adapter.py
backend/app/api/documents.py
backend/app/services/document_parsing.py
backend/app/services/section_chunker.py
backend/app/schemas/document.py
pyproject.toml
```

Test files:

```text
backend/tests/test_ocr_adapter_parse.py
backend/tests/test_phase8b_boundaries.py
```

Documentation and evidence:

```text
README.md
docs/ai/03-data-model.md
docs/ai/04-api-contract.md
docs/ai/09-phase-roadmap.md
docs/ai/17-lightweight-prd-completion-plan.md
docs/ai/27-phase8b-ocr-adapter-dev-spec.md
docs/ai/28-phase8b-test-cases.md
docs/ai/29-phase8b-demo-runbook.md
.ai/spec.md
.ai/implementation-plan.md
.ai/affected-files.md
.ai/run-trace.md
.ai/verification.md
.ai/evaluation.md
.ai/handoff.md
```

## Acceptance Criteria

Phase 8B is accepted when:

1. Existing no-body parse requests still default to `auto`.
2. Text-based PDF parse remains OCR-free when the existing parser succeeds.
3. `parse_mode = text` does not call OCR.
4. `parse_mode = ocr` uses injected OCR output to create sections/chunks.
5. `parse_mode = auto` falls back to OCR when text parsing fails or produces no
   chunks for PDF.
6. OCR chunks include source metadata and deterministic tags.
7. OCR failure marks parse failed with sanitized message.
8. Automated tests pass without PaddleOCR, Qdrant, Haystack, embeddings, LLM
   credentials, or real external services.
9. Existing Phase 1-8A tests continue to pass.

## Required Verification Commands

Run before completion:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
.\scripts\ai_check.ps1
python -m pytest backend/tests
```

Run `bash ./scripts/ai_check.sh` if shell tooling is available. If WSL/bash is
unavailable, record the blocker and do not claim it passed.
