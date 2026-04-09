---
type: entry
id: ENTRY-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-04-10
tags: [entry, root]
---

# 文档系统说明

这个 vault 的目标很简单：把散乱资料变成能查、能连、能持续更新的知识网络，同时给未来的半自动 / 自动化项目推进留好路由。

如果只记一件事，就记住这一层分法：

- `raw/` 放原始资料
- `inbox/` 放临时待处理内容
- `assets/` 放截图、图片、导出物和辅助附件
- `projects/` 放活跃软件研发项目
- `articles/`、`concepts/`、`indexes/` 放整理后的知识
- `archive/` 放退役但仍需保留的旧页面
- vault 根目录主要放入口、规则和总索引
- [[BRAIN]] 放共享背景
- [[POLICY]] 放规则和优先级
- [[projects/memory/README]] 放项目级稳定记忆
- [[AGENTS]] 放维护规则

## 怎么用这个总入口

如果你第一次打开这个 vault，就按这个顺序走：

1. 先看这页，知道它是做什么的、怎么分层、怎么启动。
2. 再看 [[BRAIN]]，了解已经确认过、后续会自动参与工作的共享背景。
3. 再看 [[POLICY]]，知道哪些规则、优先级和 memory 路由是硬约束。
4. 如果你要处理项目推进，就去看 [[projects/README]] 和 [[projects/STRUCTURE]]。
5. 如果你要先看项目当前阶段、阻塞和下一步，也可以直接看 [[projects/status]]。
6. 如果你要新增或修改文档，去看 [[WORKFLOW]]。
7. 如果你要知道 agent 能做什么、不能做什么，去看 [[AGENTS]]。
8. 如果你只是想找入口，直接看 [[INDEX]]。

常见操作对应关系：

- 想知道“这个系统怎么用” -> 读这页
- 想知道“之前确认过哪些前提，以后不用重复说” -> 读 [[BRAIN]]
- 想知道“规则、优先级和自动沉淀边界” -> 读 [[POLICY]]
- 想知道“项目级稳定记忆放哪” -> 读 [[projects/memory/README]]
- 想知道“新建目录 / 新建文件 / 修改文件怎么做” -> 读 [[WORKFLOW]]
- 想知道“Codex 处理时有哪些约束” -> 读 [[AGENTS]]
- 想知道“入口页、索引页、层级在哪” -> 读 [[INDEX]]

## 先看这些关键问题

如果你只从总入口判断要不要动文档，先看这 5 件事：

- 这是新目录，还是已有目录的扩展？
- 这是新文件，还是对已有文件的修改？
- 这份材料该进 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`？
- 这次改动会不会影响链接、目录名或索引？
- 这次处理是不是有长期价值，需要写进 [[log]] 或 `workspace-memory`？

## 这组工具怎么配合

- `Obsidian` 用来浏览、编辑和串联笔记。
- `Codex CLI` 用来读取、改写、批量生成 Markdown。
- `workspace-filesystem` 让 Codex 直接操作当前工作区下的文件。
- `workspace-memory` 记录长期规则、偏好、命名习惯和稳定结论。
- [[BRAIN]] 承接跨多轮确认、后续需要自动进入思考背景的共享内容。
- [[POLICY]] 承接共享规则、优先级和 memory 路由。
- [[projects/memory/README]] 承接项目级稳定记忆。

## 软件研发模式怎么叠加

可以把原有底座理解成只有知识库模式。

知识库模式负责长期沉淀，研发模式负责项目推进。

- 知识库模式：收集资料，整理成 `articles/`、`concepts/`、`indexes/`
- 研发模式：在 `projects/` 里维护项目主页、设计、决策、发布和复盘
- 路由层：[[BRAIN]] 放共享背景，[[POLICY]] 放规则，[[projects/memory/README]] 放项目级稳定记忆
- 两者衔接：项目里的稳定结论，最后回写到知识库层
- 流程控制：不做自动流控，由人读项目主页后手动推进

如果你正在做研发，先看 [[projects/README]]。
如果你想先看项目层的目录、文件、依赖和读取顺序，直接看 [[projects/STRUCTURE]]。

如果你想看这套 vault 的整体设计思路，去看 [[articles/2026-04-09-obsidian-doc-system-design]] 和 [[concepts/document-os]]。
如果你想看分层 memory 的设计，去看 [[articles/2026-04-09-layered-memory-research]] 和 [[concepts/layered-memory]]。

研发阶段的详细说明、阶段映射和推进方式，统一看 [[WORKFLOW]] 里的 `1.9 软件研发模式`。
如果你要让 AI 直接推进一个具体功能，也统一看 [[WORKFLOW]] 里的 `1.9.9` 到 `1.9.12`。

## 最短工作流

1. 新材料先丢进 `inbox/` 或直接放进 `raw/`。
2. 让 Codex 把材料整理成一篇 `articles/` 摘要卡片。
3. 把反复出现的工具和概念抽到 `concepts/`。
4. 把入口、分类和时间线写到 `indexes/`。
5. 把过程和决策追加到 `log.md`。
6. 把共享背景写进 [[BRAIN]]，把规则写进 [[POLICY]]，把项目级稳定记忆写进 [[projects/memory/README]]。
7. 个人稳定偏好继续放进 `workspace-memory`，避免下次重复决定。

## 为什么入口页不写太多

- `README.md` 负责让你快速判断方向，不负责承载所有细则。
- 详细的文件和目录流程放在 `WORKFLOW.md`。
- 维护约束和行为边界放在 `AGENTS.md`。
- 这样总入口不会变成长手册，但关键分流点仍然能一眼看到。

## 打开方式

- 直接用 Obsidian 打开当前 vault
- 在 vault 里直接打开 `INDEX.md`

## 更新原则

- 一篇材料只维护一张主摘要卡片。
- 一个概念只维护一个主页面。
- 索引页永远指向最新入口，不堆内容。
- 同一类信息只保留一个主入口，其他页面优先链接，不复制粘贴正文。
- 更新任何内容时，先看它在整个系统里的位置，再动当前文件。
- 上下文不是“当前文档前后几段”，而是和目标内容直接相关的主入口、上下游文件、阶段位置和知识层级。
- 同一个 vault 内的页面跳转，默认优先使用 `[[wikilink]]`，不要写死本机绝对路径。
- `log.md` 只追加，不重写。
- 原始来源只进 `raw/`，临时待处理内容只进 `inbox/`，整理稿不要回塞 `raw/`。
- 支持性图片、截图、图表和 canvas 等辅助文件优先放 `assets/`。
- 不再作为默认入口但仍需保留的页面放 `archive/`。
- 如果暂时不知道怎么归类，先放 `inbox/`。
- 只要新增模块或新类型文件，就要同步更新上下文规则，不允许文档结构和规则描述脱节。
- 只有实际内容或结构变更才需要 commit；本地状态和缓存不纳入正式提交。

更细的会话级约束、读取顺序和提交规则，以 `AGENTS.md` 和 `WORKFLOW.md` 为准。
