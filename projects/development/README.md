---
type: development
id: DEV-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-10
tags: [development]
---

# 开发

这页是开发主入口。

上游：[[projects/design/README]]、[[projects/decisions]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/releases]]、[[projects/incidents/README]]

子页：

- [[projects/development/feature-points/README]]
- [[projects/development/worklog]]

## 这页负责什么

- 说明当前开发状态
- 维护活跃功能点实体的索引和状态
- 说明阻塞和风险
- 说明下一步
- 汇总需要关注的验证项

## 功能点推进

设计拆成模块以后，这页就是当前活跃功能点的工作台。
每个功能点单独一页，状态和阶段写在该页 frontmatter 里。

### 双轴模型

- `status` 只看生命周期，回答这张卡是不是还活跃
- `phase` 只看串联步骤，回答这张卡现在走到哪一步
- 每个功能点实体页都要同时写 `status` 和 `phase`
- `projects/development/feature-points/` 里一页只放一个功能点
- `blocked` 是叠加态，不是单独一条流程
- 旧的 `in_progress` 以后统一拆成 `status=active + phase=*`

### 状态轴

- `planned`：已列入计划，还没进入执行
- `active`：已经进入当前推进链路
- `blocked`：当前链路被外部依赖或未决问题卡住
- `done`：开发和验证完成，等待收口或发布
- `released`：已经发布或对外可用
- `archived`：不再活跃但保留历史

### 阶段轴

- `design`：问题定义、方案拆分、边界确认
- `implementation`：编码、联调、实现修改
- `verification`：测试、回归、验收
- `release`：发布、观察、收口

### 实体模板

```md
---
type: feature_point
id: FP-001
project: PROJ-WIKI-001
status: active
phase: implementation
updated: 2026-04-10
tags: [development, feature-point]
---

# FP-001 | 功能点名称

- 模块：
- 目标：
- 范围：
- 验收：
- 负责人：
- 下一步：
- 阻塞：
- 相关设计：
- 相关决策：
- 过程日志：
- 发布/事故：
- 结果：
```

### 当前实体

- [[projects/development/feature-points/README]]：功能点实体目录，一页一个功能点

#### 进行中

- [[projects/development/feature-points/FP-001]]：active / implementation

#### 完成待发布

- [[projects/development/feature-points/FP-002]]：done / release

#### 已发布

- [[projects/development/feature-points/FP-003]]：released / release

### 维护方式

- 这页保留当前活跃功能点的索引和状态，完成后只改对应实体页，不要把多个功能点正文塞进同一页
- 如果某个功能点卡在某一步，就只改该页的 `status` 为 `blocked`，`phase` 保留当前阶段
- 如果 `phase` 从 `design` 推进到 `implementation` 或 `verification`，就在同一功能点页更新，不要新开另一页
- 过程流水写到 [[projects/development/worklog]]
- 关键取舍写到 [[projects/decisions]]
- 可复用结论写到 [[projects/memory/README]] 或知识库层

## 当前关注点

按需要补充：

- 当前状态和阶段
- 当前分支或关联 PR/Issue
- 当前阻塞
- 测试关注点
- 下一步

## 维护说明

- 开发推进时如果发现项目记忆、规则边界或决策发生变化，先回写到 [[projects/memory/README]]、[[POLICY]] 和 [[projects/decisions]]
- 功能点状态发生变化时，同步更新对应实体页、[[projects/status]] 和 [[projects/development/worklog]]；如果已经发布，再看 [[projects/releases]]
- 开发页只记录推进过程，不重复写设计正文
