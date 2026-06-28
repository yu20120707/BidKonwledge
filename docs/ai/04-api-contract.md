# API Contract

## GET /health

Health check.

Response:

```json
{
  "status": "ok"
}
```

## POST /api/files/upload

Upload a historical bid file or a tender file.

Parameters:

- `file`: UploadFile
- `doc_role`: `historical_bid | tender`

Success response:

```json
{
  "document_id": "string",
  "original_filename": "string",
  "doc_role": "historical_bid",
  "parse_status": "pending",
  "file_size": 123,
  "created_at": "2026-06-27T12:00:00Z"
}
```

Success status: `201 Created`

Error response:

```json
{
  "error_code": "INVALID_DOC_ROLE",
  "message": "Unsupported document role",
  "details": {}
}
```

Phase 1 error codes: `MISSING_FILE`, `MISSING_DOC_ROLE`, `INVALID_DOC_ROLE`, `EMPTY_FILE`, `UNSAFE_FILENAME`, `FILE_TOO_LARGE`, `UNSUPPORTED_FILE_TYPE`, `FILE_WRITE_FAILED`, `METADATA_WRITE_FAILED`.

## POST /api/documents/{document_id}/parse

Parse a document.

Response:

```json
{
  "document_id": "string",
  "sections_count": 10,
  "chunks_count": 20,
  "parse_status": "parsed",
  "error_message": null
}
```

Phase 2 status values are `pending`, `parsing`, `parsed`, and `failed`.

## GET /api/documents/{document_id}

Return document metadata and current parse counts.

Response:

```json
{
  "document_id": "string",
  "original_filename": "string",
  "doc_role": "historical_bid",
  "file_ext": ".docx",
  "file_size": 123,
  "parse_status": "parsed",
  "error_message": null,
  "created_at": "2026-06-27T12:00:00Z",
  "updated_at": "2026-06-27T12:01:00Z",
  "sections_count": 10,
  "chunks_count": 20
}
```

## GET /api/documents/{document_id}/chunks

Return persisted normalized chunks for a document.

Response:

```json
{
  "document_id": "string",
  "chunks": [
    {
      "chunk_id": "string",
      "document_id": "string",
      "section_id": "string",
      "section_title": "运维服务方案",
      "section_path": "运维服务方案",
      "order_index": 0,
      "chunk_index": 0,
      "chunk_type": "text",
      "text": "string",
      "tags": ["运维服务"],
      "page_start": null,
      "page_end": null,
      "metadata": {
        "section_level": 1,
        "tagger": "deterministic_v1"
      }
    }
  ]
}
```

## POST /api/knowledge/build

Convert historical bid sections into knowledge cards.

Request:

```json
{
  "document_id": "string"
}
```

Response:

```json
{
  "document_id": "string",
  "cards_count": 20,
  "tags": ["运维服务实施方案", "突发应急方案和措施"]
}
```

## POST /api/tender/analyze

Analyze a new tender document.

Request:

```json
{
  "document_id": "string"
}
```

Response:

```json
{
  "project_requirements": [],
  "scoring_items": [],
  "disqualification_risks": []
}
```

## POST /api/retrieve

Retrieve persisted chunks.

Request:

```json
{
  "query": "应急",
  "tag": "运维服务",
  "top_k": 5
}
```

Response:

```json
{
  "query": "应急",
  "tag": "运维服务",
  "results": [
    {
      "chunk_id": "string",
      "document_id": "string",
      "section_id": "string",
      "section_title": "运维服务应急",
      "section_path": "运维服务应急",
      "text": "string",
      "tags": ["运维服务", "应急响应"],
      "score": 2.0,
      "source": {
        "original_filename": "retrieval.docx",
        "doc_role": "historical_bid",
        "file_ext": ".docx",
        "page_start": null,
        "page_end": null,
        "chunk_metadata": {
          "tagger": "deterministic_v1"
        }
      }
    }
  ]
}
```

Phase 3 requires at least one of `query` or `tag`. Retrieval is local and
deterministic over Phase 2 SQLite chunks. It does not call Qdrant, Haystack,
embeddings, or LLM services.

## POST /api/generate

Generate candidate content.

Request:

```json
{
  "target_tag": "运维服务",
  "query": "根据招标要求生成运维服务应急方案",
  "top_k": 5
}
```

Response:

```json
{
  "target_tag": "运维服务",
  "generated_content": "string",
  "citations": [
    {
      "source_filename": "generation.docx",
      "source_section_title": "运维服务应急",
      "content_snippet": "运维服务支持应急响应，包含突发事件处理和服务保障。",
      "chunk_id": "string",
      "document_id": "string"
    }
  ],
  "risks": [
    {
      "risk_type": "MISSING_CITATIONS",
      "description": "No retrieval citations are available for this output.",
      "severity": "high",
      "source_text": null
    }
  ],
  "need_human_review": true
}
```

Phase 4 uses Phase 3 retrieval context, an injectable LLM adapter, citation
formatting, and rule-based risk checks. Automated tests use a fake LLM and do
not require real external LLM credentials.

## GET /demo

Minimal demo page.

This endpoint is not part of Phase 1.
