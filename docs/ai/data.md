# Python Data And Persistence Guidance

## Persistence Risk

- Treat SQLAlchemy, Django ORM, Alembic, Django migrations, raw SQL, and data model changes as data compatibility risk.
- Review transaction boundaries, session scope, lazy loading, cascade behavior, and retry semantics.
- Avoid silent migration or query behavior changes without rollback notes.

## Model And Serialization Changes

- Treat Pydantic, dataclass, attrs, TypedDict, marshmallow, protobuf, and ORM model changes as contract changes.
- Check N+1 query risk, pagination behavior, and filtering defaults.
- State migration order and compatibility when schema changes affect deployed services.

## Verification

- Prefer repository/service tests that cover success, validation failure, missing data, and rollback paths.
- Record database engine and migration command assumptions when relevant.
