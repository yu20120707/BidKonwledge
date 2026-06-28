# Phase 5 Demo Harness Documentation Review Packet

## Role

Read-only harness orchestration and documentation compliance reviewer.

## Assigned Agent

- nickname: Bernoulli
- agent id: `019f0d48-73f1-7fa2-914c-101acc595826`

## Required Skills

- `task-router`
- `verification-before-completion`

## Required Context

- `AGENTS.md`
- `docs/ai/workflow.md`
- `.ai/subagent-packets/README.md`
- `.ai/subagent-packets/reviewer.md`
- `.ai/subagent-packets/explorer.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`
- `.ai/state.json`

## Objective

Audit this multi-subagent review round for Auto_AICoding_Harness compliance:
packet prompts, subagent roles, skill injection, verification evidence,
gate/state caveats, result recording, and residual-risk reporting.

## Forbidden Actions

- Do not edit files.
- Do not approve harness gates.
- Do not claim `.ai/state.json` changed unless a harness command succeeded.

## Expected Output

Required documentation updates, gate/state caveats, verification gaps, and
residual risks.

## Return Format

```text
role: harness-doc-reviewer
status: complete | blocked
required_doc_updates:
gate_state_caveats:
verification_gaps:
blockers:
residual_risks:
```
