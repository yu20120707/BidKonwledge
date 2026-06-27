# Python Async And Concurrency Guidance

## Concurrency Risk

- Treat asyncio, threading, multiprocessing, Celery, RQ, Dramatiq, and scheduler changes as concurrency risk.
- Keep sync and async boundaries explicit.
- Avoid blocking calls inside event-loop code unless they are isolated with a documented executor strategy.

## Async Code Notes

- Preserve timeout, cancellation, retry, and exception propagation semantics.
- Be explicit about context propagation for tracing, request state, auth, and logging.
- Avoid unbounded task creation, queues, retries, or worker concurrency without backpressure notes.

## Verification

- Prefer deterministic tests for timeout, cancellation, and failure paths.
- For worker changes, document queue, retry, dead-letter, and idempotency behavior.
