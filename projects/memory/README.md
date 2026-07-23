---
type: memory
memory_layer: project
scope: project
project: wiki
status: active
source_of_truth: true
updated: 2026-07-23
---

# 项目记忆

这页是 `projects/` 里的运行层记忆入口，承接项目级稳定背景。

## 这页负责什么

- 记录当前项目长期有效的背景、路由和模块边界
- 记录“以后做事默认要知道”的项目级前提
- 作为项目级记忆的主入口
- 为后续自动化提供可读的稳定上下文

## 这页不负责什么

- 不放全局规则，那是 [[POLICY]]
- 不放项目拍板，那是 [[projects/decisions]]
- 不放需求到实现的演进链，那是 [[projects/trace]]
- 不放共享背景正文，那是 [[BRAIN]]
- 不放过程流水，那是 [[log]]

## 当前子页

- [[projects/memory/shared]]：项目共享背景和稳定事实
- [[projects/memory/policy-links]]：运行层和规则层的连接页
- [[projects/meetings/README]]：项目正式会议入口和纪要分流页
- [[projects/design/topics/implementation-engineering-template-system]]：实现类工程合集与模板系统的设计 owner
- [[wiki-governance-system-contract.v1]]：wiki 治理体系全面整改的运行合同
- [[templates/implementation-project-profile-template]]：主控 / 子工程 / runtime service / 数据模型 / 文档治理工程的接入 profile

## 当前路由

- 会话 / 临时收口区：临时信息
- [[projects/memory/README]]：项目级稳定背景
- [[projects/design/topics/implementation-engineering-template-system]]：实现类工程模板定位、工程类型覆盖和不能上推边界
- [[wiki-governance-system-contract.v1]]：agent、workflow、memory、harness、skill、evaluation、governance、template、topic、migration 的全面整改完成定义
- [[acknowledgebase-topic-system-adoption.v1]]：AcknowledgeBase source topic 到 wiki 系统层的逐 topic ability adoption manifest
- [[projects/design/topics/agent-workflow-memory-harness-skill-landing]]：AcknowledgeBase topic 到 wiki 系统层的摘要矩阵
- [[projects/trace]]：项目需求演进链
- [[projects/meetings/README]]：项目正式会议入口
- [[BRAIN]]：共享背景
- [[POLICY]]：规则和优先级
- [[projects/decisions]]：项目冲突和拍板
- `articles/`、`concepts/`、`indexes/`：长期知识资产

## 维护说明

- 如果一条信息只对当前项目长期有效，优先放这里
- 如果内容是在说明本轮需求怎样收敛、哪些修补改变了当前实现口径，优先放 [[projects/trace]]
- 如果内容是在说明正式会议怎么收口、怎么分流，优先放 [[projects/meetings/README]]
- 如果它会改变后续怎么判断和怎么写，优先放到 [[POLICY]]
- 如果它已经变成跨阶段、可复用的稳定知识，再提升到 `articles/` 或 `concepts/`
- 记忆研究设计继续放在 [[projects/design/memory/README]]，不要把研究稿混进正式运行层
