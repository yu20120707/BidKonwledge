# Python Dependency Guidance

## Dependency Risk

- Treat dependency changes as security, lockfile, packaging, and deployment risk.
- Keep direct dependencies explicit and avoid unnecessary broad upgrades.
- Check whether dependency versions are constrained by deployment images, serverless runtimes, or platform policy.

## Serialization And Frameworks

- Treat changes to JSON schemas, Pydantic models, dataclasses, marshmallow schemas, protobufs, or ORM models as contract changes.
- Treat FastAPI, Django, Flask, Celery, SQLAlchemy, or similar configuration changes as runtime behavior changes.
- Document migration impact for settings, environment variables, middleware, and background workers.

## Verification

- Run dependency-aware tests or import smoke tests after dependency changes.
- Record exact commands and skipped checks in `.ai/verification.md` for medium or large work.
