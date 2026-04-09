---
type: development
id: DEV-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-09
tags: [development]
---

# 开发

这页是开发主入口。

上游：[[projects/design/README]]、[[projects/decisions]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/releases]]、[[projects/incidents/README]]

子页：

- [[projects/development/worklog]]

## 这页负责什么

- 说明当前开发状态
- 维护活跃功能点清单和状态
- 说明阻塞和风险
- 说明下一步
- 汇总需要关注的验证项

## 功能点推进

设计拆成模块以后，这页就是当前活跃功能点的工作台。

### 状态词

- `planned`：已列入计划，还没补齐设计或验收
- `designed`：设计和边界已明确
- `ready`：依赖、验收和实现路径都准备好了
- `in_progress`：正在实现
- `blocked`：被外部依赖或未决问题卡住
- `review`：实现完成，正在验证
- `done`：验证通过，准备归档或进入发布
- `released`：已经发布或对外可用
- `archived`：不再活跃但保留历史
- `canceled` / `superseded`：被取消或被替代

### 卡片模板

```md
#### FP-001 | 功能点名称
- 模块：
- 状态：planned
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

### 示例

#### FP-001 | 为项目状态页补功能点状态镜像

- 模块：项目运行层
- 状态：in_progress
- 目标：把模块 -> 功能点 -> 状态 -> 记录 -> 发布这条链路固定下来
- 范围：`projects/status.md`、`projects/development/README.md`、`projects/development/worklog.md`
- 验收：读者能按模板登记一个功能点，并知道状态如何推进
- 负责人：team
- 下一步：把活跃页面按模板补齐
- 阻塞：暂无
- 相关设计：[[projects/design/README]]
- 相关决策：[[projects/decisions]]
- 过程日志：[[projects/development/worklog]]
- 发布/事故：视实现结果补到 [[projects/releases]] 或 [[projects/incidents/README]]
- 结果：待完成后补充

### 维护方式

- 这页保留当前活跃功能点清单，完成后移到归档区，或在同页标成 `done`
- 过程流水写到 [[projects/development/worklog]]
- 关键取舍写到 [[projects/decisions]]
- 可复用结论写到 [[projects/memory/README]] 或知识库层

## 当前内容

按需要补充：

- 活跃功能点清单
- 当前状态
- 当前分支或关联 PR/Issue
- 当前阻塞
- 测试关注点
- 下一步

## 维护说明

- 开发推进时如果发现项目记忆、规则边界或决策发生变化，先回写到 [[projects/memory/README]]、[[POLICY]] 和 [[projects/decisions]]
- 功能点状态发生变化时，同步更新 [[projects/status]] 和 [[projects/development/worklog]]；如果已经发布，再看 [[projects/releases]]
- 开发页只记录推进过程，不重复写设计正文
