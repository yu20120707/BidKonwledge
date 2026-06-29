# Phase 11 Sample Outputs Dev Spec

## Purpose

Phase 11 makes the server demo repeatable by another engineer or agent. It
turns the Phase 10 PRD-shaped page into a fixed replay package:

1. fixed sample file choices
2. selected PRD tags and retrieval mappings
3. representative JSON outputs for each major API stage
4. expected failure and fallback behavior
5. a repeatable operator runbook

## Execution Level

Use harness `large` mode because the repository requires it after Phase 0.
Classify the implementation work itself as Level 2 / medium because it spans
several documentation and sample-output files, but does not change backend API,
schema, runtime dependencies, or the demo page contract.

Escalate if:

1. real backend code must change to produce the sample output
2. Phase 11 requires new public API fields
3. sample generation starts copying customer files or generated runtime data
   into Git

## In Scope

1. Add a fixed sample manifest under `docs/ai/sample-outputs/phase11/`.
2. Add representative JSON outputs for:
   - historical upload and parse
   - knowledge cards
   - tender analysis
   - retrieval evidence
   - candidate generation
   - no-LLM failure
   - OCR smoke status
   - expected failures and deferred files
3. Add a repeatable Phase 11 runbook.
4. Add a lightweight pytest that validates the JSON files and secret boundary.
5. Update roadmap, docs index, and active `.ai` runtime files.

## Out Of Scope

1. No customer source documents are committed.
2. No `data/` runtime uploads, SQLite databases, temporary PDFs, OCR model
   caches, or generated outputs are committed.
3. No Qdrant, Haystack, embeddings, dense retrieval, or semantic retrieval.
4. No table reconstruction.
5. No image batch ingestion.
6. No certificate or qualification-material authenticity validation.
7. No login/user system.
8. No final Word/PDF export.
9. No PyMuPDF project dependency addition.

## Sample Output Policy

The Phase 11 JSON files are representative replay artifacts, not production
records. They must:

1. preserve API response shape
2. use deterministic placeholder ids
3. use catalog-relative paths instead of committed binary files
4. use脱敏片段 or representative snippets instead of customer text dumps
5. keep all generated content marked as candidate content requiring human review
6. omit API keys, bearer tokens, local temp paths, and generated runtime files

## Fixed Demo Set

Use the source root recorded in `docs/source-materials/sample-catalog.md`.

1. Historical bid primary:
   `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
2. Historical bid qualification-side sample:
   `宁波运维项目\牧鸿\省人事工资管理服务系统-宁波人社运维-资格证明文件.docx`
3. Tender primary:
   `KSDQZFCG（GK）2026-64...项目（二次）.docx`
4. OCR smoke sample:
   `宁波运维项目\九州拓新\批量输出为图片\...\_08.png`

## Acceptance Criteria

1. Another engineer can identify the exact fixed sample set.
2. Another engineer can replay the demo through `/demo` or direct API calls.
3. Sample JSON files are valid JSON and listed from the manifest.
4. The sample package records success, no-LLM failure, OCR dependency failure,
   text-PDF behavior, scanned-PDF OCR fallback, and large-file deferral.
5. Phase 11 does not add runtime dependencies or backend behavior.
