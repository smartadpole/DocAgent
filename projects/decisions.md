---
type: decision-log
id: DECISION-LOG-001
project: PROJ-WIKI-001
status: active
priority: high
updated: 2026-04-10
tags: [decision]
---

# 决策

这页是决策主文件。

上游：[[projects/requirements]]、[[projects/design/README]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/development/README]]、[[projects/releases]]、[[projects/incidents/README]]

## 这页负责什么

- 记录关键取舍
- 说明为什么选这个方案
- 说明为什么不选其他方案
- 记录当时约束和影响
- 承接项目阶段的思维碰撞和冲突升级

## 当前内容

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

### 2026-04-10 功能点推进采用小卡片状态机

- 背景：设计拆到模块之后，推进粒度需要落到功能点，否则状态、阻塞和验证会散落在多个页面里。
- 决定：
  - 以功能点作为最小执行单位
  - 用 [[projects/development/README]] 维护模板和活跃清单
  - 用 [[projects/development/worklog]] 维护过程流水
  - 用 [[projects/status]] 维护全局状态镜像
  - 用 [[projects/releases]] 维护完成和发布结果
  - 用 [[projects/incidents/README]] 维护异常和复盘
- 影响：
  - 新功能先登记功能点卡片，再进入实现
  - 状态词统一，避免每页各写一套
  - 稳定结果按层回写到记忆、决策或知识库层

## 维护说明

- 如果后续发生新的结构冲突或规则冲突，优先写到这里，再回写到 [[BRAIN]]、[[POLICY]] 或项目主入口
- 决策页只写拍板结果，不重复写需求和设计全文
