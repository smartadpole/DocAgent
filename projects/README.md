---
type: project
id: PROJ-WIKI-001
project: wiki
status: active
stage: design
next_action: define-policy-and-memory-routing
owner: team
source_of_truth: true
updated: 2026-04-10
tags: [project]
---

# 项目层

这里放软件研发模式下的项目运行文档。

## 和知识库模式的关系

- 知识库模式是底座，负责长期沉淀和复用。
- 研发模式是叠加层，负责项目推进和阶段管理。
- 项目里的稳定结论，最终要回写到知识库层。
- 项目里的上下文、一次性决策和阶段记录，留在项目层即可。
- 项目级稳定记忆放在 [[projects/memory/README]]。
- 共享背景放在 [[BRAIN]]。
- 规则和优先级放在 [[POLICY]]。

这两层不是并排摆放，而是有演进关系：

- 外部来源先进 `raw/` 或 `inbox/`
- 当前项目正在使用和判断的内容进入 `projects/`
- 已经稳定、能复用的结论再进入 `articles/`、`concepts/`、`indexes/`
- 不再承担当前入口职责但仍有历史价值的内容进入 `archive/`

## 默认运行方式

- 一个 `wiki` 只对应一个项目，所以项目主页固定是 `projects/README.md`
- 项目主页更像 CTO / 项目负责人视角，负责定方向、边界、优先级和最终拍板
- 当前规模很小，先保持单库、强规范、弱权限、强链接、可编排
- 没有账号体系也没关系，Git 已经足够承担审计和回滚
- 不做隐藏自动流控，状态由人读项目主页后手动判断

## 极简版本

极简模式最小只需要这两个东西：

- `projects/README.md`
- 根目录 `log.md`

其余文件都按需添加，不要为了完整性先建空文件。

## 这层不负责什么

- 不把项目上下文直接混进 `articles/`、`concepts/` 或 `indexes/`
- 不把可复用知识长期留在项目层
- 不把共享背景长期堆在这里，那是 [[BRAIN]]
- 不把规则和优先级长期堆在这里，那是 [[POLICY]]

## 结构主说明

- `projects/README.md` 只做项目层入口。
- 项目层的目录设计、文件职责、依赖关系和读取顺序，统一看 [[projects/STRUCTURE]]。
- 详细推进步骤和 AI 功能研发闭环，统一看 [[WORKFLOW]] 的 `1.9 软件研发模式`。

## 常用页面

- [[projects/README]]：项目运行层主入口。这里放目标、状态、关键链接和下一步。
- [[projects/status]]：项目状态页。这里放当前阶段、活跃功能点双轴状态镜像和当前主入口。
- [[projects/STRUCTURE]]：项目层结构主说明。这里放目录、文件、依赖和读取顺序。
- [[projects/requirements]]：需求主文件。这里放问题定义、范围、非目标和验收标准。
- [[projects/design/README]]：设计主入口。这里放设计总览，并链接架构和数据库子页。
- [[projects/design/memory/README]]：memory 研究层入口。这里放研究稿、工具调研和运行层设计草稿。
- [[projects/decisions]]：决策主文件。这里放关键取舍和 ADR 风格记录。
- [[projects/development/README]]：开发主入口。这里放研发经理视角的整体推进、状态镜像、阻塞和下一步。
- [[projects/development/feature-points/README]]：功能点实体目录。这里放工程师视角的单功能点执行页和状态索引。
- [[projects/development/worklog]]：开发过程记录。这里放时间顺序的实现、验证和排障流水。
- [[projects/releases]]：发布主文件。这里放上线范围、验证和回滚。
- [[projects/incidents/README]]：事故总览。这里放事故状态、索引和共性改进项。
- [[projects/memory/README]]：项目级稳定记忆入口。这里放项目长期背景和路由。
- [[POLICY]]：规则、优先级和 memory 路由。
- [[BRAIN]]：共享背景和共同前提。

## 什么时候再拆

- 项目主页已经装不下，并且某一类内容开始持续增长。
- 同一类信息会反复被查，比如需求、设计、发布或项目记忆。
- 你希望某类内容有独立历史，比如决策记录或事故复盘。

## 什么时候不拆

- 当前内容很少，项目主页一页就能看完。
- 某类内容只是一次性记录，不会复用。
- 拆出去之后反而需要来回跳转才能看明白。

## 手动流控

- 建议项目级状态词：`idea`、`active`、`blocked`、`released`、`archived`
- 功能点细化用 [[projects/development/feature-points/README]] 里的实体页；每页一个功能点，`status` 和 `phase` 写在 frontmatter
- 每次切状态前先读项目主页
- 如果多个文档冲突，以项目主页和 `projects/decisions.md` 为准
- 如果项目结束，把可复用内容提炼回知识库，把项目特有内容保留在项目目录或归档层
