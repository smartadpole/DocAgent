---
type: example
id: DEV-EX-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-10
tags: [development, examples]
---

# 开发示例

主入口：[[projects/development/README]]  \
配套：[[projects/development/worklog]]

这页只放可直接复制的示例，不承载真实进度。

## 示例 1：功能点卡片

#### FP-001 | 为项目状态页补功能点状态镜像

- 模块：项目运行层
- 状态：in_progress
- 目标：把模块 -> 功能点 -> 状态 -> 记录 -> 发布这条链路固定下来
- 范围：[[projects/status]]、[[projects/development/README]]、[[projects/development/worklog]]
- 验收：读者能按模板登记一个功能点，并知道状态如何推进
- 负责人：team
- 下一步：把活跃页面按模板补齐
- 阻塞：暂无
- 相关设计：[[projects/design/README]]
- 相关决策：[[projects/decisions]]
- 过程日志：[[projects/development/worklog]]
- 发布/事故：视实现结果补到 [[projects/releases]] 或 [[projects/incidents/README]]
- 结果：待完成后补充

## 示例 2：过程记录

- 2026-04-10 10:30
  - 功能点：FP-001 为项目状态页补功能点状态镜像
  - 模块：项目运行层
  - 状态变化：planned -> in_progress
  - 做了什么：补齐开发入口的模板、状态词和示例
  - 发现了什么：功能点卡片和时间流水需要分层维护，不能混在同一段正文里
  - 如何验证：读者可以从模板复制一张卡，并知道要同步更新哪些页面
  - 阻塞：暂无
  - 下一步：把活跃页面按模板补齐
  - 关联链接：[[projects/development/README]]、[[projects/status]]
