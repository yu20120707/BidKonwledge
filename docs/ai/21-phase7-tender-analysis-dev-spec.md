# Phase 7 Tender Analysis Dev Spec

## Purpose

Phase 7 makes the tender-file side of the lightweight PRD visible. After a
tender document is uploaded and parsed, the backend should produce a
source-traceable analysis with project requirements, scoring items, and
disqualification risks.

Status: implemented on 2026-06-28.

## User Story

As a demo operator, after uploading and parsing a tender file, I can run tender
analysis and inspect requirements, scoring items, and disqualification risks so
that later generation can use tender-side evidence instead of only a free-form
query.

## In Scope

1. Analyze parsed `tender` documents.
2. Persist the latest analysis for a tender document.
3. Provide analyze and get APIs.
4. Extract deterministic evidence items:
   - project requirements
   - scoring items
   - disqualification risks
5. Preserve source traceability.
6. Return `need_human_review = true`.
7. Support deterministic re-analysis for a document.

## Out Of Scope

1. OCR or PaddleOCR.
2. LLM-based tender interpretation.
3. Legal/compliance decisioning.
4. Complete tender understanding.
5. Vector retrieval, Qdrant, Haystack, or embeddings.
6. User system.
7. Demo page redesign.
8. Word/PDF export.

## Data Contract

### TenderEvidenceItem

Fields:

- `item_id`: string
- `item_type`: `requirement | scoring_item | disqualification_risk`
- `title`: string
- `description`: string
- `source_filename`: string
- `severity`: optional string for risks
- `score`: optional float for scoring items
- `source_chunk_id`: string
- `source_section_title`: string
- `source_section_path`: string
- `page_start`: optional int
- `page_end`: optional int
- `matched_keywords`: list[string]

### TenderAnalysisRecord

Fields:

- `id`: string
- `document_id`: string
- `project_requirements_json`: JSON list of `TenderEvidenceItem`
- `scoring_items_json`: JSON list of `TenderEvidenceItem`
- `disqualification_risks_json`: JSON list of `TenderEvidenceItem`
- `raw_text_summary`: string
- `analysis_method`: string
- `need_human_review`: bool
- `metadata_json`: dict
- `created_at`: string

### TenderAnalysisResponse

Fields:

- `document_id`
- `project_requirements`
- `scoring_items`
- `disqualification_risks`
- `raw_text_summary`
- `analysis_method`
- `need_human_review`
- `metadata`

## Storage Contract

Add a SQLite table:

```sql
CREATE TABLE IF NOT EXISTS tender_analyses (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL UNIQUE,
    project_requirements_json TEXT NOT NULL,
    scoring_items_json TEXT NOT NULL,
    disqualification_risks_json TEXT NOT NULL,
    raw_text_summary TEXT NOT NULL,
    analysis_method TEXT NOT NULL,
    need_human_review INTEGER NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE
)
```

Re-analysis rule:

1. Delete or replace the existing analysis for the document.
2. Insert the new analysis in one transaction.
3. Keep item order deterministic by source chunk order.

## API Contract

### POST /api/tender/analyze

Request:

```json
{
  "document_id": "string"
}
```

Success:

```json
{
  "document_id": "string",
  "project_requirements": [],
  "scoring_items": [],
  "disqualification_risks": [],
  "raw_text_summary": "string",
  "analysis_method": "deterministic_tender_v1",
  "need_human_review": true,
  "metadata": {
    "source_chunks_count": 3
  }
}
```

Errors:

- `DOCUMENT_NOT_FOUND`
- `DOCUMENT_NOT_PARSED`
- `UNSUPPORTED_DOCUMENT_ROLE`

### GET /api/documents/{document_id}/tender-analysis

Success returns the same shape as the analyze response.

Errors:

- `DOCUMENT_NOT_FOUND`
- `TENDER_ANALYSIS_NOT_FOUND`

## Initial Rule Ideas

Project requirement keywords:

- 需求
- 服务内容
- 项目内容
- 建设内容
- 运维
- 实施

Scoring item keywords:

- 评分
- 分值
- 得分
- 评审
- 评分标准
- 技术分
- 商务分

Disqualification risk keywords:

- 废标
- 无效投标
- 否决
- 不接受
- 不符合
- 资格审查
- 必须
- 不得

These rules are intentionally conservative. Phase 7 should extract evidence and
flag human review, not decide legal compliance.

## Acceptance Criteria

1. Parsed tender chunks can produce a tender analysis.
2. Analysis can be retrieved by document.
3. Re-analysis replaces existing analysis deterministically.
4. Unsupported `historical_bid` documents are rejected.
5. Source evidence is preserved for each extracted item.
6. Boundary tests prove no OCR/vector/LLM dependency.
