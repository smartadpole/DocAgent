---
type: article
id: ARTICLE-AGENT-SYSTEM-DEEP-ANALYSIS-20260530
status: active
updated: 2026-05-30
tags: [agent, governance, harness, karpathy, openclaw, memory, routing, synthesis]
---

# Agent 体系深度分析：理论视角与工程现实的对照

相关：[[concepts/agent-governance]]、[[concepts/harness-engineering]]、[[concepts/openclaw]]、[[articles/2026-05-30-agent-governance-cross-project-synthesis]]、[[articles/2026-05-25-harness-engineering-research]]、[[articles/2026-05-28-openclaw-memory-system-research]]

## 来源与方法

本页综合以下来源，对当前 agent 体系做深度对照分析：

- **前沿调研**：Karpathy Software 3.0 / Agentic Engineering 理论（2025-2026）、AHE 论文（arXiv:2604.25850）、AIOS 研究、CoALA memory 框架、Mem0 实践、多 agent 架构 2026 报告、agent 权限边界安全研究
- **知识库存量**：[[articles/2026-05-25-harness-engineering-research]]、[[articles/2026-05-28-openclaw-memory-system-research]]、[[articles/2026-05-25-codex-goals-research]]
- **工程现实**：8 个工程的横向结构分析（见 [[articles/2026-05-30-agent-governance-cross-project-synthesis]]）

**工程拓扑（已校准）**：
- `wiki`：**模板源**。所有其他工程都是从 wiki 复制（fork）出来的，wiki 本身不是任何工程的子工程，也不以 submodule 方式被引用；它是静止的起点，不是运行时共享库。
- `DocCustomeranalysis`：主控，管辖 fetch-adapter / customeranalysis / prefect / train_platform
- `DocFilmCommunity`：主控，管辖 17lang
- `AcknowledgeBase`：双重角色——**管理层**（跨工程学习和治理）+ **个人知识库**（概念沉淀、研究存档）
- 核心挑战：wiki 是一次性模板源，改进不能通过 submodule 传播；各工程复制后独立演化，模板与各副本之间天然发散

---

## 第一层：Karpathy 的理论框架对当前系统的诊断

### Software 3.0 的核心命题

Karpathy 在 2025-2026 年 Sequoia AI Ascent 上的判断是：
- Software 1.0：人类手写代码
- Software 2.0：神经网络权重即程序
- **Software 3.0：提示词即程序，上下文窗口即运行时，LLM 即解释器**

这个框架有一个直接推论：**AGENTS.md 是程序**。它被加载进上下文窗口，由模型"执行"。

当一个程序有 360 行密集非结构化文本，执行结果会是什么？程序员写任何语言的代码都知道：密度越高的非结构化文本，执行越不可靠。这不是 agent 懒惰，而是信息密度超过上下文解析容量的必然结果。

**Karpathy 的另一个关键判断**：从 2025 年 11 月到 12 月，他从自己写 80% 代码变成 agent 写 80%。他对 agent 的定义是"spiky entities"——随机的、有时不可靠的，但当被正确引导时极其有能力。关键词是：**正确引导，而不是更多规则**。

> "Vibe coding raises the floor for everyone. Agentic engineering preserves the quality bar."

"质量保线"靠的是什么？不是更多 prose rules，而是**可执行的、结构化的、可验证的约束**。

### 当前系统与这个框架的距离

| Karpathy 的工程化约束 | 当前系统的实现 | 差距 |
|---|---|---|
| 提示即程序，要有结构 | AGENTS.md 是自然语言长文 | 高密度散文，非结构化程序 |
| 质量保线靠可执行约束 | 主要靠自然语言 + sensor 事后检查 | sensor 是 post-hoc，不是 pre-hoc |
| "正确引导"而非更多规则 | 规则积累主导 | 规则增速高于工程化速度 |
| agent 是随机实体需要容错设计 | 设计假设 agent 能可靠遵守规则 | 失守时加更严格规则，未设计容错层 |
| 上下文窗口是 RAM，要管理 | 无 context budget 显式控制 | 任何任务都加载相同密度的规则 |

### "你可以外包思考，但不能外包理解"

这句话对当前系统的含义是：**治理规则不能替代产品理解**。当前系统有大量规则告诉 agent 怎么写 log、怎么管理 EP/TASK、怎么做验收——但这些规则的质量依赖于用户对规则意图的持续维护。当用户不维护规则时，规则腐烂而 agent 无法辨别。

---

## 第二层：多 agent 架构视角

### 2026 年的主流架构

2026 年多 agent 架构研究的共识：

- **Hub-and-spoke（轮辐式）**：最主流生产架构。中央 orchestrator 分解目标、分发子任务、聚合结果，子 agent 不直接通信。
- **Hierarchical（层级式）**：50+ agent 的企业场景首选，domain supervisor + 顶层 coordinator。
- **Anthropic 自身数据**：Claude Opus 4 作为 lead + Claude Sonnet 4 subagents，性能提升 90.2%。

关键发现：**路由器（supervisor）的 prompt 必须含每个 worker 的明确能力描述；描述模糊则路由随机。**

### 当前系统的拓扑 vs. 理论架构

```
理论上：
AcknowledgeBase（学习/管理层）
       ↓ 管理
wiki（模板内核层）
       ↓ 派生
┌─────────────────────────────┐
DocCustomeranalysis（主控）    DocFilmCommunity（主控）
    ↓ 协调                         ↓ 协调
fetch-adapter                      17lang
customeranalysis
prefect
train_platform
```

```
现实上：
AcknowledgeBase ←──── 人工阅读和手动同步 ────→ 各工程
wiki ←──── 人工模仿复制 ────→ 各工程 AGENTS.md
DocCustomeranalysis ←──── 人工转发 issue ────→ 子工程
```

**核心问题**：这是一个 **hub-and-spoke 的文档拓扑**，但没有 **hub-and-spoke 的执行路由**。协调靠的是人类读文档，不是 agent 执行协议。

### 缺失的 Orchestrator 层

当前系统没有任何"orchestrator agent"。DocCustomeranalysis 作为主控，其协调能力完全依赖用户在对话中手动触发。子工程无法主动汇报，主控无法主动路由任务。

这意味着：
1. 每次跨工程任务都需要用户在两个工程里分别开对话
2. handoff 协议（L1/L2/L3）是文档级约定，不是机器可执行协议
3. 主控-子工程的状态同步完全依赖人工

---

## 第三层：OpenClaw memory 框架对当前 memory 设计的审视

### OpenClaw 的四层 memory 架构

```
磁盘层（可检索）：
  memory/YYYY-MM-DD.md  ──→  工作层（日常观察，细粒度）
  MEMORY.md             ──→  提纯层（长期稳定事实）
  DREAMS.md             ──→  晋升审阅层（候选长期记忆）
  memory-wiki/          ──→  知识编译层（structured claims + evidence）

上下文注入层（当前 prompt）：
  AGENTS.md / SOUL.md   ──→  启动注入（bootstrap）
  active memory plugin  ──→  按需召回（pre-reply sub-agent）
```

### 当前系统的 memory 现状对照

| OpenClaw 层 | 当前系统对应 | 差距 |
|---|---|---|
| 工作层（daily memory） | log.md | log.md 是按主题记录，不是按日期的工作台账 |
| 提纯层（MEMORY.md） | BRAIN.md + projects/memory | 结构相似，但无晋升机制，人工维护 |
| 晋升审阅层（DREAMS.md） | harness-feedback-ledger（仅 Harness 部分） | 没有通用的"候选提纯"中间层 |
| 知识编译层（memory-wiki） | articles/ + concepts/ | 有知识卡片，但无 structured claims、evidence、contradictions |
| 按需召回（active memory） | 无 | 全部靠 agent 在 prompt 内手动读 |
| Prompt budget 控制 | 无显式控制 | 无 context budget 可视化 |

**最大缺口**：当前系统没有 **action-sensitive memory**。OpenClaw 专门强调有些 memory 不只是"事实"，还会改变未来动作，必须连同 action boundary 一起记录：
- 是否需要审批
- 临时限制是否还有效
- 谁是 owner / authority
- 何时过期

这直接对应当前系统的写入边界问题——写入权限是一种 action-sensitive memory，但当前只用自然语言规则表达，没有结构化存储和执行层面的 enforce。

### CoALA 框架的四类 memory

认知科学 → LLM Agent 的标准映射（CoALA framework，2025-2026 共识）：

| 类型 | 存储内容 | 当前系统实现 |
|---|---|---|
| Working memory | 当前上下文窗口，live reasoning | 无预算控制，任务越来越重 |
| Episodic memory | 过去发生的具体事件 | log.md（低结构化） + harness ledger（仅 Harness） |
| Semantic memory | 稳定事实、偏好、决策 | BRAIN.md + projects/memory（强） |
| Procedural memory | 可复用技能、可执行计划 | skills/（强）+ scripts/（强） |

**强项**：Procedural memory（skills + scripts）设计最好，与 Voyager 的 skill library 理念一致。

**弱项**：Episodic memory 没有结构化的事件索引（log.md 太散，没有 time decay + retrieval）；Working memory 无预算管理。

---

## 第四层：AHE（Agentic Harness Engineering）视角的成熟度再评估

### AHE 的三个可观测性支柱

arXiv:2604.25850 定义的 AHE 三支柱：

1. **Component observability**：每个可编辑的 harness 组件有文件级表示，动作空间明确且可回退
2. **Experience observability**：把数百万 raw trajectory tokens 蒸馏成分层证据语料
3. **Decision observability**：每次编辑配对一个 self-declared prediction，后续验证与实际 outcome 对照

### 当前系统对 AHE 三支柱的覆盖

**Component observability**：部分覆盖
- governance/ 文件层级清晰 ✓
- 每个 sensor 脚本有独立文件 ✓
- 但没有"哪些 harness 组件可被 agent 自动编辑 vs 需要人工审核"的显式分类 ✗
- AGENTS.md 的哪些部分是不变的约束、哪些是可演化的策略，没有区分 ✗

**Experience observability**：弱覆盖
- harness-feedback-ledger 有 episode 记录 ✓
- 但 episode 是文字摘要，不是 trajectory token 级的结构化数据 ✗
- 没有"失败率、纠偏频率、重复失守次数"等量化指标 ✗
- DocCustomeranalysis 60+ active episodes 没有任何 closed/deprecated，无法判断哪些已被真正解决 ✗

**Decision observability**：几乎没有覆盖
- harness 变更时没有 self-declared prediction ✗
- 没有"本次规则升级预期减少 X 类错误"的预测记录 ✗
- 没有事后验证"本次升级是否真的减少了该类错误"的机制 ✗

**结论**：当前系统声称 H5 maturity，但按 AHE 标准，只达到了 **H3（可执行反馈 + 部分 episode 记录）**，未达到真正的可观测自演进（H4-H5）。

---

## 第五层：Agent 权限边界的安全现实

### 行业数据

2026 年安全研究数据：
- **只有 8% 的组织**表示 AI agent 从未超过预期权限
- **53% 表示 agent 偶尔或有时超出权限**

这个数据与当前系统的 episode 记录完全吻合：DocCustomeranalysis 有 3+ 条"外部子工程写入边界失守"的 episode，用于修复该问题的机制是：自然语言规则 → sensor 事后检查 → finalizer 事后拦截。

问题是：这三层全部是**事后**机制。数据说明自然语言规则（第一层）对 53% 的情况是无效的。

### 行业解决方向

2026 年的工程实践趋势：

1. **Kernel-level enforcement**：`make-trust-irrelevant` 项目的思路——用内核级权限系统替代规则声明，让"不信任"变成系统默认而非配置选项
2. **多层次边界**：网络层（agent 只能访问特定网段）→ 应用层（限制 agent 在特定应用内的能力）→ 数据层（字段级访问控制）
3. **Least privilege + 时间约束**：有限权限 + agent identity + 基于时间的限制 + 明确的 blast radius

当前系统只有应用层部分覆盖（sensor + finalizer），没有网络层和数据层控制。对于"agent 是否能写子工程文件"的判断，仍然完全依赖 agent 在上下文中读到规则并自我约束。

---

## 综合诊断：六个根本性设计缺陷

### 缺陷 1：把"规则"当"程序"

从 Software 3.0 视角看，AGENTS.md 是 agent 执行的程序。当前系统把程序设计成自然语言长文，而不是有结构、有层次、可验证的规格。正确的设计是：P0 硬约束应该是 schema/type-level 约束，P1 策略应该是模板字段，P2 建议才是自然语言。

**根因**：把 harness 当文档写，而不是当工程系统设计。

### 缺陷 2：容错设计缺失

Karpathy 明确说 agent 是"spiky entities"。系统的响应是"如果 agent 犯错，加更严格的规则"。但随机实体不会因为规则更严格而变得可靠——它需要**容错架构**：当 agent 犯错时系统能自我修复，而不是积累更多规则。

**根因**：设计假设了可靠执行，没有为不可靠执行设计回退路径。

### 缺陷 3：Memory 未分层管理

当前系统的 memory 只有一个有效维度：BRAIN.md（语义 memory，static）。没有：
- 结构化 episodic memory（有检索能力的事件索引）
- Action-sensitive memory（权限、审批、有效期）
- Context budget 控制（working memory 边界）

**根因**：把所有 memory 都压到 AGENTS.md 里，导致上下文越来越重。

### 缺陷 4：Orchestrator 层缺失

当前的主控-子工程协调依赖人类作为 orchestrator。这意味着：跨工程任务的路由、状态同步、handoff 触发都需要用户手动完成。这既是效率瓶颈，也是错误源——用户不可避免地会遗漏、错判或延迟协调。

**根因**：把人类当 orchestrator 是当前阶段的现实，但系统没有设计向自动 orchestrator 演进的路径。

### 缺陷 5：Episode 没有闭环

60+ active episodes，零 closed。这说明系统只有"发现问题"和"加规则"两个动作，没有"验证修复是否有效"和"标记问题已解决"的闭环。这直接对应 AHE 的 Decision observability 缺失：没有 prediction + outcome verification。

**根因**：episode lifecycle 缺少终态设计。

### 缺陷 6：wiki 模板漂移无人监控

wiki 是所有工程的**模板源**——各工程从 wiki fork 出来后独立演化，wiki 不以 submodule 方式被引用，也不是运行时共享库。真正的问题不是"共享内核未落地"，而是：**wiki 的改进找不到路传播给各副本，各副本的教训也找不到路反哺 wiki**。

当前：wiki 做了修复（如 finalizer scope proof）时，其他工程不知道；DocCustomeranalysis 发现了 wiki 没有的问题，也靠人工记忆决定是否同步回 wiki。AcknowledgeBase 作为管理层有能力做漂移监控，但目前没有工具支撑这个角色。

**根因**：模板源和副本之间的变更流动没有被追踪，漂移是不可见的。

---

## 可行演进路径

### Phase 0（当前可做，不破坏现有系统）

**目标**：减轻认知负担，建立最小可验证约束。

1. **AGENTS.md 压缩**：三档分类执行（P0 ≤15行，P1 跳转链接，P2 进 Prune Queue）
2. **Episode 加终态**：给 ledger 加 `closed` / `superseded` 状态，每季度执行一次 prune
3. **Action-sensitive memory 字段**：在 BRAIN.md 或专用文件里为写入权限、审批状态加 expiry 字段
4. **Scope 声明前置**：复杂任务开始时强制声明 `allowed_write_roots`，作为 finalizer 的检查依据

### Phase 1（1-2 个月，需要少量工具改动）

**目标**：让 wiki 模板改进可被追踪，让 AcknowledgeBase 承担漂移监控角色。

1. **wiki TEMPLATE ZONE 分区**：显式标记哪些文件是平台级约定（脚本/模板骨架/核心路由规则），哪些是 wiki 专属业务内容；只有 TEMPLATE ZONE 变更才需要向各工程传播
2. **模板变更日志**：wiki 的 TEMPLATE ZONE 重要变更记录到独立日志，各工程可对照检查自己是否已跟进
3. **Decision observability 起步**：每次 harness 变更时记录 prediction（"预期效果"），下一次 episode 时验证
4. **跨工程 Episode 注册表**：在 AcknowledgeBase 建立，2+ 工程共现的模式自动晋升为平台级问题

### Phase 2（3-6 个月，架构级改动）

**目标**：从文档型治理转向结构化治理 + agent 辅助漂移管理。

1. **模块化规则版本化**：wiki 治理规则拆成独立 `.rule.md` 文件并版本化，各工程 AGENTS.md 声明引用版本号，漂移检测变成版本号对比而不是全文 diff
2. **AcknowledgeBase 漂移 agent**：由 AcknowledgeBase 的 agent 定期对比 wiki TEMPLATE ZONE 和各工程对应文件，生成漂移报告和 patch 建议，由用户决定是否应用
3. **Structured governance schema**：P0 约束用 JSON/YAML schema 定义，agent 读取结构化规格而非散文
4. **Context budget 可视化**：在每个工程建立 context size monitor，当 AGENTS.md 超出预算时触发精简告警

---

## 一句话总结

当前 agent 体系的根本矛盾是：**用文档治理的方式在管理一个需要工程治理的问题**。规则是文字，程序是结构；容错靠文字是幂零的，容错靠结构才能累积。wiki 是正确的模板源起点，AcknowledgeBase 是正确的管理层位置，但两者之间的变更流动机制是空白的——补上这个空白，比继续加密每个工程自己的规则更有杠杆。

---

## 参考文献

- Karpathy, A. (2026). Software 3.0 / Agentic Engineering, Sequoia AI Ascent. [MindStudio Blog](https://www.mindstudio.ai/blog/vibe-coding-vs-agentic-engineering-karpathy-framework)
- arXiv:2604.25850, Agentic Harness Engineering: Observability-Driven Automatic Evolution
- arXiv:2403.16971, AIOS: LLM Agent Operating System
- CoALA Framework (2025), Memory for Autonomous LLM Agents
- Mem0 (2026), Semantic Memory Layer for AI Agents
- Cloud Security Alliance (2026), AI Agent Security Starts with Scope Control
- Fowler, M. (2026), Harness Engineering for Coding Agent Users
- [[articles/2026-05-25-harness-engineering-research]]
- [[articles/2026-05-28-openclaw-memory-system-research]]
- [[articles/2026-05-25-codex-goals-research]]
