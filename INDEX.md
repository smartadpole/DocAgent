---
type: index
scope: shared
status: active
updated: 2026-04-09
---

# 知识库入口

这是一套给 Obsidian + Codex 用的文档系统。

如果你不知道先看什么，按这个顺序：

1. 先看 `[[README]]`，知道这个 vault 是干什么的、怎么启动、怎么选动作。
2. 再看 `[[BRAIN]]`，知道哪些已确认背景会自动参与后续工作。
3. 再看 `[[POLICY]]`，知道规则、优先级和 memory 路由怎么定。
4. 要处理项目运行层，就看 `[[projects/README]]` 和 `[[projects/memory/README]]`。
5. 要处理文件和目录细节，就看 `[[WORKFLOW]]`。
6. 要知道 agent 的维护边界，就看 `[[AGENTS]]`。
7. 要找入口分类和运行记录，就留在这页。

这页只做总导航，不承载细节。

## 入口

- `[[README]]`：vault 总说明和启动入口
- `[[BRAIN]]`：共享背景
- `[[POLICY]]`：规则、优先级和 memory 路由
- `[[projects/README]]`：活跃软件研发项目的运行入口
- `[[projects/memory/README]]`：项目级稳定记忆入口

## 设计思路

- `[[articles/2026-04-09-obsidian-doc-system-design]]`：Obsidian 文档系统整体设计研究
- `[[concepts/document-os]]`：文档操作系统概念定义
- `[[articles/2026-04-09-layered-memory-research]]`：分层 memory 研究
- `[[concepts/layered-memory]]`：分层 memory 概念定义

## 层级

- `raw/`：原始资料层，尽量只进不改
- `inbox/`：临时收口区，来源还没完全整理前先放这里
- `assets/`：截图、图片、导图、导出物和辅助附件
- `projects/`：活跃软件研发项目层，放需求、设计、决策、记忆、发布和复盘
- `articles/`：每篇材料一张摘要卡片
- `concepts/`：每个工具或概念一个页面
- `indexes/`：全局索引、分类索引、时间线索引
- `archive/`：退役但仍需保留的页面和历史版本

## 运行记录

- `[[log]]`：按时间追加的 ingest / lint / decision 记录

## 更新原则

- 工具名和概念名尽量用 `[[双向链接]]`
- 新内容先写成摘要卡片，再汇总到概念页和索引页
- 长期不变的规则和偏好分别写进 `[[BRAIN]]`、`[[POLICY]]` 和 `workspace-memory`
