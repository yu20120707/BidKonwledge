# Phase 1 Verification Checklist

## Required Command Evidence

Every Phase 1 completion report must include:

1. Harness status command.
2. Project check script command.
3. Test command.
4. Any manual smoke command.

Record results in `.ai/verification.md`.

## Harness Checks

Run:

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status"
& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor"
```

Expected:

- initialized: yes
- mode: large
- state_valid: yes
- required large files present

## Script Checks

Run:

```powershell
.\scripts\ai_check.ps1
```

When available:

```powershell
bash ./scripts/ai_check.sh
```

After Phase 1 implementation, these scripts should call the actual build/test commands instead of printing placeholders.

## Automated Tests

Expected test command after implementation:

```powershell
python -m pytest backend/tests
```

Minimum test cases:

1. `GET /health` returns `200` and `{"status": "ok"}`.
2. `POST /api/files/upload` returns `201 Created` for valid `historical_bid` and `tender` uploads.
3. Upload response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
4. Upload rejects invalid input with the documented error JSON shape: `error_code`, `message`, and `details`.
5. Upload saves a small file under the configured upload root without using the original filename as the stored filename.
6. Upload inserts a metadata row into SQLite using the documented `documents` table fields.
7. Failed validation does not leave orphan files or metadata rows.

Use `docs/ai/16-phase1-test-cases.md` as the detailed acceptance source.

## Manual Smoke Checks

After starting the server, verify:

```powershell
curl.exe --noproxy "*" http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Use `--noproxy "*"` for localhost checks on this machine because proxy environment variables can distort local requests.

The upload smoke check should expect HTTP `201 Created` and the fixed upload success response documented in `docs/ai/12-phase1-api-persistence.md`.

## Not Required In Phase 1

Do not require these checks before Phase 1 completion:

1. Docling parsing.
2. OCR parsing.
3. Qdrant startup.
4. Haystack retrieval.
5. LLM generation.
6. Demo page browser walkthrough.

These belong to later phases.
