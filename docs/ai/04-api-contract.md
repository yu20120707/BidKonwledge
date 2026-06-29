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

Optional request body:

```json
{
  "parse_mode": "auto"
}
```

`parse_mode` values:

- `auto`: default when the body is omitted. Existing parser first; PDF can
  fallback to OCR.
- `text`: existing parser only; OCR disabled.
- `ocr`: OCR only for PDF in Phase 8B.

Response:

```json
{
  "document_id": "string",
  "sections_count": 10,
  "chunks_count": 20,
  "parse_status": "parsed",
  "error_message": null,
  "parse_metadata": {}
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
  "chunks_count": 20,
  "parse_metadata": {}
}
```

Phase 8A parse metadata can include:

- `original_extension`
- `detected_format`
- `is_mislabeled`
- `requires_conversion`
- `conversion_required`
- `conversion_method`
- `converted_path`

`converted_path` is a relative internal path when present. API responses must
not expose absolute local paths.

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

Convert parsed historical bid chunks into knowledge cards.

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

Errors:

- `DOCUMENT_NOT_FOUND`
- `DOCUMENT_NOT_PARSED`
- `UNSUPPORTED_DOCUMENT_ROLE`

## GET /api/documents/{document_id}/knowledge-cards

Return persisted knowledge cards for a document.

Response:

```json
{
  "document_id": "string",
  "cards": [
    {
      "card_id": "string",
      "document_id": "string",
      "source_chunk_id": "string",
      "title": "运维服务实施方案",
      "tag": "运维服务实施方案",
      "content": "string",
      "source_filename": "knowledge.docx",
      "source_section_title": "运维服务实施方案",
      "source_section_path": "运维服务实施方案",
      "page_start": 1,
      "page_end": 2,
      "confidence": 0.8,
      "metadata": {
        "tagger": "prd_deterministic_v1",
        "matched_keywords": ["运维"],
        "source_chunk_metadata": {}
      },
      "created_at": "2026-06-28T12:00:00Z"
    }
  ]
}
```

Phase 6 only builds cards for `historical_bid` documents with
`parse_status = parsed`. It does not call OCR, Qdrant, Haystack, embeddings, or
LLM services.

## POST /api/tender/analyze

Analyze a parsed tender document.

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
  "project_requirements": [],
  "scoring_items": [],
  "disqualification_risks": [],
  "raw_text_summary": "string",
  "analysis_method": "deterministic_tender_v1",
  "need_human_review": true,
  "metadata": {}
}
```

Errors:

- `DOCUMENT_NOT_FOUND`
- `DOCUMENT_NOT_PARSED`
- `UNSUPPORTED_DOCUMENT_ROLE`

## GET /api/documents/{document_id}/tender-analysis

Return the latest persisted tender analysis for a document.

Response shape is the same as `POST /api/tender/analyze`.

Errors:

- `DOCUMENT_NOT_FOUND`
- `TENDER_ANALYSIS_NOT_FOUND`

Phase 7 only analyzes `tender` documents with `parse_status = parsed`. It does
not call OCR, Qdrant, Haystack, embeddings, or LLM services.

## Phase 8A Parse-Time Word Conversion

`POST /api/documents/{document_id}/parse` detects file content format before
calling the parser.

Supported Phase 8A behavior:

1. True `.docx` ZIP content parses directly.
2. Text-based `.pdf` parses directly with OCR disabled.
3. Legacy OLE Word `.doc` content, including `.docx` files mislabeled over OLE
   content, is converted to a derived `.docx` file before Docling parsing when
   the Word converter is available.

Converter-unavailable or converter-failure cases return normal parse responses
with `parse_status = failed`, sanitized `error_message`, and safe
`parse_metadata`.

Phase 8A does not add OCR/PaddleOCR or semantic parsing.

## Phase 8B OCR Parse Adapter

`POST /api/documents/{document_id}/parse` supports OCR through `parse_mode`.

Behavior:

1. Missing body remains backward compatible and defaults to `auto`.
2. `auto` keeps Docling-first parsing and may fallback to OCR for PDF if the
   text parser fails or produces no chunks.
3. `text` never calls OCR.
4. `ocr` calls the OCR adapter directly for PDF in this phase.
5. OCR errors are returned as normal parse failures with sanitized messages.

Automated tests use fake OCR adapters and do not require PaddleOCR.

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
deterministic over parsed historical-bid SQLite chunks and knowledge-card
source-chunk tags. Tender documents are excluded from the retrieval evidence
pool. It does not call Qdrant, Haystack, embeddings, or LLM services.

## POST /api/generate

Generate candidate content.

Request:

```json
{
  "target_tag": "运维服务",
  "query": "根据招标要求生成运维服务应急方案",
  "top_k": 5,
  "llm_config": {
    "api_key": "user-provided-key",
    "base_url": "https://api.openai.com/v1",
    "model": "gpt-4o-mini"
  }
}
```

`llm_config` is optional. If present, it is used only for this request and the
API key must not be returned in responses or persisted. Request-scoped
`base_url` must be HTTPS.

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

Phase 12 closeout note:

- The demo page may combine the user's generation query with the first analyzed
  tender requirement before calling this endpoint. This preserves the existing
  request schema while making the tender-analysis context visible to the
  generation prompt.
- When retrieval context came through a PRD knowledge-card tag, the internal
  prompt includes optional `knowledge_card_tag`, `knowledge_card_title`, and
  `knowledge_card_confidence` lines. The public response schema stays citation
  based and unchanged.

## GET /demo

Minimal demo page.

This endpoint is not part of Phase 1.
