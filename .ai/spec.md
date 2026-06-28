# Spec - Phase 9 Real PaddleOCR Runtime And Scanned PDF Smoke

## Objective

Verify the existing Phase 8B OCR adapter with a real local PaddleOCR runtime and
one scanned PDF smoke before Phase 10 presents OCR in the PRD-shaped demo page.

This phase is an environment and evidence phase. It may fix narrow OCR-runtime
dependency bugs, but it must not expand OCR into table reconstruction, large
image batch ingestion, certificate validation, or semantic retrieval.

Status: in progress on 2026-06-28.

## Required Execution Mode

This task runs under Auto_AICoding_Harness `large` mode with the
`python-backend-service` profile.

Current harness state remains:

- `mode: large`
- `status: DONE`
- `current_gate: none`

Do not claim a new Phase 9 harness gate transition unless the matching harness
command succeeds.

## Baseline

Already available:

1. Phase 8B fake-testable OCR adapter and `parse_mode=auto|text|ocr`.
2. Forced OCR mode for PDFs.
3. Auto fallback to OCR when PDF text parsing fails or produces no chunks.
4. OCR metadata persisted in parse/chunk metadata.
5. Phase 9 durable docs:
   - `docs/ai/30-phase9-real-ocr-smoke-dev-spec.md`
   - `docs/ai/31-phase9-test-cases.md`
   - `docs/ai/32-phase9-demo-runbook.md`

## In Scope

1. Install and verify optional OCR runtime dependencies on the local machine.
2. Add missing non-default OCR dependency declarations when real runtime proof
   shows they are required.
3. Fix narrow runtime-loading issues in `PaddleOCRAdapter`.
4. Select one small indexed scanned/image sample and convert it to a temporary
   PDF outside Git.
5. Run API-level forced OCR parse smoke.
6. Run API-level `auto` fallback smoke.
7. Update `.ai` evidence with commands, results, and residual risks.

## Out Of Scope

1. Do not add PaddleOCR/PaddlePaddle to default dependencies.
2. Do not commit customer samples, temporary PDFs, OCR outputs, or model files.
3. Do not add PyMuPDF to project dependencies without explicit license review.
4. Do not implement table reconstruction.
5. Do not support large image batch ingestion.
6. Do not validate certificates, seals, or qualification evidence.
7. Do not add Qdrant, Haystack, embeddings, dense retrieval, or hybrid
   retrieval.

## Acceptance Criteria

Phase 9 is accepted when:

1. `paddleocr` and `paddle` import successfully in the project runtime.
2. The OCR optional dependency group declares the required PaddlePaddle runtime.
3. Runtime import failures are surfaced as sanitized `OCRError` values.
4. A selected scanned/image sample converted to a temporary PDF can be uploaded
   and parsed with `parse_mode=ocr`.
5. The same sample can be uploaded and parsed with `parse_mode=auto`, with OCR
   fallback evidence in metadata.
6. OCR output creates normal sections/chunks and includes OCR metadata.
7. Automated fake-OCR tests and project verification still pass.
8. PyMuPDF/fitz use is recorded as local smoke-only because its license is
   dual AGPL/commercial.
