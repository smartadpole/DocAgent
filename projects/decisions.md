---
type: decision-log
id: DECISION-LOG-001
project: PROJ-WIKI-001
status: active
priority: high
updated: 2026-05-25
tags: [decision]
---

# 决策

这页是决策主文件。

上游：[[projects/requirements]]、[[projects/trace]]、[[projects/design/README]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/development/README]]、[[projects/releases]]、[[projects/incidents/README]]

## 这页负责什么

- 记录关键取舍
- 说明为什么选这个方案
- 说明为什么不选其他方案
- 记录当时约束和影响
- 承接项目阶段的思维碰撞和冲突升级
- 为需求演进链提供正式拍板节点，不重复承接整条需求收敛过程

## 当前生效决策摘要

1. [[projects/decisions#2026-05-25 Gate / FP / EP / TASK 成为研发事项默认主链|Gate / FP / EP / TASK 成为研发事项默认主链]]：risk、Issue、test、验收、报告和服务台账作为关系节点接入。影响：不能再用单个 TODO 或报告替代 EP / TASK / Gate 闭环。
2. [[projects/decisions#2026-05-25 响应模式路由成为 wiki Harness 默认入口|响应模式路由成为 wiki Harness 默认入口]]：每轮先判快速诊断、沉淀、验收、实现或规则升级。影响：简单问题先给 checkpoint，重治理闭环显式切换。
3. [[projects/decisions#2026-05-25 H5 自演进和本地 sensor 成为 Harness 默认支撑|H5 自演进和本地 sensor 成为 Harness 默认支撑]]：episode 先入 ledger，再按证据晋升。影响：规则不直接膨胀，优先补模板和 `scripts/check_all.py` sensor。
4. [[projects/decisions#2026-04-13 会议材料拆出到 meetings 模块|会议材料拆出到 meetings 模块]]：正式会议进入会议层。影响：会议纪要、行动项和会后分流不再默认写进开发 worklog。
5. [[projects/decisions#2026-04-10 功能点推进采用实体页状态机|功能点推进采用实体页状态机]]：功能点成为能力实体页。影响：执行闭环后续已由 EP / TASK 承接，FP 不再作为最小执行单位。
6. [[projects/decisions#2026-04-10 功能点改用 status + phase 双轴|功能点改用 status + phase 双轴]]：生命周期和推进阶段分开。影响：不再用单个 `in_progress` 表达所有状态。
7. [[projects/decisions#2026-04-10 项目、开发、功能点三层职责分工|项目、开发、功能点三层职责分工]]：项目负责人、研发经理和工程师视角分层。影响：方向、协调和执行正文不再混写。
8. [[projects/decisions#2026-04-09 分层 memory 落点|分层 memory 落点]]：共享背景、规则、项目记忆和决策分层。影响：稳定内容按作用域进入对应入口。

## 正式决策记录

### 2026-05-25 Gate / FP / EP / TASK 成为研发事项默认主链

- **背景**：用户明确要求完整吸收 `DocCustomeranalysis` 中 Gate、FP、EP、TASK、Issue、risk、test、验收和台账等工程设计。对照后确认，可复用部分是事项主链、关系节点、Issue / report 分工、验收执行包和服务台账规则，不是下游项目事实。
- **要决策什么**：是否把当前 wiki 的研发事项模型从“功能点 / TODO / 报告”升级为更完整的 `Gate -> FP -> EP -> TASK` 主链，并让 Issue、risk、test、验收和服务台账进入默认关闭守卫。
- **可选项**：
  - 只在回复里说明已经吸收。
  - 原样复制下游项目目录和业务规则。
  - 抽象为模板级研发事项系统，并补模板、入口和 sensor。
- **最终决策**：采用 `Gate -> FP -> EP -> TASK` 作为默认主链；risk、Issue、test、验收、报告和服务台账作为关系节点；新增 EP、TASK、Issue 入口和模板，并把 `work-item-matrix` 纳入 `scripts/check_all.py`。
- **影响**：
  - TASK 是父 EP 下的状态化交付合同，不能无父 EP 直接派发为正式编码任务。
  - Issue 是案件档案，报告是每次验证记录；报告不能替代 Issue，也不能自动上推关闭父项。
  - 验收和服务台账成为关闭守卫的一部分，尤其涉及真实服务、UI / API 配对、配置恢复和服务组验证时。
- **各自优劣**：
  - 只回复最快，但不会改变后续执行默认。
  - 原样复制最完整，但会带入项目事实和过重结构。
  - 抽象吸收需要同步更多入口，但能保留模板库边界，并由 sensor 约束关键 wiring。
- **风险点**：
  - 如果所有轻量任务都强制建 EP / TASK，会增加管理成本；因此 TODO 仍保留为轻量待办和过渡视图。
  - 如果 sensor 只查关键词，仍不能替代真实验收；因此 `work-item-matrix` 只检查系统 wiring，关闭结论仍按报告和人工确认边界执行。

### 2026-05-25 响应模式路由成为 wiki Harness 默认入口

- **背景**：[[articles/2026-05-25-agent-response-efficiency-governance-reflection]] 已经确认，当前系统的慢不应简单理解为治理多余；真正缺口是所有问题容易默认进入同一条重治理链，导致首次反馈慢、模式切换不清楚。
- **要决策什么**：是否把响应效率治理从知识沉淀候选升级为正式执行机制，并决定它的单一信息源和入口同步方式。
- **可选项**：
  - 继续只保留在文章里，作为后续参考。
  - 直接把长规则塞进 [[AGENTS]]。
  - 新增独立治理页做单一信息源，[[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 只保留短入口和硬边界。
- **最终决策**：新增 [[response-mode-routing]] 作为响应模式路由的单一信息源，并同步 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[skills/issue-analysis/SKILL]] 和 [[templates/harness-adoption-template]]。
- **影响**：
  - agent 每轮先判快速诊断、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
  - 快速诊断可以先给 `confirmed / likely / possible / blocked` checkpoint，但不能替代验收、关闭、准出或规则升级。
  - 治理闭环继续保留；进入沉淀、验收、规则升级或收尾时必须显式说明当前阶段。
- **各自优劣**：
  - 继续留在文章里最轻，但不会改变默认执行。
  - 写进 [[AGENTS]] 最容易被 agent 看到，但会让根入口继续膨胀。
  - 独立治理页需要同步多个入口，但最符合短入口和单一信息源原则。
- **风险点**：
  - 如果快速诊断被误用来关闭状态，会破坏验收边界；因此 [[POLICY]] 明确快速诊断默认不写状态、不关闭 TASK / EP / FP / Gate。
  - 如果后续只继续加自然语言规则，Harness 会变重；因此下一步优先补 feedback sensor 和模板校验。

### 2026-05-25 H5 自演进和本地 sensor 成为 Harness 默认支撑

- **背景**：用户指出同定位的 `DocCustomeranalysis` 工程在 Harness 设计和整体系统流程上更健全。对照后确认，可复用部分不是具体项目事实，而是 H5 自演进、episode ledger、统一本地门禁、工作阶段专项 sensor 和周期复盘模板。
- **要决策什么**：是否把这些能力从下游项目抽象吸收进当前 wiki 模板库，并决定它们的单一信息源。
- **可选项**：
  - 只在最终回复里总结差距。
  - 直接复制下游项目完整治理页和 CI 配置。
  - 抽象成模板级 H5 机制，保留当前库的 GitHub remote 和项目事实边界。
- **最终决策**：新增 [[harness-evolution]]、[[harness-feedback-ledger]]、[[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]]、`.codex/AGENTS.md`、`scripts/check_all.py` 和 `scripts/check_harness_governance.py`。
- **影响**：
  - 用户纠偏、检查失败、模式切换和重复失守先形成 episode 数据，不直接新增硬规则。
  - 工作阶段可以跑 `python3 scripts/check_all.py --only harness-governance`，收尾和提交前跑 `python3 scripts/check_all.py`。
  - 后续 sensor 扩展优先覆盖 Markdown / wikilink、frontmatter、技能质量和模板完整性。
- **各自优劣**：
  - 只总结最快，但无法改变后续执行。
  - 原样复制最完整，但会夹带 DocCustomeranalysis 的项目事实和 GitLab 平台假设。
  - 抽象吸收需要同步多个入口，但能保持模板库边界，并让规则减肥和 sensor 晋升形成闭环。
- **风险点**：
  - 如果 episode ledger 变成新流水账，会增加维护负担；因此 [[harness-feedback-ledger]] 只记录可反哺 Harness 的结构性信号。
  - 如果 `scripts/check_all.py` 长期只覆盖 Harness wiring，还不足以替代更广泛的文档质量检查；因此状态页保留 wider sensor coverage 作为后续缺口。

### 2026-04-13 会议材料拆出到 meetings 模块

- 背景：项目管理中的正式会议越来越多，如果继续把会议纪要和开发过程混写在 `projects/development/execution/worklog.md`，会把实现流水、会议结论和会后分流混成一层，后续检索和回看都会变难。
- 决定：
  - 新增 `projects/meetings/` 作为项目侧会议主入口
  - 正式会议的纪要、行动项和回看链接优先写到 [[projects/meetings/worklog]]
  - 开发过程的联调、排障、验证和临时同步继续留在 [[projects/development/execution/worklog]]
  - 会议组织规则和会后分流流程统一收进 [[governance/WORKFLOW]]
- 影响：
  - 后续正式会议不再默认写进开发 worklog
  - 如果会议结果已经形成拍板、需求收敛或实现动作，再分别回写到 [[projects/decisions]]、[[projects/trace]] 或 [[projects/development/execution/worklog]]
  - 项目主页、结构说明、状态页、开发入口、项目记忆页和总入口都要补上会议入口的链接

### 2026-04-09 分层 memory 落点

- 背景：当前 vault 已经具备入口层、治理层、共享背景层、项目层、知识层和历史层，需要把 memory 路由明确下来，避免后续继续把所有稳定内容都塞进 [[BRAIN]]。
- 决定：
  - [[BRAIN]] 只保留共享背景
  - [[POLICY]] 承接规则、优先级和自动沉淀边界
  - `projects/memory/` 承接项目级稳定记忆
  - [[projects/decisions]] 继续承接项目取舍
- 影响：
  - 以后新增稳定内容时，先判断它是背景、规则、项目记忆还是决策
  - 没有账号体系也可以靠 Git + 文档层级协作
  - 结构升级以小改为主，不推翻现有骨架

### 2026-04-10 功能点推进采用实体页状态机

- 背景：设计拆到模块之后，推进粒度需要落到功能点，否则状态、阻塞和验证会散落在多个页面里。
- 决定：
  - 以功能点作为当时的能力执行实体；2026-05-25 后，正式执行闭环升级为 `Gate -> FP -> EP -> TASK`，FP 不再作为最小执行单位
  - 用 [[projects/development/README]] 维护模板和活跃清单
  - 用 [[projects/development/feature-points/README]] 维护一页一个功能点的实体页
  - 用 [[projects/development/execution/worklog]] 维护过程流水
  - 用 [[projects/status]] 维护全局状态镜像
  - 用 [[projects/releases]] 维护完成和发布结果
  - 用 [[projects/incidents/README]] 维护异常和复盘
- 影响：
  - 新功能先登记功能点实体页，再进入实现
  - 功能点字段统一，避免每页各写一套
  - 功能点实体页一页一个功能点，避免同页放多个实体正文
  - 稳定结果按层回写到记忆、决策或知识库层

### 2026-04-10 功能点改用 status + phase 双轴

- 背景：`in_progress` 同时覆盖设计、实现和验证，无法清楚表达串联关系，也不利于区分进行中和已完成。
- 决定：
  - 用 `status` 表示生命周期
  - 用 `phase` 表示串联步骤
  - 旧 `in_progress` 口径拆成 `status=active + phase=*`
  - 活跃实体保留在开发入口的索引里，完成后转到发布或归档
- 影响：
  - 进行中和已完成可以用不同字段区分，不再靠一个词包住所有含义
  - 设计、实现、验证可以按阶段顺序推进并记录
  - 每个功能点实体页单独承载 `status` 和 `phase`
  - 如果功能点完成后又要修复，优先新开修复点或事故记录，保留原卡的完成状态

### 2026-04-10 项目、开发、功能点三层职责分工

- 背景：`projects/README.md`、`projects/development/README.md` 和 `projects/development/feature-points/README.md` 之前都在解释功能点和状态，容易让读者把协调层和执行层混在一起。
- 决定：
  - `projects/README.md` 承担 CTO / 项目负责人视角，负责方向、边界、优先级和最终拍板
  - `projects/development/README.md` 承担研发经理视角，负责整体推进、状态镜像、阻塞协调和下一步
  - `projects/development/feature-points/README.md` 和其下实体页承担工程师视角，负责单个功能点执行、验证和结果
- 影响：
  - 以后写文档时，先判断是在定方向、做协调，还是在做单个功能点执行
  - 功能点正文只放在实体页里，不再和开发主入口混写
  - 状态分组是索引视图，不是目录结构

## 维护说明

- 如果后续发生新的结构冲突或规则冲突，优先写到这里，再回写到 [[BRAIN]]、[[POLICY]] 或项目主入口
- 如果拍板改变了当前实现范围或替换了既有口径，记得同步回写 [[projects/trace]]
- 新增正式决策默认参考 [[templates/decision-entry-template]]
- 决策页默认用“当前生效决策摘要 -> 正式决策记录 -> 已覆盖 / 历史决策”的单页结构，不为每条决策先拆详情目录
- 决策页记录正式拍板和比较过程，不重复写需求和设计全文
