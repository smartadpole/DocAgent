---
type: development_test_report
id: REPORT-2026-06-30-AGENT-SYSTEM-MATURITY-PHASE-1A
project: PROJ-WIKI-001
status: partial
updated: 2026-06-30
tags: [report, agent-system, intelligence, skill-maturity, work-item-auto-decomposition]
---

# Agent System Maturity Phase 1A Validation

## 验证对象

- 对象：wiki Agent System Capability Package、Intelligence Evidence Snapshot、通用 skill 前沿维护、项目绑定事项自动拆解。
- 类型：文档治理 / skill contract / template / sensor / external evaluator capsule。
- 计划来源：用户要求从 skill-only 升级到 agent system + intelligence maturity，并把 `work-item-auto-decomposition` 做成本仓项目 / 领域绑定能力。
- 关闭边界：本报告只证明 Phase 1A 本地 wiring 和 evidence capsule；不宣布外部矩阵已刷新、不输出正式智能化总分、不关闭任何 Gate / FP / EP / TASK。

## Matrix Recognition Capsule

| Field | Current value |
| --- | --- |
| evaluator | AcknowledgeBase skill maturity matrix + agent-system maturity diagnostics；主控 / Orchestrator 持有外部刷新循环。 |
| candidate files / scanned surfaces | `AGENTS.md`、`.codex/AGENTS.md`、`governance/agent-system-maturity.md`、`governance/agent-system-maturity-snapshot.v1.json`、`skills/README.md`、`skills/*/SKILL.md`、`templates/`、`scripts/check_*.py`、`projects/development/reports/`、`views/`。 |
| current baseline | 本地 `skill-maturity` 和 `work-item-matrix` 专项检查已通过；此前外部诊断中 wiki 的 `work-item-auto-decomposition` 是缺口，agent-system / intelligence 需要本地 owner 与 snapshot。 |
| true-gap | 缺本仓 agent-system owner、snapshot、专项 checker、项目绑定事项自动拆解 skill。 |
| recognition-gap | cross-project skill adoption / transferable governance 已有能力，但缺 Matrix Recognition Capsule 与 agent-system 七层对象在本仓本地成套出现。 |
| signal-only-gap | 入口链接、checker key、expected impact 属于识别面补齐；不能为此制造空通用 skill。 |
| Goodhart guard | 不复制 AcknowledgeBase 当前分数、profile hash、运行 ID、项目事实或一次性报告；不把本地 green 当外部 readback。 |
| external readback | `blocked-by-orchestrator-readback`；本轮只回传 expected impact，外部矩阵需主控刷新。 |

## Agent System Capability Package

| Layer | Local owner | Phase 1A evidence | Remaining boundary |
| --- | --- | --- | --- |
| skill | [[skills/README]]、各 `SKILL.md` | `skill-maturity` baseline 通过；新增 [[skills/work-item-auto-decomposition/SKILL]] | skill 完整不能上推为 agent system 完整。 |
| runtime | `AGENTS.md`、`.codex/AGENTS.md`、git / browser profile 规则 | git remote / fetch / ahead-behind 读回；浏览器 profile 规则存在 | 未运行 browser / MCP live probe。 |
| harness | [[response-mode-routing]]、Goal、Loop、Run Capsule、[[agent-orchestration]] | 既有 harness owner + 新 snapshot 引用 | 结构证明不等于真实行为智能。 |
| memory | [[BRAIN]]、[[projects/memory/README]]、[[projects/trace]]、[[log]] | 本轮读入口并将变更分流到 report / trace / log | memory 不替代当前 live readback。 |
| evaluation | `scripts/check_agent_system_maturity.py`、`scripts/check_all.py` | 新增专项 checker 和 report | 外部 evaluator 未在本仓内刷新。 |
| governance | [[harness-evolution]]、[[harness-feedback-ledger]]、[[instruction-adherence]] | 维持纠偏 / sensor / 模板晋升路由 | 未做负证据行为评分。 |
| migration | [[skills/transferable-skill-governance/SKILL]]、[[skills/cross-project-skill-adoption-prompt/SKILL]] | 补 Matrix Recognition Capsule、source-depth、Goodhart guard | 不复制源工程目录或当前分数。 |

## true-gap / recognition-gap / signal-only-gap

| Item | Gap type | Patch | Boundary |
| --- | --- | --- | --- |
| Agent system owner | true-gap | 新增 [[agent-system-maturity]] | 只定义本仓 owner，不复制上游目录。 |
| Intelligence snapshot | true-gap | 新增 `governance/agent-system-maturity-snapshot.v1.json` | 八维均为 `insufficient-evidence`，不出总分。 |
| Agent system checker | true-gap | 新增 `scripts/check_agent_system_maturity.py` 并接入 `check_all` | 本地结构检查，不是外部 readback。 |
| Cross-project taskbook frontier maintenance | recognition-gap | 更新 cross-project skill adoption skill / TRANSFER | 任务书质量门不代表目标已完成迁移。 |
| Transferable skill governance review contract | recognition-gap | 更新 transferable governance skill / TRANSFER | sensor 证明 wiring，不证明真实运行质量。 |
| Work-item auto decomposition | true-gap + project-bound | 新增项目绑定 skill，更新矩阵模板和 checker | 不硬升通用可迁移 skill。 |
| Entry links / checker key | signal-only-gap | 同步 README / INDEX / governance / `.codex` | 只为可发现性，不扩写空能力。 |

## Intelligence Evidence

全部八维已出现在 snapshot，但仍为 `insufficient-evidence`：

- `intent_modeling`：缺 rubric-backed 正负行为样本。
- `mode_selection`：缺模式选择行为评分。
- `tool_and_runtime_use`：缺系统化 runtime 行为证据。
- `context_and_memory_use`：缺 stale memory 和 owner-first 行为审查。
- `decomposition_and_orchestration`：缺 worker / evaluator 合流行为样本。
- `evidence_judgment`：缺结构 / runtime / outcome / manual 边界行为评分。
- `recovery_and_learning`：缺重复偏差到 sensor / template 晋升的效果评分。
- `user_alignment`：缺用户纠偏序列和最终回复 alignment 评分。

## 验证计划

- Local validation：`python3 scripts/check_all.py --only agent-system-maturity,skill-maturity,work-item-matrix`
- Full validation：`python3 scripts/check_all.py`
- Whitespace：`git diff --check`
- External evaluator：主控刷新 AcknowledgeBase matrix；本仓记录 `blocked-by-orchestrator-readback` 和 expected impact。

## 未验证边界

- 未运行外部矩阵刷新。
- 未进行 browser / MCP live runtime probe。
- 未做八维 intelligence 负证据审查和行为评分。
- 未关闭任何 Gate、FP、EP、TASK、risk 或 issue。
- 预存 `.obsidian` 本地改动不属于本报告和本次提交范围。
