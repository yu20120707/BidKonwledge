# Phase 1 API And Persistence Details

## API Surface

Phase 1 implements only:

1. `GET /health`
2. `POST /api/files/upload`

All other API contracts in `docs/ai/04-api-contract.md` are future-phase contracts.

## GET /health

Response status: `200 OK`

Response body:

```json
{
  "status": "ok"
}
```

No database or external dependency check is required in Phase 1.

## POST /api/files/upload

Request:

- `multipart/form-data`
- `file`: uploaded file
- `doc_role`: one of `historical_bid`, `tender`

Success response status: `201 Created`

Success response body:

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

Error response body:

```json
{
  "error_code": "INVALID_DOC_ROLE",
  "message": "Unsupported document role",
  "details": {}
}
```

Required Phase 1 error codes:

| Scenario | HTTP status | `error_code` |
| --- | --- | --- |
| Missing file | `400 Bad Request` | `MISSING_FILE` |
| Missing `doc_role` | `400 Bad Request` | `MISSING_DOC_ROLE` |
| Invalid `doc_role` | `400 Bad Request` | `INVALID_DOC_ROLE` |
| Empty file | `400 Bad Request` | `EMPTY_FILE` |
| Unsafe filename | `400 Bad Request` | `UNSAFE_FILENAME` |
| File too large | `413 Payload Too Large` | `FILE_TOO_LARGE` |
| Unsupported file extension | `400 Bad Request` | `UNSUPPORTED_FILE_TYPE` |
| File write failure | `500 Internal Server Error` | `FILE_WRITE_FAILED` |
| Metadata write failure | `500 Internal Server Error` | `METADATA_WRITE_FAILED` |

## Upload Rules

Phase 1 should:

1. Save files under `data/uploads`.
2. Generate a server-side document id.
3. Generate the stored filename on the backend, for example `<document_id><safe_extension>`.
4. Preserve the original filename in metadata.
5. Reject missing file input.
6. Reject missing or invalid `doc_role`.
7. Reject empty files.
8. Reject path traversal filenames.
9. Reject unsupported extensions: `.exe`, `.bat`, `.cmd`, `.ps1`, and other executable-like uploads.
10. Return the structured JSON error shape above.
11. Avoid trusting extension or MIME type as proof of safe content; Phase 1 stores bytes but does not parse them.

Allowed Phase 1 extensions are:

```text
.txt
.pdf
.doc
.docx
```

If Phase 1 implements a configurable max upload size, the default should be documented in README and tests should override it with a small test limit.

Do not implement content parsing.

## Atomicity Rules

Upload persistence must avoid inconsistent file/database state:

1. If request validation fails, do not write a file and do not insert metadata.
2. If file write fails, do not insert metadata.
3. If database insert fails after file write, delete the stored file before returning the error.
4. If cleanup after database failure also fails, return `METADATA_WRITE_FAILED` and log the cleanup failure without exposing local absolute paths in the response.
5. Original filenames are metadata only; never use them as stored filenames.

## Document Metadata

SQLite table: `documents`

Required fields:

| Column | Type | Notes |
| --- | --- | --- |
| `id` | text primary key | server-generated id |
| `original_filename` | text | original filename from upload metadata |
| `stored_filename` | text | backend-generated filename |
| `stored_path` | text | relative path under upload root |
| `file_ext` | text | normalized lower-case extension |
| `content_type` | text nullable | client-provided MIME type, stored for reference only |
| `file_size` | integer | uploaded byte length |
| `doc_role` | text | `historical_bid` or `tender` |
| `created_at` | text | ISO-8601 timestamp |
| `updated_at` | text | ISO-8601 timestamp |
| `parse_status` | text | default `pending` |
| `error_message` | text nullable | default null |

## Status Rules

Initial upload status:

```text
parse_status = pending
```

Phase 1 does not transition documents to `success` or `failed` because parsing is not implemented.

## Security Notes

1. Normalize or replace storage filenames to avoid path traversal.
2. Store uploads only inside configured upload root.
3. Do not execute or parse uploaded files in Phase 1.
4. Do not log file contents.
5. Do not copy external sample directories into repository history.
6. Do not return absolute local filesystem paths in public API responses.
