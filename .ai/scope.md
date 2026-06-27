# Scope

## Allowed Write Scope

- `AGENTS.md`
- `README.md`
- `docs/ai/*.md`
- `docs/ai/tasks/init-large/*.md`
- `.ai/*.md`
- `.ai/state.json`

## Forbidden Areas

- Do not implement backend business code.
- Do not add runtime dependencies.
- Do not copy large customer sample files into Git.
- Do not start OCR, LLM, embedding, vector-store, retrieval, or demo-page work.

## Harness Requirement

Future development must use `large` mode. Large mode means stronger planning, gate, verification, and handoff discipline. It does not automatically imply multi-agent orchestration unless the user explicitly asks for subagents or delegation.
