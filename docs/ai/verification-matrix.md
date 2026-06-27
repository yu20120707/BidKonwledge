# Python Verification Matrix

| Risk Trigger | Suggested Verification |
| --- | --- |
| `public_api_change` | Focused API tests plus compatibility notes. |
| `dependency_change` | Project-defined dependency install/check and focused tests. |
| `serialization_change` | Fixture round-trip or contract tests. |
| `database_migration_change` | Migration upgrade/downgrade or compatibility tests when available. |
| `async_concurrency_change` | Async timeout, cancellation, and concurrency behavior tests. |
| `packaging_change` | Build/import smoke test and project-defined packaging checks. |

## Notes

- Prefer `pytest` or project-defined wrappers already present in the target repository.
- Run type checking when interface or typing changes are part of the task.
- Record actual commands and results in `.ai/verification.md` for medium and large work.
