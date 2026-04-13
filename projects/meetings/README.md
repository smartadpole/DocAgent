---
type: meetings
id: MEET-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-13
tags: [meetings, project]
---

# 会议

这页是项目侧的会议主入口。

当会议很多、而且会前材料、纪要、行动项和回看都需要稳定收口时，就用这里做总入口。
正式会议优先放这里；开发过程里的临时讨论，仍然可以直接记到 [[projects/development/worklog]]。

上游：[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[WORKFLOW]]  \
下游：[[projects/meetings/worklog]]、[[projects/trace]]、[[projects/decisions]]、[[projects/development/worklog]]、[[projects/memory/README]]

## 这页负责什么

- 统一会议材料的落点
- 统一正式会议的记录入口
- 统一会后分流：决策、需求收敛、开发动作和稳定背景
- 统一会议相关的最小规则和流程入口

## 这页不负责什么

- 不放原始录音、截图和外部附件本体，那些优先进 `raw/` 或 `assets/`
- 不替代 [[projects/decisions]] 的拍板正文
- 不替代 [[projects/trace]] 的需求收敛链
- 不替代 [[projects/development/worklog]] 的实现、排障和验证流水

## 固定流程

1. 会前先收集议程、背景、待确认问题和相关链接。
2. 会中只记录结论、风险、行动项和需要继续确认的问题。
3. 会后按结果分流：
   - 拍板和取舍进 [[projects/decisions]]
   - 需求变化和范围收敛进 [[projects/trace]]
   - 开发动作和验证进 [[projects/development/worklog]]
   - 稳定背景进 [[projects/memory/README]]
4. 如果某类会议开始反复出现，再把固定字段继续收紧成模板或索引。

## 当前子页

- [[projects/meetings/worklog]]：按时间顺序记录正式会议

## 规则来源

- [[WORKFLOW]]：会议材料怎么收、怎么记、怎么分流
- [[projects/decisions]]：会议里的正式拍板
- [[projects/trace]]：会议里推动的需求收敛
- [[projects/development/worklog]]：会议里推动的实现动作
