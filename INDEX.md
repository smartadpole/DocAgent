---
type: index
id: INDEX-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-04-12
tags: [index, root]
---

# 知识库入口

这是一套给 Obsidian + Codex 用的文档系统。

如果你不知道先看什么，按这个顺序：

1. 先看 [[README]]，知道这个 vault 是干什么的、怎么启动、怎么选动作。
2. 再看 [[governance/README]]，先知道治理层怎么分。
3. 再看 [[BRAIN]]，知道哪些已确认背景会自动参与后续工作。
4. 再看 [[POLICY]]，知道规则、优先级和 memory 路由怎么定。
5. 要处理项目运行层，就看 [[projects/README]] 和 [[projects/memory/README]]。
6. 要处理文件和目录细节，就看 [[WORKFLOW]]。
7. 要知道 agent 的维护边界，就看 [[AGENTS]]。
8. 要找入口分类和主题化后的运行记录，就留在这页。

这页只做总导航，不承载细节。

## 入口

- [[README]]：vault 总说明和启动入口
- [[governance/README]]：治理层入口
- [[BRAIN]]：共享背景
- [[POLICY]]：规则、优先级和 memory 路由
- [[log-writing-rules]]：`[[log]]` 的记录规则入口
- [[projects/README]]：活跃软件研发项目的运行入口
- [[projects/memory/README]]：项目级稳定记忆入口
- [[projects/trace]]：需求演进链入口
- [[trace-writing-rules]]：`[[projects/trace]]` 的记录规则入口

## 设计思路

- [[articles/2026-04-09-obsidian-doc-system-design]]：Obsidian 文档系统整体设计研究
- [[concepts/document-os]]：文档操作系统概念定义
- [[articles/2026-04-09-layered-memory-research]]：分层 memory 研究
- [[concepts/layered-memory]]：分层 memory 概念定义

## 层级

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]
- 运行层：`projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

## 物理结构

- 根目录保留高频入口：[[README]]、[[INDEX]]、[[AGENTS]]、[[log]]
- `governance/` 收治理页和规则页
- `projects/` 收运行层
- `articles/`、`concepts/`、`indexes/` 收知识沉淀
- `archive/` 收退役历史，`raw/`、`inbox/`、`assets/` 收证据

## 运行记录

- [[log]]：按时间降序记录每次对话的主题、用户意图、关键动作和结构调整
- [[log-writing-rules]]：`[[log]]` 的记录单位、主题合并规则和跨日期边界

## 更新原则

- 工具名和概念名尽量用 `[[双向链接]]`
- 新内容先写成摘要卡片，再汇总到概念页和索引页
- 长期不变的规则和偏好分别写进 [[BRAIN]]、[[POLICY]] 和 `workspace-memory`
