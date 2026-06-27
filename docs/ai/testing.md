# Python Testing Guidance

## Test Strategy

- Prefer focused `pytest` tests near the changed behavior before broad suite runs.
- Distinguish unit, integration, contract, and external-service tests in verification notes.
- Keep fixtures deterministic and avoid relying on undeclared local services.

## Common Commands

- `pytest`
- `python -m pytest`
- project-defined wrappers such as `tox`, `nox`, `uv run pytest`, or `poetry run pytest`

## Review Checks

- Cover success, error, and boundary cases for API or serialization changes.
- For async code, cover cancellation, timeout, and event-loop behavior where practical.
- For database or migration changes, cover rollback or compatibility paths when feasible.
