# Python Framework Guidance

## Framework Discovery

- Identify whether the project uses FastAPI, Django, Flask, Starlette, Celery, or another framework before applying conventions.
- Prefer existing routing, dependency injection, settings, middleware, and test-client patterns.
- Treat decorator, middleware, settings, and lifecycle-hook changes as runtime behavior changes.

## API Framework Notes

- For FastAPI or Starlette, review dependency injection, request models, response models, background tasks, and async boundaries.
- For Django, review settings, middleware, apps, migrations, ORM behavior, and management commands.
- For Flask, review app factory, blueprints, context usage, and extension initialization.

## Verification

- Use framework test clients or integration tests for routing, middleware, authentication, and error handling changes.
- Record any external service assumptions in `.ai/verification.md` for medium or large work.
