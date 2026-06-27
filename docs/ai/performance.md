# Python Performance Guidance

## Performance Risk

- Treat hot-path allocation, serialization, ORM access, network calls, import-time work, and cache changes as performance-sensitive.
- Check startup time, memory growth, event-loop blocking, and connection-pool behavior when relevant.
- Avoid broad caching changes without invalidation and memory-growth notes.

## Runtime Considerations

- Note GIL, multiprocessing, thread pool, and async event-loop implications when concurrency changes.
- For batch or streaming work, check backpressure, chunking, and pagination behavior.
- Keep profiling assumptions separate from correctness changes unless the target project owns them.

## Verification

- Prefer existing benchmarks or project-defined performance smoke tests.
- If no benchmark exists, record manual risk assessment and the reason a benchmark was not run.
