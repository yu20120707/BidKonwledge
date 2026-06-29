# Phase 11 Repeatable Demo Runbook

## Purpose

Run the PRD-shaped demo with a fixed sample set and compare the observed API
shape against committed representative JSON outputs.

## Preconditions

1. Repository is on a commit that includes Phase 10 and Phase 11 docs.
2. Source materials are available at the source root recorded in
   `docs/source-materials/sample-catalog.md`.
3. Customer source files remain outside Git.
4. Optional OCR runtime is installed only when replaying the OCR smoke path.
5. Optional LLM credentials are available only when replaying the successful
   generation path.

## Start Server

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$env:BIDKNOWLEDGE_DATABASE_URL='sqlite:///./data/bidknowledge-phase11.db'
$env:BIDKNOWLEDGE_UPLOAD_ROOT='./data/uploads-phase11'
& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Open:

- `http://127.0.0.1:8000/demo`

## Fixed Samples

Use `docs/ai/sample-outputs/phase11/manifest.json` as the source of truth.

Historical samples:

1. `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
2. `宁波运维项目\牧鸿\省人事工资管理服务系统-宁波人社运维-资格证明文件.docx`

Tender sample:

1. `KSDQZFCG（GK）2026-64...项目（二次）.docx`

OCR smoke sample:

1. `宁波运维项目\九州拓新\批量输出为图片\...\_08.png`

Convert the OCR image to a temporary local PDF only when replaying OCR. Do not
commit the temporary PDF.

## Page Flow

### 1. Historical Bid Primary

1. Upload the primary historical bid as `historical_bid`.
2. Parse with default `auto`.
3. Build knowledge cards.
4. Compare the response shape with:
   - `historical-bid-upload-parse.json`
   - `knowledge-cards.json`

### 2. Historical Bid Qualification-Side Sample

1. Upload the qualification-side sample as `historical_bid`.
2. Parse with default `auto`.
3. Build knowledge cards.
4. Use this only as supporting demo material; do not claim certificate or
   qualification truth validation.

### 3. Tender

1. Upload the tender sample as `tender`.
2. Parse with default `auto`.
3. Analyze tender.
4. Compare response shape with `tender-analysis.json`.

### 4. Tags And Retrieval

Use these fixed PRD labels:

1. `运维服务实施方案` -> `运维服务`
2. `突发应急方案和措施` -> `应急响应`
3. `网络和数据安全防护保障措施` -> `安全保障`

Run retrieval for at least one selected tag and compare shape with
`retrieval-evidence.json`.

### 5. Generation

With an LLM key:

1. Generate candidate content from the selected tag.
2. Confirm citations and `need_human_review = true`.
3. Compare shape with `generation-candidate.json`.

Without an LLM key:

1. Clear server LLM env variables.
2. Leave page API key empty.
3. Generate candidate content.
4. Confirm `LLM_NOT_CONFIGURED`.
5. Compare shape with `no-llm-error.json`.

## OCR Replay

Use OCR only as Phase 9 smoke evidence.

1. Convert the fixed image sample into a temporary PDF outside Git.
2. Upload the temporary PDF.
3. Parse with `parse_mode=ocr`.
4. Optionally upload a fresh copy and parse with `parse_mode=auto`.
5. Compare status fields with `ocr-smoke-status.json`.

Do not add PyMuPDF to project dependencies without explicit license approval.

## Expected Failures And Deferrals

Use `expected-failures.json` when explaining:

1. no LLM key
2. OCR dependency unavailable
3. text PDF should parse without OCR
4. scanned PDF requires OCR runtime
5. large files are deferred
6. qualification truth validation is out of scope

## Verification

Run before closing Phase 11:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_phase11_sample_outputs.py
.\scripts\ai_check.ps1
git diff --check
```

Attempt:

```powershell
bash ./scripts/ai_check.sh
```

If no WSL/Linux distro is available, record that blocker and do not claim bash
verification passed.
