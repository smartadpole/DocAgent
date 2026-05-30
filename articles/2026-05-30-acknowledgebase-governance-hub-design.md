---
type: article
id: ARTICLE-ACKNOWLEDGEBASE-GOVERNANCE-HUB-20260530
status: active
updated: 2026-05-30
tags: [agent, governance, acknowledgebase, hub, scheduling, propagation, cross-project]
---

# AcknowledgeBase 作为治理中控：设计方案

相关：[[concepts/agent-governance]]、[[articles/2026-05-30-agent-governance-cross-project-synthesis]]、[[articles/2026-05-30-agent-system-deep-analysis]]、[[harness-feedback-ledger]]

## 问题重新定位

跨工程的治理传播问题，有三种思路：

| 思路 | 机制 | 问题 |
|---|---|---|
| 各工程自己演化 | 现状 | 独立重发明，漂移不可见 |
| git submodule 共享内核 | 运行时依赖 | wiki 是模板源，不是运行时库，不适用 |
| **AcknowledgeBase 中控定期治理** | 主动观察 + 生成建议 | **无需改变各工程拓扑，是当前最可行路径** |

AcknowledgeBase 天然具备做中控的条件：
- 已经有读取所有工程的能力（本次跨工程分析在这里完成）
- 双重角色（管理层 + 知识库）适合"观察 + 沉淀"的工作方式
- 不需要其他工程做任何改动
- 中控的所有产出留在 AcknowledgeBase 自身，不直接写入其他工程

---

## 中控的职责边界

**AcknowledgeBase 中控只做三件事**：

1. **读**：定期读取各工程的关键治理文件（AGENTS.md、harness-feedback-ledger、governance/ 核心文件、sensor 脚本清单）
2. **比**：对照 wiki TEMPLATE ZONE 和跨工程共性模式，识别漂移和缺口
3. **写建议**：把发现的问题和改进建议写入 AcknowledgeBase 内的专项页面，或生成可直接转发给目标工程的 handoff 包

**AcknowledgeBase 中控不做**：直接修改其他工程的文件。patch 建议由用户确认后，在目标工程里执行。

---

## 治理动作分类

### 动作 1：模板漂移检查（wiki → 各工程）

**逻辑**：wiki 的 TEMPLATE ZONE（平台级约定文件）发生重要变更后，中控对比各工程对应文件，输出漂移清单。

```
漂移检查流程：
1. 读 wiki/governance/template-changelog.md（记录 TEMPLATE ZONE 变更）
2. 对每个工程：读对应文件的关键结构和版本标记
3. 对比：哪些工程已跟进，哪些落后，落后多少
4. 输出：projects/governance/drift-report-YYYY-MM.md
```

**输出格式**：

```markdown
# 模板漂移报告 2026-05

| 工程 | 文件 | wiki 版本 | 工程版本 | 建议动作 |
|---|---|---|---|---|
| DocCustomeranalysis | agent_finalizer.py | v2.3（scope proof） | v2.1 | 建议升级 finalizer |
| DocFilmCommunity | response-mode-routing.md | v1.4 | v1.4 | 已对齐 |
| fetch-adapter | check_agent_harness.py | v1.2 | v1.0 | 建议补 scope check |
```

### 动作 2：跨工程 episode 对比（发现平台级模式）

**逻辑**：读取所有工程的 harness-feedback-ledger，识别在 2+ 工程中重复出现的问题类型，晋升为平台级问题。

```
跨工程 episode 分析流程：
1. 读所有工程的 harness-feedback-ledger.md
2. 对 episode 按"问题类型"聚合（不是逐字匹配，而是语义聚合）
3. 出现在 2+ 工程的问题类型 → 平台级问题
4. 输出：cross-project-episode-registry.md（已有规划）+ 平台级改进建议
```

**意义**：当 DocCustomeranalysis 解决了写入边界失守问题，而 DocFilmCommunity 还没有，中控能发现这个差距，并生成"DocFilmCommunity 应参考 DocCustomer 的 check_external_write_boundary.py"的建议。

### 动作 3：规则健康度检查（各工程自身）

**逻辑**：不依赖 wiki 基线，而是对每个工程自身的治理文件做健康度评估。

检查项：
- AGENTS.md 行数是否超过阈值（建议 100 行以内）
- Ledger 中 active episode 是否过多（超过 20 条无 closed 记录）
- sensor 脚本数量 vs 覆盖的 episode 数量是否对应
- 是否有 Rule Prune Queue 且上次执行时间

输出：各工程健康度评分 + 具体改进建议。

### 动作 4：生成针对性 handoff 包

对于漂移超阈值或健康度低的工程，中控生成一个可直接转发的 handoff 包：

```markdown
# 治理 handoff：DocFilmCommunity 2026-05

## 建议来源
AcknowledgeBase 中控 2026-05 定期治理

## 发现的问题
1. finalizer 缺少 scope proof 检查（wiki v2.3 已有，当前工程停在 v2.1）
2. Episode Ledger 有 8 条 active，无 closed 记录

## 建议动作
1. 参考 DocCustomeranalysis/scripts/agent_finalizer.py 升级 finalizer
2. 对 2026-04 之前的 active episode 做一次 review，标记可关闭的为 closed

## 参考材料
- wiki/scripts/agent_finalizer.py（v2.3）
- DocCustomeranalysis/governance/harness-feedback-ledger.md（finalizer scope proof episode）
```

用户收到这个包后，在 DocFilmCommunity 里执行，不需要自己重新发现问题。

---

## 调度设计

### 调度频率

| 对象 | 频率 | 理由 |
|---|---|---|
| 主控工程（DocCustomeranalysis、DocFilmCommunity） | 月度 | 演化快，问题多，值得高频 |
| 子工程（fetch-adapter、customeranalysis、prefect、train_platform） | 季度 | 演化慢，问题少，低频够用 |
| wiki 漂移检查（wiki → 各工程） | wiki 有 TEMPLATE ZONE 变更时触发 | 不需要定时，事件驱动 |
| 跨工程 episode 对比 | 月度 | 跟主控频率一致 |

### 调度实现选项

**选项 A：AcknowledgeBase 内的 `/schedule` 定时任务**（推荐起步方式）

在 AcknowledgeBase 里设置一个每月触发的 scheduled agent，执行以下流程：
```
1. 读取 wiki/governance/template-changelog.md
2. 对每个主控工程：读 AGENTS.md + harness-feedback-ledger
3. 生成月度漂移报告 → projects/governance/drift-YYYY-MM.md
4. 生成月度 episode 摘要 → cross-project-episode-registry.md 更新
5. 对健康度低的工程生成 handoff 包 → inbox/ 或指定位置
```

**选项 B：用户主动触发（现阶段更实际）**

目前调度工具需要额外配置，可以先做成一个手动触发的技能（skill），用户说"做一次跨工程治理检查"时触发，而不是自动定时运行。技能成熟后再转 scheduled。

**选项 C：集成到 AcknowledgeBase 的 WORKFLOW**

在 AcknowledgeBase 的 WORKFLOW 里加入"月度中控治理"作为标准模式，在响应模式路由里增加"跨工程治理扫描"这个模式，用户每月开一次会话专门做这件事。

**推荐起步路径**：选项 C（最小阻力）→ 选项 B（技能化）→ 选项 A（调度化）

---

## 中控需要的能力建设

### 在 AcknowledgeBase 内新建的文件

```
AcknowledgeBase/
  projects/governance/           # 中控治理层（新建）
    cross-project-registry.md    # 跨工程工程台账（各工程基本信息 + 最后检查时间）
    cross-project-episodes.md    # 跨工程 episode 注册表（平台级问题）
    drift-reports/               # 按月的漂移报告
      2026-05-drift-report.md
    handoffs/                    # 生成的 handoff 包（待用户确认后转发）
      2026-05-DocFilm-governance-handoff.md
  governance/cross-project-routing.md  # 中控的响应模式（如何读、比、写建议）
```

### wiki 需要做的最小改动

在 wiki 里加一个 `governance/template-changelog.md`，记录 TEMPLATE ZONE 文件的重要变更。格式：

```markdown
# Template Changelog

## v2.3 (2026-05-29)
- agent_finalizer.py: 新增 --scope-base / --scope-manifest 参数（scope proof）
- 影响工程：所有使用 finalizer 的工程

## v2.2 (2026-05-27)
- response-mode-routing.md: 新增 Issue Intake 分层流程
- 影响工程：主控工程
```

这是 wiki 需要的唯一改动，成本极低。

---

## 一句话总结

AcknowledgeBase 中控的核心价值不是"自动化"，而是**把"发现治理问题"这件事从各工程的偶然副产品，变成 AcknowledgeBase 的显式职责**。定期扫描 + 生成建议 + 用户确认后执行——这个流程不需要改变任何工程的结构，只需要 AcknowledgeBase 承担观察者和协调者的角色。
