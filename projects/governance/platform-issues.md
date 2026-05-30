---
type: governance-platform-issues
id: GOV-PLATFORM-ISSUES-001
scope: cross-project
status: active
source_of_truth: true
updated: 2026-05-30
tags: [governance, platform, issues, cross-project]
---

# 平台级问题目录

记录跨工程共性问题、抽象解法和实施状态。每个问题独立于具体工程；handoff 只引用问题编号，不重复写抽象部分。

**治理标准**：[[governance/platform-standards]]  
**注册表**：[[projects/governance/registry]]

---

## 问题目录

### PI-001 Issue Intake 缺证据充分性判定

**问题描述**：用户提 issue 时，agent 无论用户是否已提供足够证据（截图 + 入口 + 期望行为），都默认执行浏览器复现，导致 issue 归档耗时显著增加。

**首次观测**：DocCustomeranalysis，2026-05-30，ISSUE-024 归档，耗时 21 分钟；复现占约 6-8 分钟。

**根因**：Issue Intake 快路径缺少"进入三层执行前先判断用户证据是否已足够"的前置规则；复现被当作默认步骤而不是条件步骤。

**受影响工程**：所有有 Issue Intake 流程的主控工程（DocCustomeranalysis、DocFilmCommunity）

**抽象解法**：在 Issue Intake 快路径的三层执行之前，补证据充分性判定：用户同时提供截图、可见入口路径和期望行为时，直接进入最小落档层，不做浏览器复现；仅当三项中任一缺失时，才在最小落档层前做最小范围复现（只验证现象能否稳定触发）。

**实施状态**：

| 工程 | 状态 | handoff | 备注 |
|---|---|---|---|
| DocCustomeranalysis | `applied` | [[projects/governance/handoff-DocCustomeranalysis-2026-05]] | 2026-05-30 直接操作 |
| DocFilmCommunity | `pending` | — | 待下一轮治理 |

---

### PI-002 跨工程读取模式无读取预算

**问题描述**：主控工程读取子工程文件时，响应模式路由只为"快速诊断"定义了读取预算（1-3 个事实源），子工程读取模式的最小读取描述为"目标代码上下文"，无深度上限，agent 自行判断，实际读入整个相关模块，造成 token 消耗过重。

**首次观测**：DocCustomeranalysis，2026-05-30，ISSUE-022 复开，耗时 14 分 53 秒；读取 customeranalysis 子工程无约束。

**根因**：`response-mode-routing.md` 读取预算段只覆盖快速诊断模式，子工程实现/回传模式无对应 budget 规则。

**受影响工程**：所有主控工程（DocCustomeranalysis、DocFilmCommunity）；子工程不适用（子工程不主动读其他工程）

**抽象解法**：在响应模式路由的读取预算段，补"主控读取子工程的默认读取预算"：默认只读子工程 AGENTS.md + 直接点名的最多 3 个文件 + 命令输出；不默认读子工程完整 codebase、governance 文件或历史报告；扩展读取前必须说明理由和范围。

**实施状态**：

| 工程 | 状态 | handoff | 备注 |
|---|---|---|---|
| DocCustomeranalysis | `applied` | [[projects/governance/handoff-DocCustomeranalysis-token-2026-05]] | 2026-05-30 直接操作 |
| DocFilmCommunity | `pending` | — | 待下一轮治理 |

---

### PI-003 Episode Ledger 无终态，规则只增不减

**问题描述**：DocCustomeranalysis 的 harness-feedback-ledger 有 60+ 条 episode，全部标记为 `active`，零条 `closed` 或 `deprecated`。已被 sensor 覆盖的规则没有从 AGENTS.md 退出，只挂在 Prune Queue 里。每次读取治理上下文都加载整张表，形成固定 token 成本，且认知负担随 episode 数量线性增长。

**首次观测**：2026-05-30 跨工程横向分析，DocCustomeranalysis ledger 全量审查。

**根因**：系统设计了"规则晋升"路径（observed → promoted），但没有设计"规则闭环"路径（promoted → closed/deprecated）；已被 sensor 覆盖的 episode 没有出口。

**受影响工程**：DocCustomeranalysis（最重，60+条）；AcknowledgeBase 自身也有类似问题

**抽象解法**：
1. 为 episode 补终态定义：`promoted-replaced`（已有 sensor/模板覆盖）、`deprecated`（问题消失或被更高层规则吸收）、`closed`（验证规则持续生效超过 N 轮）
2. 建立周期清理节奏：每月/每季检查 ledger，把已有 sensor 覆盖的 active episode 推进到终态
3. AGENTS.md 对应规则：sensor 覆盖后从 AGENTS.md 正文移出，只保留 sensor 入口引用

**实施状态**：

| 工程 | 状态 | handoff | 备注 |
|---|---|---|---|
| DocCustomeranalysis | `pending` | — | 需单独一轮，逐条判断 60+ 条 episode |
| AcknowledgeBase | `pending` | — | 同类问题，同步处理 |

---

## 变更记录

| 日期 | 变更内容 |
|---|---|
| 2026-05-30 | 初版建立，录入 PI-001、PI-002、PI-003 |
