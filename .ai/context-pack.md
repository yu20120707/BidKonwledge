# Context Pack

## Harness State

- mode: large
- profile: python-backend-service
- status: INIT
- current_gate: none
- approved_gates: none

## Important Files

- AGENTS.md: present
- docs/ai/: present
- task chain: present
- docs/ai/tasks/init-large/05-verification.md: present
- scripts/ai_check.sh: present
- .ai/verification.md: present
- .ai/reviews/diff-review.md: missing
- .ai/approvals/diff-approval.md: missing

## Git Summary

```text
?? .ai/
?? .codex/
?? .github/
?? .gitignore
?? AGENTS.md
?? CLAUDE.md
?? README.md
?? backend/
?? data/
?? docs/
?? frontend/
?? scripts/
```

## Diff Stat

```text
empty
```

## Changed Files

```text
empty
```

## Recent Review

- unavailable

## Context Manifest

- context manifest: present (.ai/tasks/init-large/context.jsonl)
- context manifest valid: yes
- context manifest entries: 9
  - .ai/spec.md [implement]: Large-mode requirement source
  - .ai/implementation-plan.md [implement]: Large-mode implementation plan
  - .ai/tech-design.md [implement]: Large-mode technical design
  - .ai/risk-and-rollback.md [review]: Rollback and risk guardrails
  - .ai/verification.md [review]: Verification evidence
  - .ai/handoff.md [handoff]: Cross-session handoff summary
  - docs/ai/tasks/init-large/01-spec.md [implement]: Durable task spec evidence
  - docs/ai/tasks/init-large/03-implementation-plan.md [implement]: Durable task implementation plan evidence
  - ... 1 more

## Recent Approval

- unavailable

## Plan Snapshot

- spec: # Spec - Phase 0 Repository Initialization ## Objective
- plan: # Implementation Plan ## Current Large-Mode Prep Task
- affected-files: # Affected Files ## Updated

## Verification Snapshot

- verification.md: present (0 ran, 0 not-run)

## Next Suggested Action

- Start a task or run `ai-review diff` after changes.
