# Phase 6 Knowledge Cards Dev Spec

## Purpose

Phase 6 closes the first major gap between the current backend chain and the
lightweight PRD: historical bid content must become visible as knowledge cards,
not only raw chunks.

Status: implemented on 2026-06-28.

This phase remains deterministic and backend-first. It prepares the
data layer used by later tender analysis, demo flow, and retrieval improvements.

## User Story

As a demo operator, after uploading and parsing a historical bid file, I can
build knowledge cards and inspect cards by document so that the demo can show
PRD-style historical knowledge before generating candidate content.

## In Scope

1. Build knowledge cards from parsed chunks for historical bid documents.
2. Persist knowledge cards in SQLite.
3. Provide build and list APIs.
4. Add PRD-aligned deterministic tags.
5. Preserve source traceability.
6. Support deterministic rebuild for a document.

## Out Of Scope

1. OCR or PaddleOCR.
2. Tender analysis.
3. Vector retrieval.
4. Semantic embeddings.
5. Qdrant or Haystack.
6. User system.
7. Demo page redesign.
8. Word/PDF export.

## Data Contract

### KnowledgeCardRecord

Fields:

- `id`: string
- `document_id`: string
- `source_chunk_id`: string
- `title`: string
- `tag`: string
- `content`: string
- `source_filename`: string
- `source_section_title`: string
- `source_section_path`: string
- `page_start`: optional int
- `page_end`: optional int
- `confidence`: float
- `metadata`: dict
- `created_at`: string

### KnowledgeCardResponse

Return the same business fields, using `card_id` instead of raw `id`.

### KnowledgeBuildResponse

Fields:

- `document_id`
- `cards_count`
- `tags`

## Storage Contract

Add a SQLite table:

```sql
CREATE TABLE IF NOT EXISTS knowledge_cards (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    source_chunk_id TEXT NOT NULL,
    title TEXT NOT NULL,
    tag TEXT NOT NULL,
    content TEXT NOT NULL,
    source_filename TEXT NOT NULL,
    source_section_title TEXT NOT NULL,
    source_section_path TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    confidence REAL NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY(source_chunk_id) REFERENCES document_chunks(id) ON DELETE CASCADE
)
```

Rebuild rule:

1. Delete existing cards for the document.
2. Insert newly generated cards in one transaction.
3. Keep ordering deterministic by chunk order.

## API Contract

### POST /api/knowledge/build

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
  "cards_count": 2,
  "tags": ["运维服务实施方案", "突发应急方案和措施"]
}
```

Errors:

- `DOCUMENT_NOT_FOUND`
- `DOCUMENT_NOT_PARSED`
- `UNSUPPORTED_DOCUMENT_ROLE`

### GET /api/documents/{document_id}/knowledge-cards

Success:

```json
{
  "document_id": "string",
  "cards": [
    {
      "card_id": "string",
      "document_id": "string",
      "source_chunk_id": "string",
      "title": "运维服务应急",
      "tag": "突发应急方案和措施",
      "content": "string",
      "source_filename": "demo.docx",
      "source_section_title": "运维服务应急",
      "source_section_path": "运维服务应急",
      "page_start": 1,
      "page_end": 2,
      "confidence": 0.8,
      "metadata": {
        "tagger": "prd_deterministic_v1"
      }
    }
  ]
}
```

Errors:

- `DOCUMENT_NOT_FOUND`

## Tagging Rules

Initial PRD tags should be deterministic keyword rules:

| Tag | Example keywords |
| --- | --- |
| `运维服务实施方案` | 运维, 维护, 服务, 实施 |
| `突发应急方案和措施` | 应急, 突发, 响应, 故障 |
| `网络和数据安全防护保障措施` | 网络安全, 数据安全, 安全, 防护, 保密 |
| `服务质量保障和考核评估方案` | 质量, 考核, 评估, SLA, 保障 |
| `团队人员` | 团队, 人员, 项目经理, 工程师 |
| `业绩情况` | 业绩, 案例, 合同, 客户 |
| `资格材料` | 营业执照, 资格, 承诺函, 中小企业 |
| `商务报价` | 报价, 价格, 费用 |
| `未分类` | fallback |

If multiple tags match, Phase 6 can create one card per best tag or one card per
matched tag. Prefer one card per best tag for the first implementation unless
tests require multi-tag cards.

## Source Traceability

Every card must retain:

1. Document id.
2. Source chunk id.
3. Source filename.
4. Section title and path.
5. Page fields if available.
6. Tagger metadata.

## Acceptance Criteria

1. Parsed historical bid chunks build cards.
2. Cards can be listed by document.
3. Rebuild is deterministic and replaces old cards.
4. Source traceability is present.
5. PRD-style tags appear on expected content.
6. Boundary tests prove no OCR/vector/LLM dependency.

## Implementation Notes

Use simple deterministic logic first. Do not add abstractions for multiple card
builders until a real second implementation exists.
