---
type: status
id: STATUS-001
project: PROJ-WIKI-001
status: active
stage: design
source_of_truth: true
updated: 2026-04-25
next_action: slim-development-manager-view
current_entry: projects/README.md
blockers:
  - remaining-page-normalization
tags: [status]
---

# 项目状态

这页是 [[projects/README]] 的状态镜像，适合给人和 agent 快速读取当前阶段、下一步、阻塞项和活跃功能点。

## 当前状态

- 状态：active
- 阶段：design
- 当前主入口：[[projects/README]]

## 下一步

- 把项目主页、开发主入口、会议主入口和功能点实体目录的职责分层进一步收口
- 继续把高频页面的链接和字段收敛成机器可读格式
- 如果某个结论已经稳定，再回写到 [[projects/memory/README]] 或知识库层

## 功能点镜像

功能点正文以 [[projects/development/feature-points/README]] 和实体页为准，这里只放当前状态镜像。

## 功能点状态维护

- 这页只保留全局状态镜像，不展开所有功能点细节
- 整体推进看 [[projects/development/README]]
- 实体模板和活跃实体清单看 [[projects/development/feature-points/README]]
- 过程流水看 [[projects/development/worklog]]
- 正式会议看 [[projects/meetings/worklog]]
- 功能点用 `status` + `phase` 双轴管理
- `status` 看生命周期：`planned`、`active`、`blocked`、`done`、`released`、`archived`
- `phase` 看串联步骤：`design`、`implementation`、`verification`、`release`
- 旧的 `in_progress` 口径以后统一拆成 `status=active + phase=*`
- 功能点实体页一页一个功能点，`status` 和 `phase` 写在各自页的 frontmatter
- 被取消或被替代的功能点，分别标成 `canceled` 或 `superseded`
- 切状态时，先更新功能点实体页，再回看发布、事故和记忆是否需要同步

### 进行中

- [[projects/development/feature-points/FP-001]]：active / implementation

### 完成待发布

- [[projects/development/feature-points/FP-002]]：done / release

### 已发布

- [[projects/development/feature-points/FP-003]]：released / release

## 维护说明

- 状态变化前先读 [[projects/README]]。
- 功能点状态变化时，同步对应功能点页、[[projects/development/README]] 和这里。
- 如果状态变化反映了需求范围、设计口径或决策变化，再同步 [[projects/trace]] 和 [[projects/decisions]]。

## 阻塞项

- 还没有把更大范围的页面批量规范化
