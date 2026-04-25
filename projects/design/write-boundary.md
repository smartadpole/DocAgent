---
type: design
id: DES-WRITE-001
project: wiki
status: optional
stage: design
updated: 2026-04-25
tags: [design, write-boundary]
---

# 写操作边界

主入口：[[projects/design/README]]

这里记录哪些写动作可以留在平台层，哪些必须进入业务后端、服务端动作或受控流程。

## 当前内容

- 轻量写白名单：
- 必须受控的写操作：
- 跨表事务：
- 审计和消息：
- 页面动作映射：
- 改造优先级：

## 维护说明

- 写操作边界要和 [[projects/design/permission-boundary]]、[[projects/design/database]] 同步。
- 如果既有工程里存在不符合边界的写法，先记到 [[projects/codebase/conflicts]]。
