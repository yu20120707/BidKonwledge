# Python Backend Guidance

## Review Focus

- Keep public API and wire-format changes explicit.
- Treat dependency, packaging, import-path, and configuration changes as compatibility risks.
- Prefer small, testable functions around IO, serialization, and business rules.
- Preserve existing framework conventions instead of introducing new ones without a clear reason.

## Runtime Notes

- State the expected Python version before using new language or typing features.
- Keep sync, async, thread, and process boundaries explicit.
- Avoid hidden global state in request handlers, workers, and tests.
- Document migration impact for module moves, settings changes, and package metadata changes.

## Agent Checklist

- Inspect `pyproject.toml`, `requirements*.txt`, `setup.cfg`, `tox.ini`, or project docs before choosing commands.
- Prefer project-defined scripts or task runners when present.
- Record build, test, lint, and type-check commands in `.ai/verification.md` for medium or large work.
