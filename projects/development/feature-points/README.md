---
type: feature_points
id: DEV-FP-INDEX-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-10
tags: [development, feature-points]
---

# 功能点实体目录

主入口：[[projects/development/README]]  \
配套：[[projects/development/worklog]]

这页是工程师视角的执行目录，不承载多个功能点正文。每个功能点一页，`status` 和 `phase` 写在各自页面的 frontmatter 里。
同一个功能点只对应一个文件，状态变化只改同一页的 frontmatter。
这页负责单个功能点的执行、验收和结果，不负责整体排期和跨功能点协调。

## 约定

- 一页一个功能点实体
- 功能点页里同时写 `status` 和 `phase`
- 目录页只列清单和跳转，不重复写实体正文
- `status` 看生命周期，`phase` 看串联步骤
- `blocked` 是叠加态，不是单独一条流程
- 旧的 `in_progress` 统一拆成 `status=active + phase=*`

## 状态轴

- `planned`：已列入计划，还没进入执行
- `active`：已经进入当前推进链路
- `blocked`：当前链路被外部依赖或未决问题卡住
- `done`：开发和验证完成，等待收口或发布
- `released`：已经发布或对外可用
- `archived`：不再活跃但保留历史

## 阶段轴

- `design`：问题定义、方案拆分、边界确认
- `implementation`：编码、联调、实现修改
- `verification`：测试、回归、验收
- `release`：发布、观察、收口

## 单页模板

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

## 当前实体

下面按当前状态分组的是索引视图，不是目录拆分。

### 进行中

- [[projects/development/feature-points/FP-001]]：active / implementation

### 完成待发布

- [[projects/development/feature-points/FP-002]]：done / release

### 已发布

- [[projects/development/feature-points/FP-003]]：released / release
