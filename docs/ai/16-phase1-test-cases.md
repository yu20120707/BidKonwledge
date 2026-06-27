# Phase 1 Test Spec v0.1

## Purpose

This document is the internal acceptance test specification for the Phase 1 backend foundation.

It is suitable for developers and agents implementing Phase 1 tests. It is not a customer-facing PRD and not a full Demo acceptance document.

Phase 1 verifies only:

1. FastAPI application startup.
2. `GET /health`.
3. `POST /api/files/upload`.
4. Local file persistence.
5. SQLite metadata persistence.
6. Configuration isolation.
7. Windows-local smoke workflow.

Phase 1 is not the customer-facing knowledge-base Demo. Passing Phase 1 does not mean the product can yet demonstrate OCR, document parsing, knowledge cards, retrieval, generation, source tracing, risk prompts, or frontend Demo workflows.

## Scope Boundary

In scope:

1. Backend foundation tests.
2. Upload API contract tests.
3. File-storage safety tests.
4. SQLite metadata tests.
5. Local script and manual smoke evidence.

Out of scope:

1. OCR.
2. LLM calls.
3. Embeddings.
4. Qdrant or any vector database.
5. Haystack pipeline execution.
6. Knowledge-card generation.
7. Tender-file analysis.
8. Frontend Demo page.
9. User accounts.
10. Word/PDF export.
11. Customer-facing PRD validation.

## Test Environment Assumptions

1. Run tests from the repository root, not from a hard-coded absolute path.
2. Primary shell is Windows PowerShell.
3. Tests should run without WSL.
4. Python should be 3.11 or newer unless Phase 1 selects a stricter version.
5. The FastAPI app entrypoint should be importable by tests.
6. Automated tests must use isolated temporary paths for upload storage and SQLite database files.
7. Automated tests must not write to real source-material folders.
8. Automated tests must not require external services or internet access.
9. Localhost smoke checks should use `curl.exe --noproxy "*"` on this machine.

## Expected Test File Layout

Phase 1 should create a focused automated test suite:

```text
backend/tests/
|-- test_health.py
|-- test_upload_contract.py
|-- test_upload_validation.py
|-- test_storage.py
|-- test_database.py
`-- test_phase1_boundaries.py
```

Files may be merged if the implementation is small, but the coverage areas must remain visible.

Harness commands such as `ai-status`, `ai-doctor`, and `scripts/ai_check.ps1` are delivery checks, not core business pytest assertions.

## Required Test Fixtures

Use pytest fixtures for isolation:

| Fixture | Purpose |
| --- | --- |
| `tmp_path` | Temporary upload directory and SQLite database path. |
| `test_settings` | Settings override for upload root, database path, and optional upload limits. |
| `client` | FastAPI `TestClient` bound to the app with test settings. |
| `sample_text_file` | Small upload payload such as `hello bid knowledge`. |
| `empty_file` | Zero-byte file for negative validation. |
| `unsafe_filename` | Filename such as `../evil.txt` or `..\\evil.txt`. |
| `unicode_filename` | Filename such as `投标 测试 文件.txt`. |
| `duplicate_filename_files` | Two files with the same original filename and different byte content. |

The implementation must expose settings in a way tests can override without changing global developer-machine state.

## Test Data Rules

Use synthetic files for automated tests.

Allowed automated fixtures:

1. Small `.txt` files.
2. Small `.pdf` or `.docx` fixtures only if generated locally and committed intentionally.
3. In-memory bytes created inside tests.

Do not use:

1. Large customer-provided sample files.
2. Files from `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`.
3. Files copied from reference repositories.
4. Network downloads.

## Phase 1 API Contract

### Upload Endpoint

Endpoint:

```text
POST /api/files/upload
```

Content type:

```text
multipart/form-data
```

Form fields:

| Field | Required | Allowed value |
| --- | --- | --- |
| `file` | yes | uploaded file |
| `doc_role` | yes | `historical_bid` or `tender` |

Allowed Phase 1 file extensions:

```text
.txt
.pdf
.doc
.docx
```

Success status:

```text
201 Created
```

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

The success response must not expose absolute local filesystem paths.

Error response:

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

### Health Endpoint

Endpoint:

```text
GET /health
```

Success response:

```json
{
  "status": "ok"
}
```

`GET /health` is a shallow app-health endpoint in Phase 1. It must not require SQLite, OCR, LLM, Qdrant, Haystack, or internet access.

## SQLite Contract

Table:

```text
documents
```

Required fields:

| Column | Type | Required | Notes |
| --- | --- | --- | --- |
| `id` | text primary key | yes | server-generated document id |
| `original_filename` | text | yes | original filename from upload metadata |
| `stored_filename` | text | yes | backend-generated filename |
| `stored_path` | text | yes | relative path under upload root |
| `file_ext` | text | yes | normalized lower-case extension |
| `content_type` | text nullable | no | client-provided MIME type, reference only |
| `file_size` | integer | yes | uploaded byte length |
| `doc_role` | text | yes | `historical_bid` or `tender` |
| `created_at` | text | yes | ISO-8601 timestamp |
| `updated_at` | text | yes | ISO-8601 timestamp |
| `parse_status` | text | yes | default `pending` |
| `error_message` | text nullable | no | default null |

Phase 1 only creates rows with `parse_status = pending`.

## File Safety Rules

1. Stored filename must be generated by the backend, for example `<document_id><safe_extension>`.
2. Original filename is preserved only as metadata.
3. User-provided filenames must never be used as direct storage paths.
4. Stored files must resolve under the configured upload root.
5. Path traversal filenames must be rejected or fully neutralized before storage.
6. Duplicate original filenames must not overwrite stored files.
7. Extension checks are a basic Phase 1 gate, not proof that content is safe.
8. Phase 1 stores bytes and metadata only; it does not parse or execute uploaded files.
9. If validation fails, no file and no metadata row should remain.
10. If file write fails, no metadata row should be inserted.
11. If metadata insert fails after file write, the stored file must be cleaned up.

## Priority Levels

| Priority | Meaning |
| --- | --- |
| P0 | Must pass before Phase 1 can be called complete. |
| P1 | Should pass before Phase 1 handoff; required if the related code exists. |
| P2 | Useful hardening; may be deferred only with an explicit note in `.ai/verification.md`. |

## Automated Test Cases

### Health Endpoint

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-HEALTH-001 | P0 | Health endpoint returns stable shallow status. | App is importable in test mode. | Send `GET /health`. | HTTP 200. Response JSON is exactly `{"status": "ok"}`. |
| TC-HEALTH-002 | P0 | Health endpoint has no external dependency. | Qdrant, OCR, LLM, internet, and parser tools are unavailable. | Send `GET /health`. | HTTP 200. No attempt to initialize external services. |
| TC-HEALTH-003 | P1 | Health response content type is JSON. | App is running. | Send `GET /health`. | `content-type` includes `application/json`. |

### Upload Success Contract

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-UPLOAD-001 | P0 | Upload accepts historical bid role. | Test client uses temp upload dir and temp SQLite DB. | POST `/api/files/upload` with `doc_role=historical_bid` and small `.txt` file. | HTTP `201 Created`. Response follows the documented success JSON contract. |
| TC-UPLOAD-002 | P0 | Upload accepts tender role. | Same as TC-UPLOAD-001. | POST `/api/files/upload` with `doc_role=tender` and small `.txt` file. | HTTP `201 Created`. Response `doc_role` is `tender`. |
| TC-UPLOAD-003 | P0 | Upload response has required fields. | Valid upload succeeds. | Inspect response JSON. | Fields exist: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`. |
| TC-UPLOAD-004 | P0 | Upload response uses fixed pending parse status. | Valid upload succeeds. | Inspect response JSON. | `parse_status` is exactly `pending`. |
| TC-UPLOAD-005 | P0 | Upload response does not expose absolute paths. | Valid upload succeeds. | Inspect response JSON values. | No value contains the local upload root or drive-qualified path. |
| TC-UPLOAD-006 | P1 | Upload supports Chinese and spaces in original filename. | Unicode filename fixture exists. | POST `投标 测试 文件.txt`. | HTTP `201 Created`. `original_filename` is preserved. Stored filename remains backend-generated. |

### Upload Validation And Errors

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-ERR-001 | P0 | Missing file is rejected. | App is running in test mode. | POST with `doc_role=historical_bid` and no file field. | HTTP 400. Error JSON has `error_code=MISSING_FILE`. No file or metadata row remains. |
| TC-ERR-002 | P0 | Missing doc role is rejected. | App is running in test mode. | POST with a file and no `doc_role`. | HTTP 400. Error JSON has `error_code=MISSING_DOC_ROLE`. No file or metadata row remains. |
| TC-ERR-003 | P0 | Invalid doc role is rejected. | App is running in test mode. | POST with `doc_role=unknown` and a small file. | HTTP 400. Error JSON has `error_code=INVALID_DOC_ROLE`. No file or metadata row remains. |
| TC-ERR-004 | P0 | Empty file is rejected. | Empty file fixture exists. | POST zero-byte file with valid `doc_role`. | HTTP 400. Error JSON has `error_code=EMPTY_FILE`. No file or metadata row remains. |
| TC-ERR-005 | P0 | Unsafe filename is rejected. | Unsafe filename fixture exists. | POST a file named `../evil.txt` or `..\\evil.txt`. | HTTP 400. Error JSON has `error_code=UNSAFE_FILENAME`, or request succeeds only if storage proves no path escape. Preferred Phase 1 behavior is rejection. |
| TC-ERR-006 | P0 | Unsupported file extension is rejected. | `.exe` fixture exists. | POST `payload.exe`. | HTTP 400. Error JSON has `error_code=UNSUPPORTED_FILE_TYPE`. No file or metadata row remains. |
| TC-ERR-007 | P1 | Oversized upload is rejected when max size is configured. | Test settings set small max upload size. | POST file larger than configured max. | HTTP 413. Error JSON has `error_code=FILE_TOO_LARGE`. No file or metadata row remains. |
| TC-ERR-008 | P1 | Error response shape is stable. | Any invalid request is sent. | Inspect error JSON. | Response contains `error_code`, `message`, and `details`. |

### File Storage

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-STORAGE-001 | P0 | Upload directory is created if missing. | Temp upload root does not exist before upload. | Perform valid upload. | Upload root is created automatically. |
| TC-STORAGE-002 | P0 | Stored file bytes match uploaded bytes. | Valid upload succeeds. | Read stored file from test upload root. | Stored bytes equal request bytes. |
| TC-STORAGE-003 | P0 | Stored file remains under configured upload root. | Valid upload succeeds. | Resolve stored path. | Resolved path starts with configured upload root. |
| TC-STORAGE-004 | P0 | Stored filename is backend-generated. | Valid upload succeeds. | Inspect metadata row. | `stored_filename` is not the raw original filename and includes a generated identifier or equivalent safe name. |
| TC-STORAGE-005 | P1 | Duplicate original filenames do not overwrite files. | Two files with same original filename exist. | Upload both files. | Both requests succeed. Stored filenames are distinct. Metadata has two rows. Stored bytes for both files are correct. |
| TC-STORAGE-006 | P1 | Failed validation leaves no orphan file. | Invalid role, empty file, or unsupported extension request is sent. | Inspect upload root after response. | No unexpected file remains. |

### SQLite Persistence

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-DB-001 | P0 | SQLite database initializes. | Temp DB path points to a non-existing file. | Start app or perform first valid upload. | Database file is created. `documents` table exists. |
| TC-DB-002 | P0 | Valid upload inserts one metadata row. | Temp DB is empty. | Perform valid upload. | Exactly one row is inserted for the uploaded document. |
| TC-DB-003 | P0 | Metadata row stores required fields. | Valid upload succeeds. | Query metadata row. | Required columns exist and are populated: `id`, `original_filename`, `stored_filename`, `stored_path`, `file_ext`, `file_size`, `doc_role`, `created_at`, `updated_at`, `parse_status`. |
| TC-DB-004 | P0 | Nullable metadata defaults are safe. | Valid upload succeeds. | Query metadata row. | `content_type` may be null or client value; `error_message` is null. |
| TC-DB-005 | P0 | Parse status remains pending. | Valid upload succeeds. | Query metadata row. | `parse_status` is exactly `pending`; no parser output is required. |
| TC-DB-006 | P0 | Failed upload does not insert metadata row. | Temp DB is empty. | Send invalid upload request. | Row count remains zero. |
| TC-DB-007 | P1 | Multiple uploads create multiple rows. | Temp DB is empty. | Upload two valid files. | Two distinct document ids and two rows exist. |

### Atomicity And Cleanup

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-ATOMIC-001 | P0 | File write failure does not insert metadata. | Storage layer can be forced to fail or upload root is made unwritable in a controlled test. | Perform upload. | Error JSON has `error_code=FILE_WRITE_FAILED`. No metadata row is inserted. |
| TC-ATOMIC-002 | P1 | Metadata write failure cleans up written file. | Database layer can be forced to fail after file write. | Perform upload. | Error JSON has `error_code=METADATA_WRITE_FAILED`. Stored file is deleted. No metadata row remains. |

If fault injection is too costly for Phase 1, record TC-ATOMIC-001 and TC-ATOMIC-002 as explicit follow-up risks in `.ai/verification.md`; do not silently ignore them.

### Configuration

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-CONFIG-001 | P0 | Upload root is configurable for tests. | Test settings point upload root to `tmp_path`. | Perform valid upload. | File is written under `tmp_path`, not real `data/uploads`. |
| TC-CONFIG-002 | P0 | Database path is configurable for tests. | Test settings point DB to `tmp_path/test.sqlite3`. | Perform valid upload. | Metadata is written to temp DB, not local dev DB. |
| TC-CONFIG-003 | P1 | Default local config points under repository data directory. | App runs without test overrides. | Inspect settings. | Upload root and DB path resolve under documented local data paths. |
| TC-CONFIG-004 | P1 | Missing parent folders are created safely. | Configured upload/DB parent directories do not exist. | Start app or perform upload. | Required folders are created without touching source-material folders. |

### Phase 1 Boundary Tests

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
| --- | --- | --- | --- | --- | --- |
| TC-BOUNDARY-001 | P0 | Phase 1 code does not require vector services. | No Qdrant or vector service is running. | Run Phase 1 automated tests. | Tests pass without vector service. |
| TC-BOUNDARY-002 | P0 | Phase 1 code does not require LLM credentials. | No LLM API key is configured. | Run Phase 1 automated tests. | Tests pass without LLM credentials. |
| TC-BOUNDARY-003 | P0 | Phase 1 upload does not parse documents. | Valid upload succeeds. | Inspect response and DB row. | Parse status is pending; no OCR, LLM, parser, or embedding output is expected. |
| TC-BOUNDARY-004 | P1 | Deferred endpoints are not exposed as complete features. | App is running. | Probe non-Phase-1 routes only if router list exposes them. | Any non-Phase-1 route is absent, clearly stubbed, or returns not implemented; it must not pretend to be complete. |

## Delivery Command Checks

These checks are required for Phase 1 completion evidence, but they should not be mixed into core business pytest files.

| ID | Priority | Scenario | Command | Expected Result |
| --- | --- | --- | --- | --- |
| DC-001 | P0 | Harness status confirms large mode. | `ai-status` | Output reports initialized project and `mode: large`. |
| DC-002 | P0 | Harness doctor validates workflow state. | `ai-doctor` | State schema and large-mode files pass. Uncommitted working tree warning is acceptable during active work. |
| DC-003 | P0 | Windows project check script runs. | `.\scripts\ai_check.ps1` | Script exits 0 and runs real Phase 1 checks after implementation. |
| DC-004 | P1 | Bash project check is recorded when unavailable. | `bash ./scripts/ai_check.sh` | If unavailable, record blocker in `.ai/verification.md`; do not claim it passed. |

## Manual Smoke Cases

Manual smoke is required after the server can run locally.

### MS-001 Health Smoke

Command:

```powershell
curl.exe --noproxy "*" http://127.0.0.1:8000/health
```

Expected:

```json
{"status":"ok"}
```

### MS-002 Upload Smoke

Create a temporary file:

```powershell
Set-Content -Path .\data\samples\phase1-smoke.txt -Value "hello bid knowledge"
```

Upload it:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@.\data\samples\phase1-smoke.txt"
```

Expected:

1. HTTP `201 Created`.
2. Response follows the upload success JSON contract.
3. A stored file appears under configured upload root.
4. SQLite contains one metadata row.
5. Stored file bytes match the source file.

## Phase 1 Definition Of Done

Phase 1 is complete only when:

1. FastAPI app starts locally on Windows.
2. `GET /health` returns stable JSON response.
3. `POST /api/files/upload` accepts `historical_bid` and `tender`.
4. Uploaded file bytes are persisted under configured upload root.
5. Metadata is persisted into configured SQLite database.
6. Invalid requests do not leave orphan files or metadata rows.
7. Upload response follows the documented JSON contract.
8. Error responses follow the documented JSON contract.
9. SQLite `documents` table follows the documented field contract.
10. Phase 1 does not initialize OCR, LLM, vector database, parser, embedding, or frontend Demo logic.
11. All P0 automated tests pass.
12. Any deferred P1/P2 item is recorded in `.ai/verification.md`.
13. `ai-status`, `ai-doctor`, and `.\scripts\ai_check.ps1` evidence is recorded.
14. Manual health and upload smoke evidence is recorded, unless server startup is explicitly blocked.

Phase 1 is only the backend foundation for later document parsing and knowledge-base capability. It is not the customer-facing Demo.

## Suggested Pytest Mapping

| Test file | Case IDs |
| --- | --- |
| `backend/tests/test_health.py` | TC-HEALTH-001 to TC-HEALTH-003 |
| `backend/tests/test_upload_contract.py` | TC-UPLOAD-001 to TC-UPLOAD-006 |
| `backend/tests/test_upload_validation.py` | TC-ERR-001 to TC-ERR-008 |
| `backend/tests/test_storage.py` | TC-STORAGE-001 to TC-STORAGE-006 |
| `backend/tests/test_database.py` | TC-DB-001 to TC-DB-007 |
| `backend/tests/test_phase1_boundaries.py` | TC-BOUNDARY-001 to TC-BOUNDARY-004 |

Delivery command checks should be recorded in `.ai/verification.md` or CI logs, not treated as upload/business pytest cases.

## Common Failure Diagnosis

1. If localhost calls fail, check proxy variables first and use `curl.exe --noproxy "*"`.
2. If cleanup fails on Windows, make sure SQLite connections are closed before deleting temp directories.
3. If tests write to real `data/uploads`, the settings override is broken.
4. If tests require customer sample files, replace them with synthetic fixtures.
5. If tests require external services, the implementation crossed the Phase 1 boundary.
6. If response fields drift from this document, fix the implementation or update the API contract intentionally before changing tests.
