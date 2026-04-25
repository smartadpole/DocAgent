---
type: codebase
id: CODEBASE-001
project: wiki
status: optional
stage: analysis
source_of_truth: false
updated: 2026-04-25
tags: [project, codebase]
---

# 代码基线

这页是现实实现或既有工程的审计入口。

如果当前项目是从已有代码、外部模板、旧系统或第三方工程接手而来，就用这里把现实实现和目标设计分开收口。

## 这页负责什么

- 记录当前代码事实
- 挂页面图、schema 图、基础设施图、冲突清单和复用边界
- 给“设计与实现差异对齐”和后续接入策略提供稳定上下文
- 把可复用资产和实现漂移分开

## 这页不负责什么

- 不定义主需求、主设计或最终技术路线，那是 [[projects/requirements]]、[[projects/trace]]、[[projects/design/README]] 和 [[projects/decisions]] 的职责
- 不让现有代码直接反向改写主工程口径
- 不重复写完整设计正文
- 不把未来迁移意图伪装成当前事实

## 子页

- [[projects/codebase/page-map]]：路由、页面家族、布局壳、角色入口和主流程
- [[projects/codebase/schema-map]]：表、字段、状态、写入口、RPC 和生成类型
- [[projects/codebase/infra]]：部署、服务、脚本、观测、压测和回滚
- [[projects/codebase/conflicts]]：冲突、逻辑问题和实现风险
- [[projects/codebase/reuse-boundary]]：可继承主体、可复用模块和仅作参考的部分

## 读取顺序

1. 先看 [[projects/requirements]]、[[projects/trace]] 和 [[projects/design/README]]，确认目标系统要做成什么。
2. 再看这页，确认现实实现现在长什么样。
3. 再看 [[projects/codebase/page-map]] 和 [[projects/codebase/schema-map]]，把页面、数据和写入口放平。
4. 再看 [[projects/codebase/conflicts]]，把冲突、漂移和 bug 收口。
5. 再看 [[projects/codebase/reuse-boundary]]，决定哪些能继承、哪些只能参考。
6. 最后回到 [[projects/decisions]] 和 [[projects/development/README]]，把差异收成接入策略和功能点拆解。

## 维护说明

- 如果现实实现和主线需求 / 设计冲突，先记到 [[projects/codebase/conflicts]]，再升级到 [[projects/decisions]]。
- 如果代码事实已经被确认能复用，再写到 [[projects/codebase/reuse-boundary]]。
- 如果代码审计产生了可跨项目复用的方法，再沉淀到 `concepts/` 或 `articles/`。
