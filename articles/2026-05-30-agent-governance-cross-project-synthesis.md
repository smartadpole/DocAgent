---
type: article
id: ARTICLE-AGENT-GOVERNANCE-CROSS-PROJECT-SYNTHESIS-20260530
status: active
updated: 2026-05-30
tags: [agent, governance, harness, cross-project, synthesis, solution]
---

# Agent 治理跨工程综合分析与方案探索

相关：[[concepts/agent-governance]]、[[articles/2026-05-30-agent-governance-reflection-doccustomer]]、[[harness-feedback-ledger]]、[[governance/harness-evolution]]、[[governance/instruction-adherence]]

## 来源

本页来自 2026-05-30 对以下 8 个工程的 AGENTS.md、governance/ 目录、harness-feedback-ledger 和 sensor 脚本的横向对比分析：

**主控工程**：`DocCustomeranalysis`、`DocFilmCommunity`

**子工程**：`fetch-adapter`（Customer pipeline）、`customeranalysis`（识别服务）、`prefect`（调度平台）、`train_platform`（训练平台）

**模板源**：`Software/wiki`（所有工程的 fork 起点，独立存在，不归属任何主控）

**治理中控 + 个人知识库**：`AcknowledgeBase`（双重角色：跨工程管理层 + 概念研究存档）

---

## 各工程现状速览

| 工程 | 角色 | 语言 | AGENTS.md 规模 | Episode 数量 | Sensor 数量 | 成熟度 |
|---|---|---|---|---|---|---|
| DocCustomeranalysis | 主控 | 中文 | ~360 行 | 60+ 条（全 active） | ~15 个 | 最高 |
| DocFilmCommunity | 主控 | 中文 | ~300 行 | 5 条 | ~8 个（从 Doc 吸收） | 中 |
| fetch-adapter | 子工程 | 英文 | ~120 行 | 3 条 | 2 个 | 中低 |
| train_platform | 子工程 | 英文 | ~100 行 | 3 条 | 1 个 | 低 |
| prefect | 子工程 | 英文 | ~100 行 | — | — | 低 |
| customeranalysis | 子工程 | — | 无 AGENTS.md | — | — | 无 |
| Software/wiki | 模板源 | 中文 | ~370 行 | ~8 条 | ~8 个 | 高（基准版本） |
| AcknowledgeBase | 治理中控/知识库 | 中文 | ~350 行 | ~10 条 | ~8 个 | 高 |

---

## 跨工程共性问题

### 问题 1：每个项目都在独立重发明同一套治理轮子

这是最根本的结构性问题。DocFilmCommunity 的 Ledger 第一条 episode 就是"主控系统吸收 DocCustomeranalysis 的 harness/goal/事项体系"，fetch-adapter 和 train_platform 的 Ledger 里同样有"从主控吸收规则升级"的 episode。三个主控工程、四个子工程，每次吸收都是人工复制、手动对齐，没有任何自动化传播机制。

当 DocCustomeranalysis 修复了"外部子工程写入边界失守"，DocFilmCommunity 需要单独发现这个问题才能修复。当 AcknowledgeBase 沉淀了"finalizer 写入范围证明缺口"，其他工程的 finalizer 仍停留在旧设计。

**核心缺口**：治理知识是多份本地副本，不是单一来源。

**值得注意的例外**：`customeranalysis` 采用了完全不同的路子——用 10 个 `.cursor/rules/*.mdc` 模块化规则文件作为单一来源，AGENTS.md 由这些文件**自动生成**。这个设计天然解决了"规则只增不减"问题：每个规则文件职责单一（代码风格、版本管理、UI 语言等），可以独立编辑、独立废弃，不会导致 AGENTS.md 无限膨胀。这个模式值得在共享内核方案中借鉴。

### 问题 2：Episode Ledger 状态永久停在 active，规则只增不减

DocCustomeranalysis 有 60+ 条 episode，全部标记为 `active`，零条 `closed` 或 `deprecated`。AcknowledgeBase 的 ledger 有少数 `promoted` 但大部分 `observed`。train_platform 最好，有 2 条 `promoted-replaced`。

这说明系统设计了"规则晋升"路径，但没有设计"规则闭环"路径：episode 从 `observed` -> `promoted` -> ??? 没有终态。已经被 sensor 覆盖的规则没有从 AGENTS.md 中退出，只是在 Prune Queue 里挂着。

**结果**：AGENTS.md 持续增长（DocCustomeranalysis 已超 360 行），认知成本指数上升，新 agent 或模型版本切换时更容易遗漏关键约束。

### 问题 3：子工程写入边界靠自然语言规则，效果不稳定

所有 6 个有规则的工程都有"不要写其他工程"的自然语言规则：
- DocCustomeranalysis AGENTS.md: `本库侧 agent 默认不直接修改代码工程或子工程文件`
- prefect AGENTS.md: `Do not modify files or directories outside the current working directory`
- train_platform: 类似规则
- fetch-adapter: `Treat DocCustomeranalysis as the main-control read-only source by default`

DocCustomeranalysis 的 Ledger 中有 3 条 episode 关于这条规则失守（"外部子工程写入边界失守"、"验收反馈误执行为子工程代码补丁"、"Finalizer 写入范围证明缺口"）。每次失守的响应是：加更严格的自然语言规则 + 加一个新 sensor。但问题在于 sensor 也是事后检查，不是写入前防护。

**根因**：路径权限应该是系统层约束，而不是自然语言声明。

### 问题 4：响应模式分流在每个工程独立实现，维护成本高

三个主控工程都有 `response-mode-routing.md`，内容高度相似但维护分散：
- DocCustomeranalysis: `governance/response-mode-routing.md` + 独立 sensor
- AcknowledgeBase: `governance/response-mode-routing.md` + 独立 sensor
- DocFilmCommunity: `governance/response-mode-routing.md`（从 DocCustomer 吸收）
- fetch-adapter: `.codex/context/agent-harness-goal-governance.md`（自研的简化版）
- prefect: `.codex/agents/routing.md`（自研）
- train_platform: 无独立路由文件，用 AGENTS.md 内联规则

六种实现，六处维护，任何一次改进都需要手动同步。fetch-adapter 的简化版实际上更轻量，更适合子工程场景，但没有反向传播到其他工程。

### 问题 5：Commit closure 是所有工程的高频失守点

DocCustomeranalysis Ledger 有至少 5 条独立 episode 关于 commit closure：
- "提交闭环提醒依赖复发"
- "提交闭环二次失守"
- "预存脏改不能阻断 scoped commit"
- "收尾 finalizer 缺失导致执行性能退化"
- "Goal 自动续跑漏 log"

每次修复都在 instruction-adherence 里加规则、在 finalizer 里加检查。目前 `agent_finalizer.py` 已有 5 个例外参数（`--allow-residual`、`--allow-external-residual`、`--scope-base`、`--allowed-path`、`--scope-manifest`）。finalizer 本身成了一个需要维护的复杂工具。

子工程（fetch-adapter、train_platform）的 commit closure 问题更简单，但没有好的解决方案，只有规则声明。

### 问题 6：主控-子工程协调协议不统一，回传包格式各异

每个子工程自己定义了和主控的通信协议：
- fetch-adapter: L1/L2/L3 handoff template，基于证据层级分级
- prefect: 引用主控 FP/EP/TASK ID，发现问题报告 blocker
- train_platform: `.codex/context/main-control-coordination.md`，有回传规则
- customeranalysis: 无规则

没有统一格式意味着：主控在收 handoff 时需要理解每个子工程的约定，跨子工程对比时无法标准化。fetch-adapter 的 L1/L2/L3 分级是其中最完善的设计，但没有被其他子工程采用。

### 问题 7：中英文双语导致概念漂移

三个主控工程用中文，四个子工程用英文。同一个概念有两套词：
- 主控说 "验收关闭"，子工程说 "closure"
- 主控说 "执行包"，子工程说 "handoff"
- 主控说 "证据层级"，子工程说 "evidence level"

这不是翻译问题，而是概念对齐问题：两套词背后是否精确对应同一个概念？从现有文件看，对齐是不完整的（如 "AP" 在主控是验收计划，在子工程没有对应概念）。

### 问题 8：Governance 自演进机制只在主控工程完整存在

DocCustomeranalysis 和 AcknowledgeBase 有完整的 H5 演进闭环（harness-evolution + ledger + sensor + prune queue）。DocFilmCommunity 也大致具备。

但 fetch-adapter 只有简版 ledger，prefect 没有 harness 演进机制，train_platform 有 ledger 但没有成熟演进路径。当子工程发现规则失守，没有机制把教训传播回主控，也没有机制让主控把修复同步到子工程。

---

## 可行方案：以 wiki 为模板源的协议化演进

### 前提澄清：wiki 是模板源，不是运行时库

**wiki 的实际角色**：所有主控和子工程都是从 wiki 复制（fork）出来的，wiki 本身不是任何工程的子工程，也不以 submodule 方式被引用。这意味着：
- submodule 方案**不适用**（各工程已独立演化，无法简单回挂）
- "自动传播"的问题不是运行时同步问题，而是**模板漂移问题**：如何让 wiki 的改进流向已经发散的副本

**AcknowledgeBase 的双重角色**：既是管理层（负责跨工程学习和治理），也是个人知识库（概念沉淀、研究存档）。它是最合适承担"模板漂移监控"和"跨工程协议对齐"职责的工程。

### 核心思路

当各工程是模板源的独立副本时，"改进传播"需要换一套思路：
- 不靠运行时同步（submodule/package），而靠**协议化约定 + agent 辅助 diff**
- 把 wiki 里的改进显式标记为"平台级变更"，由 AcknowledgeBase 管理层决定哪些工程需要跟进
- 各工程不强制同步，但通过 AcknowledgeBase 的漂移报告知道自己落后了多少

### 方案一：wiki 分区 + AcknowledgeBase 漂移监控（推荐）

**设计**：在 wiki 里把文件明确分成两个区：

```
wiki/
  [TEMPLATE ZONE]              # 这里的内容是平台级约定，各工程应保持对齐
    governance/WORKFLOW.md     # 工作流骨架
    governance/POLICY.md       # 规则裁定框架
    scripts/check_all.py       # 标准 sensor 脚本
    scripts/agent_finalizer.py # 标准 finalizer
    templates/                 # 所有模板骨架
    governance/response-mode-routing.md  # 响应模式路由

  [INSTANCE ZONE]              # 这里是 wiki 自己的业务内容，各工程可自由发散
    BRAIN.md                   # wiki 专属背景
    projects/                  # wiki 的项目运行层
    log.md                     # wiki 的过程记录
```

**AcknowledgeBase 的漂移监控职责**：
1. 定期（或 wiki 发生 TEMPLATE ZONE 改动时）由 AcknowledgeBase 的 agent 对比 wiki TEMPLATE ZONE 和各工程对应文件的差异
2. 生成"模板漂移报告"：哪些工程在哪些核心治理文件上已经落后多少版本
3. 对于高价值改进（如 finalizer 的 scope proof 缺口修复），生成可直接应用到目标工程的 diff 建议

**传播机制**：
- wiki 改进 → 标记 `[TEMPLATE ZONE]` 变更 → AcknowledgeBase 检测漂移 → 生成目标工程的 patch 建议 → 用户决定是否应用

这不是自动同步，而是**有人工确认的辅助同步**，比纯手工更快，比强制 submodule 更灵活。

### 方案二：模块化规则文件（借鉴 customeranalysis Cursor rules）

**核心洞察**：customeranalysis 的 `.cursor/rules/*.mdc` 是模块化规则设计的一个好案例——每个规则文件职责单一，AGENTS.md 由这些文件组合生成，而非手工积累。

**应用到 wiki 拓扑**：把 wiki 的治理规则拆成独立的 `.rule.md` 文件：

```
wiki/governance/rules/
  write-boundary.rule.md      # 写入边界规则（版本化）
  commit-closure.rule.md      # 提交闭环规则（版本化）
  response-mode.rule.md       # 响应模式路由规则（版本化）
  episode-lifecycle.rule.md   # Episode 生命周期规则（版本化）
```

每个规则文件有版本号。各工程的 AGENTS.md 开头声明"使用 wiki@v2.1 的 write-boundary 规则"，AcknowledgeBase 的漂移检查就变成版本号对比，而不是全文 diff。

**优点**：版本化使漂移检测极其简单；规则可独立废弃；AGENTS.md 引用版本而非复制正文，大幅减少文本体积。

### 方案三：AGENTS.md 三档精简

**三档分类**（行数由分类逻辑决定，不硬定上限）：
- **P0（必须在 AGENTS.md）**：写入边界声明、响应模式路由入口、执行合同语义入口——这些是 agent 每轮必须加载的硬约束，不能跳转。
- **P1（移到 owning page，AGENTS.md 只保留跳转链接）**：所有 `git log`、`commit`、`测试验收`、`子工程回写`、`AP 格式`规则——按需读取，不需要每轮全量加载。
- **P2（不进 AGENTS.md，进入 Prune Queue）**：重复覆盖、已有 sensor 守住、低频触发的规则——候选清理，每季度执行一次。

**执行触发器**：每次有新规则进入 AGENTS.md，同时必须有一条旧规则进入 Prune Queue；Prune Queue 清理是硬性约束，不是 backlog。

### 方案四：写入边界字段化（最高杠杆，立即可做）

不管传播机制怎么设计，这条可以立即在所有工程独立执行：

- 任务开始时，agent 必须声明 `allowed_write_roots`（TASK_SCOPE.md 字段或 Goal Contract 字段）
- finalizer 在收尾时做 scope proof：比较本轮实际提交文件列表与声明的允许写入范围
- 没有 scope 声明 → finalizer blocked → 要求用户显式声明

这把写入边界从"agent 读规则自我约束"变成"任务起点的结构化字段 + 收尾的可检查 proof"。注意：scope proof 是 **post-commit check**，不是写入前拦截；真正的 pre-write 拦截需要工具层或沙箱层支持，当前工具链里不具备，不应作为近期可执行目标。

### 方案五：git worktree 物理隔离（中期，依赖工具层支持）

- 主控给每个跨工程任务创建独立 worktree，物理路径上隔离主控和子工程
- Agent 在 worktree 里工作，无法操作 worktree 外的 git 路径

这是对写入边界最彻底的系统层解法，但依赖工具链对 worktree 的支持，属于中期目标，不能在文档里写得像立即可推进。

### 方案六：跨工程 Episode 共享注册表

**当前问题**：同一类问题（commit closure、写入边界、response mode 分流过重）在每个工程里独立出现，独立修复。

**建议方案**：在 AcknowledgeBase（知识库）中维护一张 `cross-project-episode-registry`，格式：

```markdown
| 模式名 | 首次出现 | 涉及工程 | 当前解决方案 | 共享状态 |
|---|---|---|---|---|
| 写入边界失守 | DocCustomer 2026-05-28 | DC/DF/fetch-adapter | external-write-boundary check | 待共享 |
| Commit closure 遗漏 | DocCustomer 2026-05-27 | DC/AB | agent_finalizer.py | 已共享 |
```

当某个模式在 2+ 工程出现，它自动晋升为"平台级问题"，优先进入共享治理内核。

---

## 优先级建议

考虑迁移成本和短期收益，建议按以下顺序推进：

| 优先级 | 方案 | 难度 | 收益 | 建议时机 |
|---|---|---|---|---|
| P0 立即 | AGENTS.md 三档精简（方案三） | 低 | 直接降低认知负担 | 现在 |
| P0 立即 | 写入边界字段化 scope proof（方案四） | 低 | 减少最高频失守 | 现在 |
| P1 近期 | 跨工程 Episode 注册表（方案六） | 低 | 避免重复发明 | 本季度 |
| P2 中期 | wiki 分区 + AcknowledgeBase 漂移监控（方案一） | 中 | 让模板改进可被追踪 | 下季度规划 |
| P2 中期 | 模块化规则版本化（方案二，前置：方案一落地） | 中 | 漂移检测变版本号对比，大幅减少全文 diff 成本 | 方案一稳定后 |
| P3 远期 | git worktree 物理隔离（方案五） | 高 | 系统层代替规则层 | 工具链成熟后 |

---

## 一句话总结

这 8 个工程的共同问题是：**治理知识是多份手动同步的本地副本，改进无法自动传播，规则靠积累不靠剪枝，边界靠声明不靠执行**。可行出路是让漂移可见、让传播有协议——wiki 做模板分区，AcknowledgeBase 做漂移监控，短期先从 AGENTS.md 精简和 scope proof 字段化两个零迁移成本动作切入。

## 后续参考

- 单工程问题详述：[[articles/2026-05-30-agent-governance-reflection-doccustomer]]
- 当前 episode 台账：[[harness-feedback-ledger]]
- 治理演进判断入口：[[governance/harness-evolution]]
- 指令遵循覆盖层：[[governance/instruction-adherence]]
