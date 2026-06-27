# Reference Repositories

Reference repositories are stored outside the business repo:

```text
F:\BidKonwledge_refs
```

## Current Clones

| Repo | Local Path | Commit | Notes |
| --- | --- | --- | --- |
| `https://github.com/infiniflow/ragflow.git` | `F:\BidKonwledge_refs\ragflow` | `f90be41` | Full RAG product reference. Use for product behavior, citations, document ingestion UX, and deployment tradeoffs. |
| `https://github.com/deepset-ai/haystack-demos.git` | `F:\BidKonwledge_refs\haystack-demos` | `17e6103` | Engineering reference. Use `qdrant_indexing` for later indexing/query pipeline shape. |

## Rules

1. Do not commit these repositories into `F:\BidKonwledge`.
2. Do not copy source files without recording origin, commit, and license.
3. Prefer dependency usage and small adapted patterns over vendoring.
4. Re-run `git -C <path> rev-parse --short HEAD` before relying on a reference commit in a future task.
