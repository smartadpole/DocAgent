---
type: status
id: STATUS-001
project: PROJ-WIKI-001
status: active
stage: design
source_of_truth: true
updated: 2026-04-10
next_action: normalize-feature-point-pages
current_entry: projects/README.md
blockers:
  - remaining-page-normalization
tags: [status]
---

# 项目状态

## 当前状态

- 状态：active
- 阶段：design
- 当前主入口：[[projects/README]]

## 下一步

- 把活跃功能点按模板补到 [[projects/development/README]]
- 继续把高频页面的链接和字段收敛成机器可读格式
- 如果某个结论已经稳定，再回写到 [[projects/memory/README]] 或知识库层

## 功能点状态维护

- 这页只保留全局状态镜像，不展开所有功能点细节
- 详细模板和活跃清单看 [[projects/development/README]]
- 过程流水看 [[projects/development/worklog]]
- 状态词统一使用：`planned`、`designed`、`ready`、`in_progress`、`blocked`、`review`、`done`、`released`、`archived`
- 被取消或被替代的功能点，分别标成 `canceled` 或 `superseded`
- 切状态时，先更新功能点卡片，再回看 release、incident 和 memory 是否需要同步

## 阻塞项

- 还没有把更大范围的页面批量规范化
