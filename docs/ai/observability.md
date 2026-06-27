# Python Observability Guidance

## Logging

- Keep logs actionable and avoid leaking secrets, tokens, passwords, or PII.
- Preserve existing structured logging conventions.
- Include useful request, job, or correlation identifiers when already supported by the project.

## Metrics And Tracing

- For latency-sensitive paths, consider whether metrics or tracing need updates.
- For background workers, document retry, dead-letter, and failure visibility expectations.
- Follow existing OpenTelemetry, Prometheus, StatsD, or framework-specific conventions when present.

## Runtime Operations

- Note deployment impact for worker concurrency, process model, queue consumers, or async event loops.
- Treat timeout, retry, and connection-pool changes as operational risk.
