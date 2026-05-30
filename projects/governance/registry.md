---
type: governance-registry
id: GOV-REGISTRY-001
scope: cross-project
status: active
source_of_truth: true
updated: 2026-05-30
tags: [governance, registry, cross-project]
---

# 跨工程治理注册表

这是治理中控的核心台账，记录哪些工程在治理范围内、每个工程的路径、成熟度和当前治理阶段。

**治理标准**：[[governance/platform-standards]]  
**审计技能**：[[skills/cross-project-governance-audit/SKILL]]  
**漂移报告**：本目录下 `drift-report-YYYY-MM.md`

---

## 治理阶段定义

| 阶段 | 含义 |
|---|---|
| `reference` | 基准工程，不接受治理，只作对比参照 |
| `unenrolled` | 在列但未开始治理 |
| `assessed` | 已完成成熟度评估，知道差距在哪 |
| `handoff-ready` | 已生成 handoff 包，等待执行 |
| `applying` | 用户正在目标工程里执行 handoff |
| `verified` | 本轮治理动作已执行并复验 |

---

## 工程注册表

| 工程 | 角色 | 语言 | 本机路径 | 整体成熟度 | 治理阶段 | 上次审计 | 备注 |
|---|---|---|---|---|---|---|---|
| AcknowledgeBase | 治理中控 / 知识库 | 中文 | `/Users/hai/Documents/Docs/AcknowledgeBase` | L3+ | `reference` | 2026-05-30 | 基准工程，不接受外部治理 |
| Software/wiki | 模板源 | 中文 | 待补充 | L3 | `reference` | 2026-05-30 | fork 起点，独立维护 |
| DocCustomeranalysis | 主控 | 中文 | 待补充 | L3 | `assessed` | 2026-05-30 | episode 60+条全 active，规则闭环缺口 |
| DocFilmCommunity | 主控 | 中文 | 待补充 | L2 | `assessed` | 2026-05-30 | 从 DocCustomer 吸收，episode 5条 |
| fetch-adapter | 子工程（Customer pipeline） | 英文 | 待补充 | L2 | `unenrolled` | 2026-05-30 | 有 3 条 episode，2 个 sensor |
| train_platform | 子工程（训练平台） | 英文 | 待补充 | L1-L2 | `unenrolled` | 2026-05-30 | 有 sensor，有 promoted-replaced 终态 |
| prefect | 子工程（调度平台） | 英文 | 待补充 | L1 | `unenrolled` | 2026-05-30 | 有规则但无 episode、无 sensor |
| customeranalysis | 子工程（识别服务） | — | 待补充 | 特殊 | `unenrolled` | 2026-05-30 | 用 .cursor/rules/*.mdc 模块化，AGENTS.md 自动生成，值得借鉴 |

> **路径补充**：首次运行审计前，请把"待补充"替换为各工程的本机绝对路径，否则审计技能无法读取对应文件。

---

## 治理优先级

建议推进顺序（按投入产出比）：

1. **DocCustomeranalysis**：成熟度最高、episode 积累最多，优先做规则闭环（deprecated/promoted-replaced）和 scope proof sensor
2. **DocFilmCommunity**：已有基础，补 harness-feedback-ledger 完整化
3. **fetch-adapter**：英文子工程，补 response-mode-routing 等价文件
4. **train_platform / prefect**：优先级较低，等主控稳定后再推

---

## 变更记录

| 日期 | 变更内容 |
|---|---|
| 2026-05-30 | 初版建立，录入 2026-05-30 跨工程分析结果 |
