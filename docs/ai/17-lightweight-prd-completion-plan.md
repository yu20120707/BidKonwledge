# Lightweight PRD Completion Plan

## Purpose

This document supplements the current implementation roadmap after comparing
the repository with `docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf`.

The goal is still a lightweight capability-validation demo, not a complete
bidding system. OCR is now included as a planned lightweight-demo capability,
but it must remain behind a replaceable adapter and must not expand into a full
document-forensics or qualification-material workflow.

## PRD Target Chain

The PRD asks the demo to prove this chain:

```text
historical bid files
-> parse directory/body/tables
-> split into tagged knowledge cards
-> new tender file
-> extract requirements/scoring/disqualification risks
-> retrieve historical knowledge by target tag
-> call external LLM API
-> return generated content, citations, risks, human review marker, and JSON
-> show the result in a demo page
```

## Current Implementation Snapshot

Implemented:

1. File upload.
2. SQLite document metadata.
3. Docling-based `.docx` and text-based `.pdf` parsing.
4. Section and chunk persistence.
5. Deterministic lightweight tags.
6. Local tag/query retrieval over chunks.
7. Candidate generation with an OpenAI-compatible LLM adapter.
8. Request-scoped user LLM API key/base URL/model for demo generation.
9. Citations, risks, and `need_human_review = true`.
10. Minimal FastAPI-hosted demo page.
11. Knowledge cards as a first-class API/data layer.
12. PRD-aligned tag taxonomy for historical bid knowledge cards.
13. Tender analysis for project requirements, scoring items, and
    disqualification risks.

Missing against the PRD:

1. OCR for scanned PDFs and image-heavy pages.
2. Table-aware extraction and display.
3. Demo page flow that clearly separates historical bid ingestion from tender
   analysis.
4. Fixed sample JSON output and PRD-style demo runbook.
5. Optional semantic/vector retrieval after the lightweight baseline proves the
   workflow.

## Proposed Phase Plan

### Phase 6 - Knowledge Cards And PRD Tags

Status: complete.

Goal: convert parsed historical bid chunks into PRD-visible knowledge cards.

Scope:

1. Add `knowledge_cards` persistence.
2. Add `POST /api/knowledge/build`.
3. Add `GET /api/documents/{document_id}/knowledge-cards` or equivalent.
4. Expand deterministic tags toward PRD terms:
   - `运维服务实施方案`
   - `突发应急方案和措施`
   - `网络和数据安全防护保障措施`
   - `服务质量保障和考核评估方案`
   - `团队人员`
   - `业绩情况`
   - `资格材料`
5. Keep chunk-to-card mapping deterministic and explainable.

Non-goals:

- No embeddings.
- No Qdrant/Haystack.
- No full taxonomy management UI.

Acceptance:

1. Upload and parse one historical bid `.docx`.
2. Build at least one knowledge card.
3. Retrieve or inspect cards by PRD-like tag.
4. Cards include source file, section title/path, snippet, tags, and confidence
   or rule metadata.

### Phase 7 - Tender Analysis

Status: complete.

Goal: make the new tender-file side of the PRD visible.

Scope:

1. Add `POST /api/tender/analyze`.
2. Extract lightweight rule-based:
   - project requirements
   - scoring items
   - disqualification risks
3. Persist or return a `TenderAnalysis` result.
4. Feed selected tender requirements into generation prompts.
5. Add demo page area for tender analysis JSON.

Non-goals:

- No complete tender understanding.
- No guarantee that all scoring or disqualification terms are captured.
- No formal legal/compliance decisioning.

Acceptance:

1. Upload and parse one tender `.docx`.
2. Analyze returns non-empty requirements or a clear empty result with risks.
3. Demo can select a target tag and generate from tender requirement plus
   historical knowledge context.

### Phase 8A - Legacy / Mislabeled Word Conversion Adapter

Status: complete.

Goal: support real tender samples that have legacy OLE Word content, including
files mislabeled with a `.docx` extension, without implementing OCR.

Scope:

1. Detect file content headers before parse.
2. Convert legacy Word content to a derived true `.docx` path when Word COM is
   available.
3. Preserve the original uploaded file unchanged.
4. Record safe parse metadata.
5. Keep automated tests fake-converter based.

Non-goals:

- No OCR/PaddleOCR.
- No semantic parsing or tender understanding.
- No final document generation or export.

### Phase 8B - OCR Adapter For Scanned Material

Status: complete for scanned PDF adapter baseline.

Goal: support lightweight OCR for scanned PDFs and image-heavy pages while
keeping OCR replaceable.

Recommended route:

1. Keep Docling as the primary parser for `.docx` and text-based `.pdf`.
2. Add an OCR adapter interface, for example:

```text
OCRAdapter.extract(file_path) -> list[OCRPageText]
```

3. Add a PaddleOCR-backed implementation behind an optional dependency group.
4. Use OCR only when:
   - PDF has little or no text layer,
   - file type is image,
   - or the user explicitly requests OCR parse.
5. Store OCR evidence in chunk metadata:
   - `ocr_engine`
   - `ocr_confidence`
   - `page_number`
   - optional bounding boxes when available.

Initial API option:

```json
{
  "parse_mode": "auto | text | ocr"
}
```

Security and operational guardrails:

1. OCR dependency must be optional and documented.
2. OCR processing should have file-size and page-count limits.
3. OCR errors must set `parse_status = failed` with a sanitized message.
4. Do not copy customer scanned material into Git.
5. Do not log extracted sensitive content beyond test fixtures.

Non-goals:

- No CA signing, qualification evidence validation, or official certificate
  verification.
- No full scanned-document review UI.
- No promise that OCR output is legally reliable.

Acceptance:

1. Text-layer PDF still parses without OCR.
2. A small scanned/image sample can produce text chunks through OCR.
3. OCR chunks carry source metadata and `need_human_review` remains true for
   downstream generated output.
4. Tests can run without installing PaddleOCR by using an injected fake OCR
   adapter.
5. A manual OCR smoke test is documented separately because real OCR models may
   be heavy and environment-dependent.

Implemented baseline:

1. `OCRAdapter.extract(file_path)`.
2. Fake-testable OCR page text model.
3. Lazy PaddleOCR-backed adapter.
4. `parse_mode = auto | text | ocr`.
5. PDF OCR fallback.
6. OCR metadata on parse/chunk outputs.

Still deferred:

- Large image batch ingestion.
- Table reconstruction.
- Real PaddleOCR model/runtime smoke on server.

### Phase 9 - Real PaddleOCR Runtime And Scanned PDF Smoke

Goal: verify that the optional PaddleOCR-backed OCR adapter runs on the local
machine with a real scanned PDF before OCR is presented in the PRD demo flow.

Scope:

1. Install the optional OCR dependency group in the local runtime.
2. Verify `paddleocr` imports and the lazy `PaddleOCRAdapter` can be
   constructed.
3. Select one small scanned PDF or image-derived PDF sample from
   `docs/source-materials/sample-catalog.md`.
4. Upload the sample and force `parse_mode=ocr`.
5. Run `parse_mode=auto` when the text parser fails or produces no chunks.
6. Record OCR parse metadata, chunk metadata, model download behavior,
   cold-start behavior, and sanitized failure behavior.

Non-goals:

- No table reconstruction.
- No large image batch ingestion.
- No qualification-material or certificate validation.
- No default dependency change that makes PaddleOCR required for automated
  tests.
- No Qdrant, Haystack, embeddings, or semantic retrieval.

Acceptance:

1. A real OCR environment check is documented as passed or failed with evidence.
2. A selected scanned PDF either produces OCR-derived chunks or fails with a
   sanitized, documented OCR error.
3. Existing fake-OCR automated tests remain the default test strategy.
4. The demo can truthfully distinguish implemented adapter support from real
   OCR runtime proof.

### Phase 10 - PRD Demo Flow Page

Goal: make the demo page match the PRD story, not only expose raw endpoints.

Scope:

1. Split the page into:
   - Historical bid ingestion
   - Tender upload and analysis
   - Target tag selection
   - Retrieval evidence
   - Candidate generation
   - Citations, risks, human review, raw JSON
2. Add target-tag dropdown with PRD-like labels.
3. Add demo status panels for:
   - parsed historical files
   - generated knowledge cards
   - tender analysis result
   - retrieval result count
4. Keep it a single FastAPI-hosted static page.

Non-goals:

- No formal frontend app.
- No login.
- No project/file-management system.
- No final bidding document editor.

Acceptance:

1. A stakeholder can follow the PRD flow on one page.
2. The page still exposes raw JSON for every stage.
3. Generated content is clearly candidate content and requires human review.

### Phase 11 - Sample Outputs And Runbook

Status: complete.

Goal: make the server demo repeatable.

Scope:

1. Create a fixed runbook for:
   - 2 historical bid files
   - 1 tender file
   - selected target tags
2. Add sample JSON output files under docs, not generated runtime artifacts.
3. Record expected success/failure behavior for:
   - no LLM key
   - text PDF
   - scanned PDF requiring OCR
   - large files intentionally deferred.

Acceptance:

1. Another agent or engineer can reproduce the demo.
2. The runbook states exact sample files, commands, expected outputs, and known
   limits.

### Phase 12 - Semantic Retrieval Adapter Spike

Goal: bring Qdrant, Haystack, and embeddings into the mainline only after the
deterministic PRD demo baseline is repeatable.

Scope:

1. Keep the existing deterministic retrieval path as the default.
2. Add or document a replaceable semantic retrieval adapter boundary.
3. Evaluate Qdrant collection creation and indexing over persisted chunks or
   knowledge cards.
4. Evaluate Haystack query pipeline integration.
5. Evaluate a local or provider-backed embedding strategy.
6. Compare retrieval results against the fixed Phase 11 sample set.

Non-goals:

- No mandatory Qdrant/Haystack service for normal tests.
- No broad schema migration before the spike proves value.
- No replacement of deterministic retrieval without an evaluation result.

Acceptance:

1. Semantic retrieval can be enabled or disabled without affecting the default
   demo path.
2. The spike records dependency setup, indexing behavior, retrieval quality
   notes, and rollback path.
3. The next implementation decision is explicit: keep as optional, promote to
   default, or defer.

## Dependency Plan

### Required For Current Demo

- FastAPI
- Pydantic
- SQLite
- Docling for `.docx` and text-based `.pdf`
- OpenAI-compatible LLM endpoint

### Add For OCR

Preferred:

- PaddleOCR as optional OCR adapter.

Possible fallback:

- Keep the OCR adapter interface first.
- Use a fake OCR adapter in automated tests.
- Run real PaddleOCR only in manual smoke until dependency size and runtime are
  understood on the target server.

Do not add OCR dependencies to the default install until server cost, model
download behavior, and startup time are verified.

## Proposed Data Additions

### KnowledgeCard

Fields:

- `id`
- `document_id`
- `source_chunk_id`
- `title`
- `tag`
- `content`
- `source_filename`
- `source_section_title`
- `source_section_path`
- `page_start`
- `page_end`
- `confidence`
- `metadata`

### TenderAnalysis

Fields:

- `document_id`
- `project_requirements`
- `scoring_items`
- `disqualification_risks`
- `raw_text_summary`
- `analysis_method`
- `need_human_review`

### OCRPageText

Fields:

- `document_id`
- `page_number`
- `text`
- `confidence`
- `engine`
- `blocks`
- `metadata`

## Verification Matrix

| Area | Automated | Manual smoke |
| --- | --- | --- |
| Knowledge card build | fake parsed sections/chunks | small historical bid `.docx` |
| Tender analysis | deterministic text fixtures | small tender `.docx` |
| OCR adapter | fake OCR adapter | small scanned PDF or image |
| Generation | fake LLM | optional real user-provided LLM key |
| Demo page | static hooks + API tests | browser walkthrough |
| Bash script | only where shell exists | record WSL blocker on Windows |

## Server Demo File Recommendation

Start with:

1. `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
2. `宁波运维项目\牧鸿\省人事工资管理系统-宁波人社运维-资格证明文件.docx`
3. `KSDQZFCG（GK）2026-64...项目（二次）.docx`

Use scanned/image material only after Phase 8 is implemented:

- `宁波运维项目\九州拓新\批量输出为图片\...`
- `宁波运维项目\浙江速微科技有限公司\批量输出为图片\...`

Avoid first:

- 18 MB, 37 MB, 194 MB `.docx` files.
- 229 MB archive.
- Legacy `.doc` until conversion behavior is verified.

## Key Risks

1. OCR dependencies may be heavy and model downloads may fail on the target
   server.
2. OCR text may be noisy; all OCR-derived generation must remain high scrutiny.
3. PRD tags are business-facing; bad tag rules can make the demo look worse than
   raw retrieval.
4. Tender risk extraction can be overclaimed. Keep rule-based evidence visible.
5. Semantic retrieval is still deferred. If the demo needs long natural-language
   queries, Qdrant/Haystack or improved lexical matching must be added later.

## Recommended Next Implementation Order

1. Phase 9 real PaddleOCR runtime and scanned PDF smoke.
2. Phase 10 PRD-shaped demo page.
3. Phase 11 sample outputs and runbook.
4. Phase 12 semantic retrieval adapter spike.

Do not implement OCR before the knowledge-card and tender-analysis shape is
clear unless the server demo specifically depends on scanned sample files.
