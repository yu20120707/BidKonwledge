# Python Typing Guidance

## Static Analysis

- Respect the project's existing type-checking tool: `mypy`, `pyright`, `basedpyright`, or none.
- Do not introduce strictness changes as part of an unrelated task.
- Keep public function and data-model annotations accurate when changing interfaces.

## Runtime Boundaries

- Validate untrusted input at API, CLI, queue, or file boundaries.
- Treat dataclass, Pydantic, attrs, TypedDict, and protocol changes as contract changes.
- Avoid using `Any` to silence real interface uncertainty without documenting why.

## Verification

- Run the project-defined type-check command when type-facing code changes.
- Record skipped type checks and the reason in `.ai/verification.md` for medium or large work.
