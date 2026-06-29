# Phase 10 Demo Runbook

## Purpose

Walk through the PRD-shaped `/demo` page as a stakeholder-facing capability
demo.

## Preconditions

1. The backend server is running locally.
2. Phase 6 knowledge-card API, Phase 7 tender-analysis API, and Phase 9 OCR
   smoke evidence are already available in the repo state.
3. Optional real LLM credentials may be supplied from page fields or server env.

## Start Server

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$env:BIDKNOWLEDGE_DATABASE_URL='sqlite:///./data/bidknowledge.db'
$env:BIDKNOWLEDGE_UPLOAD_ROOT='./data/uploads'
& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Open:

- `http://127.0.0.1:8000/demo`

## Flow

### 1. Historical Bid Upload / Parse

1. Choose one historical bid file.
2. Click `Upload Historical Bid`.
3. Click `Parse Historical Bid`.
4. Confirm the status panel shows document id, parse status, and section/chunk
   counts.

### 2. Build Knowledge Cards

1. Click `Build Knowledge Cards`.
2. Confirm the page shows at least one PRD-shaped card with source filename and
   source section context.

### 3. Tender Upload / Parse / Analyze

1. Choose one tender file.
2. Click `Upload Tender File`.
3. Click `Parse Tender File`.
4. Click `Analyze Tender`.
5. Confirm the page shows project requirements and disqualification risks.

### 4. Select PRD Tag

1. Use the PRD tag selector.
2. Confirm the page shows:
   - selected PRD label
   - mapped retrieval tag
   - current top-k value

This mapping is intentional and keeps the backend retrieval contract unchanged.

### 5. Retrieve Evidence

1. Click `Retrieve Evidence`.
2. Confirm the evidence list shows:
   - source filename
   - retrieval score
   - tags
   - snippet text

### 6. Generate Candidate Content

1. Optionally fill request-scoped LLM API key/base URL/model.
2. Click `Generate Candidate Content`.
3. Confirm the page shows candidate content.

If no LLM is configured:

1. Confirm the page shows the structured missing-LLM risk state.
2. Confirm `need_human_review` remains visible.

### 7. Review Evidence Chain

Confirm the page shows:

1. citations
2. risks
3. `need_human_review`
4. raw JSON of the latest stage

### 8. OCR Status

Confirm the OCR section says only:

1. local Phase 9 smoke verified
2. `paddleocr 2.10.0`
3. `paddlepaddle 2.6.2`
4. `parse_mode=ocr` smoke produced `1 section / 1 chunk`
5. `parse_mode=auto` OCR fallback succeeded
6. PyMuPDF is local-smoke-only and not a committed project dependency
7. OCR is not claimed as production-ready

## Verification Companion

Before closing the task, run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
.\scripts\ai_check.ps1
git diff --check
```

Attempt:

```powershell
bash ./scripts/ai_check.sh
```

If no WSL/Linux distro is available, record that blocker and do not claim bash
verification passed.
