# Risk And Rollback

## Risks

1. Harness profile drift: `ai-upgrade large` defaults to `cpp-linux-backend-system` unless `--profile python-backend-service` is provided.
2. Scope drift: Phase 1 could accidentally start parsing/RAG work too early.
3. Large sample files could accidentally enter Git history.
4. Placeholder scripts could be mistaken for real build/test coverage after Phase 1 implementation.

## Mitigations

1. `.ai/state.json` is set to `mode = large` and `profile = python-backend-service`.
2. `AGENTS.md`, `README.md`, and Phase 1 docs explicitly require large mode and script execution.
3. `docs/source-materials/sample-catalog.md` indexes large files without copying them.
4. `docs/ai/13-phase1-verification-checklist.md` requires real script/test evidence before Phase 1 completion.

## Rollback

This task is documentation-only. Rollback is a normal Git revert before commit.

If harness-generated large-mode files are not wanted, remove the files listed in `.ai/affected-files.md` and restore `.ai/state.json` from `.ai/backups/20260627-214154/.ai/state.json`.
