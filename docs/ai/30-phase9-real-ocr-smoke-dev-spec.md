# Phase 9 Real OCR Smoke Dev Spec

## Purpose

Phase 9 verifies the optional PaddleOCR-backed OCR path with a real local
runtime and one scanned PDF smoke. Phase 8B already added the fake-testable OCR
adapter and parse-mode contract; Phase 9 is the environment and evidence step
before the PRD demo page presents OCR as a demonstrated capability.

This phase does not expand the OCR feature surface. It proves whether the
existing adapter can run on this machine and records what remains
environment-dependent.

## Execution Level

Use harness `large` mode because this repository requires large mode after
Phase 0. Classify the implementation work itself as Level 2 / medium in the
AGENTS.md risk model if the task only installs optional dependencies, selects a
sample, runs smoke checks, and updates evidence. Escalate if OCR integration
code changes become necessary.

## Preconditions

1. `.ai/state.json` reports `"mode": "large"`.
2. Phase 8B code and fake-OCR tests are present.
3. Normal backend tests pass before treating OCR-specific failures as isolated.
4. A small scanned PDF or image-derived PDF sample is selected from
   `docs/source-materials/sample-catalog.md`.
5. Customer samples stay outside Git; document only the indexed path and smoke
   result.

## Target Outcome

After Phase 9, the repo should have truthful evidence for one of these states:

1. Real PaddleOCR smoke passed and produced OCR-derived chunks through the
   existing parse API.
2. Real PaddleOCR installed but the selected sample failed with a sanitized,
   documented OCR error.
3. Real PaddleOCR could not be installed or initialized, with the blocking
   dependency, model download, or runtime error recorded.

Any of those outcomes can be valid for Phase 9 if the evidence is explicit.

## Scope

1. Install optional OCR dependencies with `pip install -e ".[ocr]"`.
2. Verify `import paddleocr` and local package version if available.
3. Verify lazy construction of the PaddleOCR-backed adapter.
4. Upload one selected scanned PDF through the existing upload API.
5. Parse it with `parse_mode=ocr`.
6. Parse it with `parse_mode=auto` when the text parser fails or produces no
   chunks.
7. Inspect `parse_metadata` and chunk metadata for OCR evidence:
   - `ocr_attempted`
   - `ocr_engine`
   - `ocr_pages_count`
   - OCR confidence or page metadata when available
8. Update Phase 9 evidence in `.ai/verification.md`, `.ai/evaluation.md`, and
   `.ai/handoff.md` when the smoke is actually run.

## Non-Goals

1. Do not add PaddleOCR to default dependencies.
2. Do not require PaddleOCR for normal pytest or `scripts/ai_check.ps1`.
3. Do not implement table reconstruction.
4. Do not ingest large image batches.
5. Do not validate certificates, seals, or qualification evidence.
6. Do not add Qdrant, Haystack, embeddings, dense retrieval, or hybrid
   retrieval.
7. Do not change the public parse API unless a real smoke failure proves the
   current contract is unusable.

## Expected File Scope

Likely changed:

1. `.ai/verification.md`
2. `.ai/evaluation.md`
3. `.ai/handoff.md`
4. `README.md` if the operator command needs correction after the real smoke

Only change implementation files if the real OCR smoke exposes a concrete bug
in the already-implemented Phase 8B adapter.

## Verification

Required:

1. `scripts/ai_check.ps1`
2. Targeted OCR tests:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
```

3. Real OCR dependency check:

```powershell
& $py -m pip install -e ".[ocr]"
& $py -c "import paddleocr; print(paddleocr.__version__)"
```

4. Live API smoke with one scanned PDF:
   - upload
   - forced OCR parse
   - optional auto fallback parse
   - chunk inspection

Also run `bash ./scripts/ai_check.sh` when shell tooling is available. On this
Windows machine, document the WSL/Linux-distribution blocker if it is still
unavailable.

## Exit Criteria

1. The real OCR runtime status is recorded as passed, failed, or blocked with
   concrete command evidence.
2. Normal automated tests still do not require PaddleOCR.
3. No customer sample content is committed.
4. OCR-derived output remains marked as needing human review downstream.
5. Remaining OCR limitations are explicit before Phase 10 begins.
