# Codex Development Rules

## General Rules

1. Do not build a complete bidding system.
2. Do not build user login or a permission system.
3. Do not build project management.
4. Do not build final Word/PDF export.
5. Do not build CA signing or formal bidding workflows.
6. Keep the MVP backend-first.
7. Keep the frontend minimal and demo-only.
8. Every API must return structured JSON.
9. All generated content must include citations, risks, and `need_human_review`.
10. All external services must be abstracted behind interfaces.

## Engineering Rules

1. Use Python 3.11+.
2. Use FastAPI.
3. Use Pydantic schemas.
4. Use SQLite for MVP metadata.
5. Use local storage for uploaded files.
6. Keep document parsing pluggable.
7. Keep OCR pluggable.
8. Keep LLM provider pluggable.
9. Keep embedding provider pluggable.
10. Keep vector store pluggable.

## Implementation Rules

1. First build a runnable vertical slice.
2. Prefer simple deterministic rules before complex LLM logic.
3. Start with docx and text-based pdf.
4. Treat scanned pdf as a later OCR enhancement.
5. If a file cannot be parsed, return `parse_status = failed` and `error_message`.
6. Do not silently ignore parse errors.
7. Do not generate content without retrieval context unless explicitly marked high risk.
8. Never claim generated content is ready for final bidding submission.
