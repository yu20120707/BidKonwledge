# Phase 7 Demo Runbook

## Purpose

Provide a repeatable server demo plan for Phase 7 after tender analysis is
implemented.

Status: implementation-backed as of 2026-06-28.

## Recommended Sample Files

Use a small tender file first:

1. Tender sample:
   `KSDQZFCG（GK）2026-64...项目（二次）.docx`

Observed on 2026-06-28:

- This file has a `.docx` extension but its header is legacy OLE
  `D0 CF 11 E0`, so Docling does not recognize it as real DOCX.
- Phase 8A adds automatic local legacy Word conversion before parsing when Word
  COM is available. Without Word COM, conversion fails safely with sanitized
  parse metadata.

Use historical bid files from Phase 6 only as supporting context:

1. `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
2. `宁波运维项目\牧鸿\省人事工资管理系统-宁波人社运维-资格证明文件.docx`

Avoid at Phase 7 start:

- Scanned/image material until OCR phase.
- 18 MB, 37 MB, 194 MB `.docx` files.
- 229 MB archive.
- Legacy `.doc` until conversion behavior is verified.

## Setup

Install normal dev and parsing dependencies:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e ".[dev]"
& $py -m pip install -e ".[parsing]"
```

Start backend:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

## Expected Phase 7 Flow

1. Upload a tender file as `tender`.
2. Parse the tender document.
3. Analyze the tender.
4. Inspect:
   - project requirements
   - scoring items
   - disqualification risks
   - raw text summary
   - `need_human_review`
5. Use the extracted requirements as later generation context.

## API Smoke Shape

Upload:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=tender" `
  -F "file=@<path-to-small-tender.docx>"
```

Parse:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse"
```

Analyze:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/tender/analyze" `
  -H "Content-Type: application/json" `
  -d "{\"document_id\":\"<document_id>\"}"
```

Get analysis:

```powershell
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/tender-analysis"
```

## Expected Output

Analyze should return:

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

## Known Limits

1. Phase 7 does not run OCR.
2. Phase 7 does not use LLMs for tender understanding.
3. Rule-based analysis may miss requirements or risks.
4. Analysis output is evidence extraction only, not legal/compliance judgment.
