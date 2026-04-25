---
type: design
id: DES-001
project: PROJ-WIKI-001
status: active
stage: design
updated: 2026-04-25
tags: [design]
---

# 设计

这页是设计主入口。

上游：[[projects/README]]、[[projects/requirements]]、[[projects/trace]]  \
下游：[[projects/decisions]]、[[projects/development/README]]

相关：[[projects/memory/README]]、[[POLICY]]

完整架构包子页：

- [[projects/design/tech-selection]]
- [[projects/design/architecture]]
- [[projects/design/backend-frontend-structure]]
- [[projects/design/permission-boundary]]
- [[projects/design/write-boundary]]
- [[projects/design/database]]
- [[projects/design/deployment]]
- [[projects/design/runtime-quality]]
- [[projects/design/memory/README]]

设计专题目录：

- [[projects/design/topics/README]]

## 这页负责什么

- 说明整体方案
- 说明模块划分
- 说明接口和数据流
- 说明如何把已经收敛的 PRD / 需求翻成可实现方案
- 说明设计总览，并链接技术选型、架构、工程结构、权限边界、写操作边界、数据库、部署和运行质量子页
- 说明哪些未拍板但重要的设计问题，已经被收成独立专题页
- 说明 memory 路由和 policy 接线应该如何落到项目结构里
- 承接需求演进链当前生效的范围和约束，把它落成可实现方案

相关方法：[[concepts/prd-writing]]

## 完整架构包

当前完整软件架构包默认由这 8 张主设计页组成：

1. [[projects/design/tech-selection]]：先看为什么选这条底座，不选什么。
2. [[projects/design/architecture]]：再看业务模块、页面、动作、状态机和权限边界。
3. [[projects/design/backend-frontend-structure]]：再把业务架构落到前后端模块和接口约定。
4. [[projects/design/permission-boundary]]：再看权限真相源、角色可见性和业务授权边界。
5. [[projects/design/write-boundary]]：再看哪些写动作可以留在平台层、哪些必须统一走受控后端。
6. [[projects/design/database]]：再看数据模型、约束、索引和迁移边界。
7. [[projects/design/deployment]]：再看环境、部署拓扑、发布和回滚。
8. [[projects/design/runtime-quality]]：最后看监控、告警、幂等、重试、补偿和运行稳定性。

[[projects/design/topics/README]] 不属于当前完整架构包。它承接未拍板但已需要持续推进的设计专题，以及暂不进入当前范围但需要长期保留的专项储备。

## 查看顺序

### 先理解方案时

1. 先看 [[projects/requirements]] 和 [[projects/trace]]，确认当前要解决什么、边界在哪。
2. 再看 [[projects/design/tech-selection]]，确认技术底座为什么这样选。
3. 再看 [[projects/design/architecture]]，确认业务模块、页面、动作和状态机。
4. 再看 [[projects/design/backend-frontend-structure]] 和 [[projects/design/permission-boundary]]，确认工程落点与权限分层。
5. 再看 [[projects/design/write-boundary]]，确认写操作边界。
6. 再看 [[projects/design/database]]，确认状态、字段、约束和迁移真相源。
7. 最后看 [[projects/design/deployment]] 和 [[projects/design/runtime-quality]]，确认运行、发布和稳定性口径。

### 先动实现时

1. 页面和角色边界先看 [[projects/design/architecture]]。
2. 代码落点先看 [[projects/design/backend-frontend-structure]]。
3. 权限边界先看 [[projects/design/permission-boundary]]。
4. 写操作该留在平台层还是进入受控后端，先看 [[projects/design/write-boundary]]。
5. 状态、字段和迁移先看 [[projects/design/database]]。
6. 上传、环境、发布和回滚先看 [[projects/design/deployment]]。
7. 监控、重试、补偿和告警先看 [[projects/design/runtime-quality]]。
8. 如果要评估既有代码资产怎么接，再回看 [[projects/codebase/README]] 和它的子页。

## 当前内容

按需要补充：

- 设计总览
- 模块划分
- 接口边界
- 数据流
- 技术选型入口
- 工程结构入口
- 权限边界入口
- 写操作边界入口
- 部署和运行质量入口
- `memory` 路由
- `policy` 接线
- 风险和权衡

## 维护说明

- 如果输入是一份 PRD，先按 [[concepts/prd-writing]] 收成问题、目标、范围、规则和验收，再落到这里
- 如果某一块设计长成了独立主题，再从这个主入口往下拆子页
- 如果某个未决问题会跨多张设计页反复出现，就优先沉淀到 [[projects/design/topics/README]]
- 如果这轮是在“对新稿逐项做决策”，那这项决策相关的原稿信息不能只停留在 [[projects/decisions]] 里；必须同轮沉淀到当前主设计页或对应储备页，避免后续还要重新翻原稿
- 如果设计改变了当前实现口径、范围边界或修补结论，记得同步回写 [[projects/trace]]
- 如果设计判断会影响项目记忆或规则边界，先同步 [[projects/memory/README]] 和 [[POLICY]]
- 如果新增了设计子页类型，要同步更新 [[projects/STRUCTURE]]、[[WORKFLOW]]、必要的入口页和查看顺序，不让它变成孤岛页
