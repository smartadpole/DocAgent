---
type: decision-log
id: DECISION-LOG-001
project: PROJ-WIKI-001
status: active
priority: high
updated: 2026-04-25
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

1. [[projects/decisions#2026-04-13 会议材料拆出到 meetings 模块|会议材料拆出到 meetings 模块]]：正式会议进入会议层。影响：会议纪要、行动项和会后分流不再默认写进开发 worklog。
2. [[projects/decisions#2026-04-10 功能点推进采用实体页状态机|功能点推进采用实体页状态机]]：功能点成为最小执行单位。影响：执行正文、状态和验证结果收口到功能点实体页。
3. [[projects/decisions#2026-04-10 功能点改用 status + phase 双轴|功能点改用 status + phase 双轴]]：生命周期和推进阶段分开。影响：不再用单个 `in_progress` 表达所有状态。
4. [[projects/decisions#2026-04-10 项目、开发、功能点三层职责分工|项目、开发、功能点三层职责分工]]：项目负责人、研发经理和工程师视角分层。影响：方向、协调和执行正文不再混写。
5. [[projects/decisions#2026-04-09 分层 memory 落点|分层 memory 落点]]：共享背景、规则、项目记忆和决策分层。影响：稳定内容按作用域进入对应入口。

## 正式决策记录

### 2026-04-13 会议材料拆出到 meetings 模块

- 背景：项目管理中的正式会议越来越多，如果继续把会议纪要和开发过程混写在 `projects/development/worklog.md`，会把实现流水、会议结论和会后分流混成一层，后续检索和回看都会变难。
- 决定：
  - 新增 `projects/meetings/` 作为项目侧会议主入口
  - 正式会议的纪要、行动项和回看链接优先写到 [[projects/meetings/worklog]]
  - 开发过程的联调、排障、验证和临时同步继续留在 [[projects/development/worklog]]
  - 会议组织规则和会后分流流程统一收进 [[governance/WORKFLOW]]
- 影响：
  - 后续正式会议不再默认写进开发 worklog
  - 如果会议结果已经形成拍板、需求收敛或实现动作，再分别回写到 [[projects/decisions]]、[[projects/trace]] 或 [[projects/development/worklog]]
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
  - 以功能点作为最小执行单位
  - 用 [[projects/development/README]] 维护模板和活跃清单
  - 用 [[projects/development/feature-points/README]] 维护一页一个功能点的实体页
  - 用 [[projects/development/worklog]] 维护过程流水
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
