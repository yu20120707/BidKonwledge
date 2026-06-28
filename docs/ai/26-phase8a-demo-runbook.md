# Phase 8A Demo Runbook

## Purpose

Verify that the recommended KSDQZFCG tender sample can run through upload,
parse, and tender analysis without manual pre-conversion.

## Recommended Sample

```text
C:\Users\26561\Desktop\模型训练资料\甲方提供资料\KSDQZFCG（GK）2026-64喀什大学重大设备更新（5.4人工智能数据抓取及衍生智能服务创新平台-多场景应用系统-人力资源管理平台(一期））项目（二次）.docx
```

This file has `.docx` extension but legacy OLE Word content.

## Setup

Install dev and parsing dependencies:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e ".[dev]"
& $py -m pip install -e ".[parsing]"
```

For real conversion smoke on Windows, Microsoft Word and `pywin32` must be
available. Automated tests do not require either dependency.

Verified local dependency state on 2026-06-28:

- Microsoft Word: available.
- `pywin32`: installed, version `312`.
- `win32com.client`: import passed.

## Flow

1. Start backend.
2. Upload the original KSDQZFCG `.docx` as `doc_role=tender`.
3. Call parse.
4. Confirm parse metadata:
   - `detected_format = legacy_ole_word`
   - `is_mislabeled = true`
   - `conversion_method = word_com`
   - `converted_path` is relative
5. Call tender analysis.

## Expected Result

When Word COM is available:

- upload succeeds
- parse succeeds
- tender analysis succeeds
- `need_human_review = true`

When Word COM is unavailable:

- upload succeeds
- parse fails safely
- error message is sanitized
- no absolute local path is returned

## Boundaries

Phase 8A is not OCR. Scanned PDFs and image-heavy material remain deferred to a
separate OCR adapter phase.
