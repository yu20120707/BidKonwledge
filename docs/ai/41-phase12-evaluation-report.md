# Phase 12 Evaluation Report

## Status

Status: planning/evaluation slice complete, with a follow-up deterministic
demo-flow closeout.

The Phase 12 semantic retrieval spike did not add Qdrant, Haystack,
embeddings, schema migrations, dependencies, or public API contract changes.
A later closeout pass tightened the existing deterministic demo flow so PRD
knowledge-card tags can retrieve their source chunks before any semantic
adapter work begins.

## Baseline

Phase 11 provides the comparison baseline:

1. fixed sample manifest
2. representative deterministic retrieval evidence
3. repeatable runbook
4. JSON boundary test

The current deterministic retrieval path remains the default and is still the
only normal-test retrieval path.

## Deterministic Demo-Flow Closeout

The follow-up closeout intentionally stayed inside the current deterministic
retrieval path:

1. Historical retrieval candidates are limited to `historical_bid` documents.
2. PRD knowledge-card tags can bridge back to source chunks without changing
   the `POST /api/retrieve` response contract.
3. If an original chunk row and a knowledge-card-backed row tie on score, the
   card-backed row is preferred so `chunk_metadata.knowledge_card` remains
   available as evidence.
4. The demo page first tries the selected PRD tag and only falls back to the
   mapped chunk tag if the PRD tag returns no evidence.
5. The demo page records `requested_tag`, `effective_tag`,
   `fallback_chunk_tag`, and `used_fallback` in raw JSON for review.
6. The loop-engineering polish pass adds a visible historical evidence pool,
   tender-requirement generation context, loading/error button handling, and
   browser-verified desktop/mobile layout hygiene.

This closeout is not a semantic retrieval prototype and does not change the
Phase 12 recommendation below.

## Component Evaluation

| Component | Value | Integration Boundary | Risk | Initial Decision |
| --- | --- | --- | --- | --- |
| Qdrant | Purpose-built vector store; local Docker and Python local mode make spike feasible; payload metadata can preserve source traceability. | Optional adapter or evaluation script over existing chunk/card records. | Extra service/storage, payload indexing decisions, cleanup, security if exposed beyond local. | Worth evaluating after a fake adapter boundary exists. |
| Haystack | Provides pipeline structure, Qdrant document store integration, retrievers, and embedders. | Optional implementation detail inside semantic adapter. | Additional abstraction and dependencies may be heavier than direct Qdrant for a small demo. | Evaluate after direct adapter boundary; do not expose in API contracts. |
| Local embeddings | Avoids provider secrets and can support Chinese retrieval. BGE-M3 is a plausible candidate because it is multilingual and supports multiple retrieval functions. | Optional embedder provider behind lazy import/model download. | Model download, memory, cold start, vector dimension, runtime variability. | Candidate for manual smoke only, not normal tests. |
| Provider embeddings | Faster setup when credentials exist; avoids local model weight management. | Optional provider-backed embedder with request/env-scoped credentials. | Secrets, network, cost, provider lock-in. | Manual smoke only; never required for tests. |
| Fake embeddings/adapters | Enables unit tests and boundary checks without external dependencies. | Test-only adapter implementation. | Does not prove retrieval quality. | Required before real semantic code. |

## Phase 13 Check

No Phase 13 is currently defined in the repository.

Do not treat the semantic adapter skeleton as Phase 13 unless the roadmap first
adds a Phase 13 entry with scope, non-goals, and verification.

## Recommended Next Decision

Do not write Qdrant/Haystack code first.

The lowest-risk next implementation, if Phase 12 proceeds to code, is:

1. add semantic retrieval record/match models or dataclasses
2. add a mapper from current retrievable chunk rows to semantic records
3. add a fake deterministic semantic adapter
4. add tests proving default `/api/retrieve` remains dependency-free
5. add tests proving metadata preservation through the semantic boundary

Only after that should the project try an optional local Qdrant smoke.

## Comparison Method

Use the three Phase 11 fixed retrieval tag/query pairs:

1. `运维服务实施方案` -> `运维服务` / `运维 服务 方案`
2. `突发应急方案和措施` -> `应急响应` / `应急 响应 措施`
3. `网络和数据安全防护保障措施` -> `安全保障` / `网络 数据 安全 防护`

For each pair, record:

1. deterministic top-k result ids and scores
2. semantic top-k result ids and scores
3. overlap count
4. newly discovered useful evidence
5. false positives
6. source metadata completeness
7. setup/runtime cost

## Promotion Criteria

Promote semantic retrieval from spike to optional prototype only if:

1. it finds useful evidence that deterministic retrieval misses on the fixed
   Phase 11 sample set
2. source metadata remains complete enough for citations
3. setup and cleanup are documented
4. normal tests still pass without semantic dependencies
5. deterministic retrieval stays the default

Do not promote semantic retrieval to default until a broader evaluation set and
quality threshold exist.

## Deferral Criteria

Defer semantic retrieval if:

1. deterministic retrieval is sufficient for the current stakeholder demo
2. Qdrant/Haystack setup cost is higher than the demonstrated value
3. local embedding runtime is too heavy for the target demo environment
4. provider embeddings require credentials that the demo cannot assume
5. semantic results degrade citation traceability or introduce noisy matches

## Residual Risk

1. This report is a plan-level evaluation, not a retrieval-quality benchmark.
2. Current claims about Qdrant, Haystack, and BGE-M3 are based on official docs
   checked during Phase 12 planning, but no local semantic runtime smoke has
   been executed yet.
3. Bash verification remains blocked on this Windows machine when no WSL/Linux
   distro is available.

## References

- Qdrant local quickstart: https://qdrant.tech/documentation/quickstart/
- Qdrant collections and vector schema: https://qdrant.tech/documentation/manage-data/collections/
- Haystack QdrantDocumentStore: https://docs.haystack.deepset.ai/docs/qdrant-document-store
- Haystack Qdrant retrievers: https://docs.haystack.deepset.ai/reference/integrations-qdrant
- Haystack embedders: https://docs.haystack.deepset.ai/docs/embedders
- BGE-M3 model card: https://huggingface.co/BAAI/bge-m3
