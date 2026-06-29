# Phase 12 Test Cases

## Goal

Verify that semantic retrieval remains optional, isolated, and comparable
against the Phase 11 deterministic baseline.

## Automated - Documentation Slice

### P0 Phase 11 Baseline Still Valid

Command:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_phase11_sample_outputs.py
```

Expected:

1. Phase 11 sample JSON remains valid.
2. Manifest still identifies two historical bid samples, one tender sample, one
   OCR smoke sample, and selected tags.
3. No Phase 12 doc changes weaken the sample-output secret/runtime boundary.

### P0 Project Check

Command:

```powershell
.\scripts\ai_check.ps1
```

Expected:

1. compile check passes
2. backend pytest passes
3. no Qdrant, Haystack, embedding model, API key, or network service is required

### P0 Diff Hygiene

Command:

```powershell
git diff --check
```

Expected:

1. no whitespace errors
2. no generated binary, runtime DB, upload, Qdrant storage, or model-cache files

## Automated - Adapter Skeleton Slice

Run these only if Phase 12 proceeds from documentation to code.

### P0 Default Retrieval Does Not Require Semantic Dependencies

Setup:

1. unset Qdrant, Haystack, embedding, and API-key environment variables
2. parse a small fake historical bid fixture

Expected:

1. `POST /api/retrieve` still returns deterministic results
2. no Qdrant, Haystack, embedding, or network import is required
3. existing response shape is unchanged

### P0 Semantic Mapper Preserves Source Metadata

Setup:

1. create fake persisted chunk rows
2. map them into semantic retrieval records

Expected:

1. `chunk_id`, `document_id`, `section_id`, `section_title`, `section_path`,
   `text`, `tags`, source filename, role, extension, page range, and metadata
   are preserved
2. no local absolute paths are emitted

### P0 Fake Semantic Adapter Is Deterministic

Setup:

1. index three fake Phase 11-style records
2. query the three fixed Phase 11 tag/query pairs

Expected:

1. fake adapter returns stable ordering
2. source metadata is present
3. scores are marked as spike/evaluation scores, not production ranking claims

### P0 Optional Import Boundary

Setup:

1. run tests in an environment without `qdrant-client`, `qdrant-haystack`,
   `haystack`, `sentence-transformers`, or provider credentials

Expected:

1. unit tests pass
2. optional adapter construction fails with a clear configuration/dependency
   message only when explicitly invoked

## Manual / Optional Integration

### P1 Qdrant Local Smoke

Precondition:

1. developer intentionally starts local Qdrant or uses Qdrant Python local mode
2. no customer source files are copied into Git

Expected evidence:

1. collection name
2. embedding vector size and distance metric
3. indexed record count
4. payload keys
5. query results for Phase 11 fixed tags
6. cleanup or storage path
7. whether the result improved, matched, or degraded deterministic retrieval

### P1 Haystack Pipeline Smoke

Precondition:

1. developer intentionally installs Haystack/Qdrant integration outside normal
   test requirements or in an optional dependency group

Expected evidence:

1. indexing pipeline shape
2. query pipeline shape
3. dependency setup cost
4. result comparison against direct Qdrant client
5. whether Haystack adds enough value for the demo

### P1 Provider Embedding Smoke

Precondition:

1. API key is available outside Git and outside committed sample JSON
2. network access is intentionally allowed

Expected evidence:

1. provider/model name
2. vector size
3. request volume
4. failure mode when credentials are absent
5. no secrets in logs or docs

## Non-Goals

Phase 12 tests do not verify:

1. production ranking quality
2. full Chinese retrieval benchmark performance
3. final legal truth of citations or qualification materials
4. table reconstruction
5. image batch ingestion
6. final Word/PDF export
7. login or multi-user permissions
8. Qdrant/Haystack as mandatory normal-test dependencies

## Bash Verification

Attempt when appropriate:

```powershell
bash ./scripts/ai_check.sh
```

If this Windows machine still has no usable WSL/Linux distro, record the
blocker and do not claim bash verification passed.
