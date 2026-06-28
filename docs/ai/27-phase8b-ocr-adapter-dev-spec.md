# Phase 8B OCR Adapter Dev Spec

## Purpose

Phase 8B adds a replaceable OCR adapter for scanned PDFs. It keeps Docling as
the primary parser for normal text documents and only uses OCR when requested or
when PDF text parsing fails in `auto` mode.

Status: implemented on 2026-06-28.

## In Scope

1. OCR adapter interface.
2. Fake OCR support in automated tests.
3. Lazy PaddleOCR implementation.
4. `parse_mode = auto | text | ocr`.
5. OCR page text converted to normal sections/chunks.
6. OCR metadata in parse and chunk metadata.

## Out Of Scope

1. Required PaddleOCR dependency.
2. Large image batch ingestion.
3. Table structure reconstruction.
4. Certificate or qualification evidence validation.
5. Vector retrieval, embeddings, LLM parsing, export, or final document output.

## Parse Behavior

- `auto`: default. Existing parser first; PDF can fallback to OCR.
- `text`: existing parser only.
- `ocr`: OCR only for PDF in Phase 8B.

## Metadata

Parse metadata includes:

- `parse_mode`
- `ocr_attempted`
- `ocr_engine`
- `ocr_pages_count`
- `ocr_average_confidence`
- `ocr_fallback_reason`

Chunk metadata receives the same OCR evidence where relevant.

## Acceptance

1. Existing parse calls without a body still work.
2. Text PDF parsing remains OCR-free.
3. OCR mode can parse fake OCR page output into chunks.
4. Auto mode falls back to OCR on PDF text parser failure or no chunks.
5. OCR failures are sanitized.
6. Tests do not require PaddleOCR.
