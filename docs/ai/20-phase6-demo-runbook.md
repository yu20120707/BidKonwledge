# Phase 6 Demo Runbook

## Purpose

Provide a repeatable server demo plan for Phase 6 after knowledge cards are
implemented.

Status: implementation-backed as of 2026-06-28.

## Recommended Sample Files

Use small files first:

1. Historical bid:
   `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
2. Optional second historical bid or qualification sample:
   `宁波运维项目\牧鸿\省人事工资管理系统-宁波人社运维-资格证明文件.docx`
3. Tender sample for later Phase 7:
   `KSDQZFCG（GK）2026-64...项目（二次）.docx`

Avoid at Phase 6 start:

- 18 MB, 37 MB, 194 MB `.docx` files.
- 229 MB archive.
- Scanned/image material until OCR phase.
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

Open:

```text
http://<server-ip>:8000/demo
```

## Phase 6 Flow

1. Upload a historical bid file as `historical_bid`.
2. Parse the document.
3. Build knowledge cards.
4. List knowledge cards.
5. Check tags such as:
   - `运维服务实施方案`
   - `突发应急方案和措施`
   - `网络和数据安全防护保障措施`
   - `服务质量保障和考核评估方案`
6. Use generated cards as the visible historical knowledge layer for later
   retrieve/generate steps.

## API Smoke Shape

Upload:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@<path-to-small-historical-bid.docx>"
```

Parse:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse"
```

Build cards:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/knowledge/build" `
  -H "Content-Type: application/json" `
  -d "{\"document_id\":\"<document_id>\"}"
```

List cards:

```powershell
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/knowledge-cards"
```

## Expected Output

Build cards should return:

```json
{
  "document_id": "string",
  "cards_count": 1,
  "tags": ["运维服务实施方案"]
}
```

List cards should return source-traceable cards, including source file,
section, source chunk id, tag, content, confidence, and metadata.

## Known Limits

1. Phase 6 does not analyze tender files.
2. Phase 6 does not run OCR.
3. Phase 6 does not add vector or semantic retrieval.
4. Card tags are deterministic and keyword-based.
5. Generated content remains candidate content and still requires human review.
