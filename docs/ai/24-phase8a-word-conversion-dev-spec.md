# Phase 8A Legacy / Mislabeled Word Conversion Dev Spec

## Purpose

Phase 8A removes the current real-sample blocker for legacy Word content. Some
customer samples have a `.docx` extension but are actually legacy OLE `.doc`
files. The backend should detect this before parse, convert to a derived true
`.docx` file when possible, and then reuse the existing Docling parser path.

Status: implemented on 2026-06-28.

## In Scope

1. Parse-time content format detection.
2. True `.docx` ZIP header detection.
3. Legacy OLE Word header detection.
4. Mislabeled `.docx` detection when content is OLE.
5. Fake-testable Word converter adapter.
6. Windows Word COM converter for local/manual smoke.
7. Internal derived `.docx` path under upload root.
8. Safe parse metadata.

## Out Of Scope

1. OCR or PaddleOCR.
2. Qdrant, Haystack, embeddings, dense retrieval, or hybrid retrieval.
3. LLM-based parsing or tender understanding.
4. User system, export, or final bidding output.
5. Full file repair or non-Word OLE support.

## Data Contract

`Document.parse_metadata` may include:

- `original_extension`
- `detected_format`
- `is_mislabeled`
- `requires_conversion`
- `conversion_required`
- `conversion_method`
- `converted_path`

`converted_path` must be relative. Absolute local paths must not be returned in
API responses or persisted as parse metadata.

## Conversion Contract

The converter interface is:

```text
convert_to_docx(source_path, target_path) -> WordConversionResult
```

Automated tests use fake converters. Real Word COM is optional and only needed
for the local manual smoke path.

Local dependency note:

- Microsoft Word is available on this machine.
- `pywin32 312` is installed in the bundled Python runtime.
- `win32com.client` imports successfully.

## Acceptance

1. True `.docx` parses without conversion.
2. Legacy `.doc` and mislabeled `.docx` route through converter.
3. Converter failures mark parse failed and sanitize local paths.
4. Existing parser/chunk/tender analysis flow continues to work.
5. Automated tests do not require Word COM or OCR.
