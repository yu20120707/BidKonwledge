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
  "tables_count": 2,
  "parse_status": "success"
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

Retrieve knowledge cards.

Request:

```json
{
  "query": "生成运维服务实施方案",
  "tag": "运维服务实施方案",
  "top_k": 5
}
```

Response:

```json
{
  "cards": []
}
```

## POST /api/generate

Generate candidate content.

Request:

```json
{
  "tender_document_id": "string",
  "target_tag": "运维服务实施方案",
  "query": "根据招标要求生成运维服务实施方案",
  "top_k": 5
}
```

Response:

```json
{
  "target_tag": "运维服务实施方案",
  "generated_content": "string",
  "citations": [],
  "risks": [],
  "need_human_review": true
}
```

## GET /demo

Minimal demo page.

This endpoint is not part of Phase 1.
