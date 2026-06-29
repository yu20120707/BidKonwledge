# Handoff

## Current State - Phase 11 Sample Outputs And Repeatable Runbook

Phase 11 implementation is complete and verified locally.

Current harness state:

- mode: `large`
- profile: `python-backend-service`
- state status: `DONE`
- current gate: none

Important harness note:

- `.ai/state.json` still reflects `DONE/current_gate: none`.
- Do not claim a new gate has opened unless the matching harness command
  succeeds.

Implemented in Phase 11:

1. Fixed sample manifest:
   `docs/ai/sample-outputs/phase11/manifest.json`
2. Representative sample outputs:
   - historical upload/parse
   - knowledge cards
   - tender analysis
   - retrieval evidence
   - candidate generation
   - no-LLM fallback
   - OCR smoke status
   - expected failures
3. Phase 11 docs:
   - `docs/ai/36-phase11-sample-outputs-dev-spec.md`
   - `docs/ai/37-phase11-test-cases.md`
   - `docs/ai/38-phase11-repeatable-demo-runbook.md`
4. JSON validation test:
   - `backend/tests/test_phase11_sample_outputs.py`

Latest verification:

- `ai-status`: passed.
- `ai-doctor`: passed.
- targeted pytest:
  `backend/tests/test_phase11_sample_outputs.py`
  -> `3 passed, 1 warning`
- `.\scripts\ai_check.ps1`: passed with `114 passed, 1 warning`
- `git diff --check`: passed with line-ending normalization warnings only
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distro is
  available

Outstanding blocker:

1. Bash verification is still unavailable on this Windows machine because WSL
   / Linux distro is not installed.

## Ready For Phase 12

Recommended next phase:

- Phase 12 - Semantic Retrieval Adapter Spike

Phase 12 should start as an evaluation/spike, not as a replacement of the
current deterministic retrieval path. The Phase 11 sample set is now the fixed
comparison baseline.

Use these Phase 11 artifacts as inputs:

1. `docs/ai/sample-outputs/phase11/manifest.json`
2. `docs/ai/sample-outputs/phase11/retrieval-evidence.json`
3. `docs/ai/38-phase11-repeatable-demo-runbook.md`
4. `backend/tests/test_phase11_sample_outputs.py`

Do not add mandatory Qdrant, Haystack, or embedding dependencies to normal
tests unless Phase 12 explicitly proves and documents that promotion decision.

## Next Session Prompt

````md
当前仓库：`F:\BidKonwledge`

请继续按 `Auto_AICoding_Harness large mode` 执行。先做环境和上下文确认，不要直接写代码。

当前已完成并 push：
- `61d10ba Complete phase 10 PRD demo flow`
- `7cf8d24 Complete phase 11 repeatable sample outputs`

当前状态：
- `Phase 0-11` 已完成。
- `Phase 11` 已完成固定样本集、代表性 JSON 输出、repeatable runbook 和 JSON 边界测试。
- `.ai/state.json` 仍是 `DONE/current_gate: none`，不要声称新 gate 已打开。
- `bash ./scripts/ai_check.sh` 在本机仍因无 WSL/Linux distro 阻塞，记录 blocker，不要声称通过。

请先运行：
```powershell
git status --short --branch
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

请先阅读：
- `AGENTS.md`
- `docs/ai/README.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/36-phase11-sample-outputs-dev-spec.md`
- `docs/ai/37-phase11-test-cases.md`
- `docs/ai/38-phase11-repeatable-demo-runbook.md`
- `docs/ai/sample-outputs/phase11/manifest.json`
- `docs/ai/sample-outputs/phase11/retrieval-evidence.json`
- `.ai/handoff.md`
- `.ai/verification.md`
- `.ai/evaluation.md`

现在开始 `Phase 12: Semantic Retrieval Adapter Spike`。

目标：
评估 Qdrant、Haystack、embedding 作为可选语义检索路径的价值和集成边界。Phase 12 是 spike / evaluation，不是替换当前 deterministic retrieval 默认路径。

范围：
- 以 Phase 11 固定样本集作为对比基线。
- 先做技术方案和最小 spike 计划，再决定是否写代码。
- 如写代码，优先加可替换 adapter boundary，保持 deterministic retrieval 为默认。
- 可新增 docs：
  - `docs/ai/39-phase12-semantic-retrieval-spike-dev-spec.md`
  - `docs/ai/40-phase12-test-cases.md`
  - `docs/ai/41-phase12-evaluation-report.md`
- 更新 `.ai/spec.md`、`.ai/implementation-plan.md`、`.ai/affected-files.md`、`.ai/run-trace.md`、`.ai/verification.md`、`.ai/evaluation.md`、`.ai/handoff.md`

非目标：
- 不把 Qdrant / Haystack / embeddings 变成 normal tests 的必需依赖。
- 不替换现有 `/api/retrieve` 的 deterministic 默认行为。
- 不做大规模 schema migration。
- 不声称生产级 ranking 或语义检索质量。
- 不做表格重建、图片批量 ingestion、证书/资质真实性校验、登录/用户系统、最终 Word/PDF 导出。
- 不把 PyMuPDF 加进项目依赖。

开始前请先给出任务合同：
1. proposed execution level
2. target outcome
3. expected file or module scope
4. planned verification
5. known uncertainties or blockers

建议验证：
```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_phase11_sample_outputs.py
.\scripts\ai_check.ps1
git diff --check
```

如果尝试：
```powershell
bash ./scripts/ai_check.sh
```
本机没有 WSL/Linux distro 时，记录 blocker，不要声称通过。

完成后请报告：
- 实现了什么
- 中间用到了什么 skill
- 最重要的决定
- 验证结果
- 未验证项和真实原因
````
