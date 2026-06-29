# Affected Files - Phase 11 Sample Outputs

## Added Files

Docs:

- `docs/ai/36-phase11-sample-outputs-dev-spec.md`
- `docs/ai/37-phase11-test-cases.md`
- `docs/ai/38-phase11-repeatable-demo-runbook.md`

Sample JSON:

- `docs/ai/sample-outputs/phase11/manifest.json`
- `docs/ai/sample-outputs/phase11/historical-bid-upload-parse.json`
- `docs/ai/sample-outputs/phase11/knowledge-cards.json`
- `docs/ai/sample-outputs/phase11/tender-analysis.json`
- `docs/ai/sample-outputs/phase11/retrieval-evidence.json`
- `docs/ai/sample-outputs/phase11/generation-candidate.json`
- `docs/ai/sample-outputs/phase11/no-llm-error.json`
- `docs/ai/sample-outputs/phase11/ocr-smoke-status.json`
- `docs/ai/sample-outputs/phase11/expected-failures.json`

Tests:

- `backend/tests/test_phase11_sample_outputs.py`

## Updated Files

- `docs/ai/README.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

## Forbidden Areas

- backend API contracts
- database schema
- runtime dependencies
- customer source files
- generated runtime data under `data/`
- PyMuPDF project dependency
- Qdrant/Haystack/embeddings
- final document export
