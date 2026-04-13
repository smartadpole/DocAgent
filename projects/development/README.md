---
type: development
id: DEV-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-13
tags: [development]
---

# 开发

这页是研发经理视角的开发主入口。

上游：[[projects/design/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/releases]]、[[projects/incidents/README]]

子页：

- [[projects/development/feature-points/README]]
- [[projects/development/worklog]]
- [[projects/meetings/README]]

## 这页负责什么

- 说明当前研发推进状态
- 说明阻塞和风险
- 说明下一步
- 汇总需要关注的验证项
- 维护活跃功能点的索引入口，不写单个功能点的完整执行正文

## 功能点推进

设计拆成模块以后，这页只负责整体研发推进和协调。
功能点的执行正文、状态字段和阶段字段都放到 [[projects/development/feature-points/README]] 及其下实体页。

研发经理负责拆解、协调、排期和跟进，不负责重复写单个功能点的执行正文。

### 维护方式

- 这页只保留整体推进状态、阻塞和下一步
- 具体功能点的 `status`、`phase` 和正文都只改对应实体页，不在这里重复维护
- 过程流水写到 [[projects/development/worklog]]
- 正式会议纪要和行动项写到 [[projects/meetings/worklog]]
- 需求为什么这样收敛、哪些修补属于实现纠偏，优先回看 [[projects/trace]]
- 关键取舍写到 [[projects/decisions]]
- 可复用结论写到 [[projects/memory/README]] 或知识库层

## 当前关注点

按需要补充：

- 当前阻塞
- 测试关注点
- 下一步

## 维护说明

- 开发推进时如果发现项目记忆、规则边界或决策发生变化，先回写到 [[projects/memory/README]]、[[POLICY]] 和 [[projects/decisions]]
- 功能点状态发生变化时，同步更新对应实体页、[[projects/status]] 和 [[projects/development/worklog]]；如果已经发布，再看 [[projects/releases]]
- 开发页只记录推进过程，不重复写设计正文
