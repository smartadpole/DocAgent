---
type: entry
id: ENTRY-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-04-25
tags: [entry, root]
---

# 文档系统说明

这个文档库的目标很简单：把散乱资料变成能查、能连、能持续更新的知识网络，同时给未来的半自动 / 自动化项目推进留好路由。

如果只记一件事，就记住这套六层模型：

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]
- 运行层：[[projects/README]] 和 `projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

当前物理结构再补一句：

- 根目录保留高频入口：[[README]]、[[INDEX]]、[[AGENTS]]、[[log]]
- `governance/` 收治理页：[[governance/README]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[log-writing-rules]]、[[trace-writing-rules]]、[[template-feedback-rules]]
- `projects/` 收运行中的项目内容
- 其他目录分别承接沉淀、历史和证据

## 怎么用这个总入口

如果你第一次打开这个文档库，就按这个顺序走：

1. 先看这页，知道它是做什么的、怎么分层、怎么启动。
2. 再看 [[governance/README]]，先建立治理层的整体边界。
3. 再看 [[BRAIN]]，了解已经确认过、后续会自动参与工作的共享背景。
4. 再看 [[POLICY]]，知道哪些规则、优先级和记忆路由是硬约束。
5. 如果你要处理项目推进，就去看 [[projects/README]] 和 [[projects/STRUCTURE]]。
6. 如果你要先看项目当前阶段、阻塞和下一步，也可以直接看 [[projects/status]]。
7. 如果你要新增或修改文档，去看 [[WORKFLOW]]。
8. 如果你要知道 agent 能做什么、不能做什么，去看 [[AGENTS]]。
9. 如果你只是想找入口，直接看 [[INDEX]]。

常见操作对应关系：

- 想知道“这个系统怎么用” -> 读这页
- 想知道“治理层是怎么分的” -> 读 [[governance/README]]
- 想知道“之前确认过哪些前提，以后不用重复说” -> 读 [[BRAIN]]
- 想知道“规则、优先级和自动沉淀边界” -> 读 [[POLICY]]
- 想知道“项目级稳定记忆放哪” -> 读 [[projects/memory/README]]
- 想知道“一轮需求是怎么从原始意图收敛成当前实现口径的” -> 读 [[projects/trace]]
- 想知道“`[[projects/trace]]` 应该怎么写、怎么续写旧主题” -> 读 [[trace-writing-rules]]
- 想知道“其他项目进化出的系统层信息怎么反哺模板” -> 读 [[template-feedback-rules]]
- 想看“现实代码 / 旧工程怎么审计” -> 读 [[projects/codebase/README]]
- 想看“完整软件架构包” -> 按 [[projects/design/README]] 里的顺序读技术选型、架构、工程结构、权限边界、写操作边界、数据库、部署和运行质量
- 想看“还没拍板但已经需要持续推进的设计专题” -> 读 [[projects/design/topics/README]]
- 想知道“新建目录 / 新建文件 / 修改文件怎么做” -> 读 [[WORKFLOW]]
- 想知道“`[[log]]` 应该怎么写、怎么合并主题” -> 读 [[log-writing-rules]]
- 想知道“会议很多时怎么收口会议材料” -> 读 [[projects/meetings/README]]
- 想知道“Codex 处理时有哪些约束” -> 读 [[AGENTS]]
- 想知道“入口页、索引页、层级在哪” -> 读 [[INDEX]]

## 先看这些关键问题

如果你只从总入口判断要不要动文档，先看这 5 件事：

- 这是新目录，还是已有目录的扩展？
- 这是新文件，还是对已有文件的修改？
- 这份材料该进 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`？
- 这次改动会不会影响链接、目录名或索引？
- 这次处理是不是有长期价值，需要把按对话整理后的主题、用户意图和关键动作写进 [[log]]，或把稳定偏好写进 `workspace-memory`？

## 这组工具怎么配合

- `Obsidian` 是这套库的原生阅读 / 编辑工具，用来浏览、编辑和串联笔记；不用 `Obsidian` 时，`[[wikilink]]` 导航和双向链接不会完整生效。
- `Codex CLI` 用来读取、改写、批量生成 Markdown。
- `workspace-filesystem` 让 Codex 直接操作当前工作区下的文件。
- `workspace-memory` 记录长期规则、偏好、命名习惯和稳定结论。
- [[BRAIN]] 承接跨多轮确认、后续需要自动进入思考背景的共享内容。
- [[POLICY]] 承接共享规则、优先级和记忆路由。
- [[projects/memory/README]] 承接项目级稳定记忆。

## 治理层怎么分

治理层现在已经逻辑和物理两次收口：

- 逻辑上，治理层负责约束、流程、裁定、背景和写法指南
- 物理上，治理页统一收进 `governance/`，只保留 [[AGENTS]] 在根目录做 agent 特殊入口

最容易混的是这四页：

- [[POLICY]]：系统裁定规则。回答“什么允许、什么不允许、冲突时先按谁”
- [[AGENTS]]：执行约束。回答“agent 修改时必须怎么做”
- [[WORKFLOW]]：流程编排。回答“通常按什么顺序推进”
- [[BRAIN]]：共享背景。回答“哪些前提以后默认带入”

一句话记忆：

- [[POLICY]] 决定怎么判
- [[AGENTS]] 决定怎么执行
- [[WORKFLOW]] 决定怎么走
- [[BRAIN]] 决定默认带什么背景

## 软件研发模式怎么叠加

可以把原有底座理解成只有知识库模式。

知识库模式负责长期沉淀，研发模式负责项目推进。

- 知识库模式：收集资料，整理成 `articles/`、`concepts/`、`indexes/`
- 研发模式：在 `projects/` 里维护项目主页、设计、决策、发布和复盘
- 路由层：[[BRAIN]] 放共享背景，[[POLICY]] 放规则，[[projects/memory/README]] 放项目级稳定记忆
- 演进链：[[projects/trace]] 放当前项目里需求、约束、决策变化和最终落地范围之间的串联
- 两者衔接：项目里的稳定结论，最后回写到知识库层
- 流程控制：不做自动流控，由人读项目主页后手动推进
- 模板反哺：下游项目里被真实使用验证过的结构、流程、规则、记忆路由、写法、模板和自动化契约，抽掉项目事实后按 [[template-feedback-rules]] 回写模板库

## 角色和 memory 的关系

这套文档库里的角色分层，和 memory 分层不是一回事。

- 角色分层回答“谁负责什么”：项目负责人、研发经理、工程师
- memory 分层回答“该把哪些上下文放哪”：共享背景、规则、项目级稳定记忆
- 角色是职责视角，memory 是上下文视角
- 当前设计不打算给每个角色单独一套 memory，而是让同一套分层 memory 按作用域服务不同角色
- 如果未来要做角色专属 memory，需要额外补 ownership 和 routing 设计，那会是框架层变更，不是项目层内容
- 这类框架级说明以后优先维护在 [[README]]、[[governance/README]]、[[BRAIN]] 和 [[POLICY]]，不要下放到 `projects/` 及其子页

如果你正在做研发，先看 [[projects/README]]。
如果你想先看项目层的目录、文件、依赖和读取顺序，直接看 [[projects/STRUCTURE]]。
如果你想按一条固定顺序看完整架构，直接看 [[projects/design/README]] 里的 `完整架构包` 和 `查看顺序`。

如果你想看这套文档库的整体设计思路，去看 [[articles/2026-04-09-obsidian-doc-system-design]] 和 [[concepts/document-os]]。
如果你想看分层记忆的设计，去看 [[articles/2026-04-09-layered-memory-research]] 和 [[concepts/layered-memory]]。

研发阶段的详细说明、阶段映射和推进方式，统一看 [[WORKFLOW]] 里的 `1.9 软件研发模式`。
如果你要让智能体直接推进一个具体功能，也统一看 [[WORKFLOW]] 里的 `1.9.9` 到 `1.9.12`。

## 最短工作流

1. 新材料先丢进 `inbox/` 或直接放进 `raw/`。
2. 让 Codex 把材料整理成一篇 `articles/` 摘要卡片。
3. 把反复出现的工具和概念抽到 `concepts/`。
4. 把入口、分类和时间线写到 `indexes/`。
5. 把按对话整理后的主题、用户意图、关键动作和关键决策写进 [[log]]。
6. 把共享背景写进 [[BRAIN]]，把规则写进 [[POLICY]]，把项目级稳定记忆写进 [[projects/memory/README]]。
7. 如果这轮已经进入项目推进或实现，就把需求演进链写进 [[projects/trace]]。
8. 个人稳定偏好继续放进 `workspace-memory`，避免下次重复决定。
9. 如果某个下游项目进化出了可复用的系统层信息，按 [[template-feedback-rules]] 反哺回模板。

## 为什么入口页不写太多

- [[README]] 负责让你快速判断方向，不负责承载所有细则。
- 更完整的治理边界放在 [[governance/README]]。
- 详细的文件和目录流程放在 [[WORKFLOW]]。
- 维护约束和行为边界放在 [[AGENTS]]。
- 这样总入口不会变成长手册，但关键分流点仍然能一眼看到。

## 打开方式

- 优先用 `Obsidian` 打开当前文档库；如果只用普通 Markdown 阅读器，可以看正文，但不会完整解析 `[[wikilink]]`。
- 在文档库里直接打开 `INDEX.md`

## 更新原则

- 一篇材料只维护一张主摘要卡片。
- 一个概念只维护一个主页面。
- 索引页永远指向最新入口，不堆内容。
- 同一类信息只保留一个主入口，其他页面优先链接，不复制粘贴正文。
- 正文默认中文，英文只保留文件名、产品名、代码标识和必要术语，不为了表面统一强行翻译专有名词。
- 更新任何内容时，先看它在整个系统里的位置，再动当前文件。
- 上下文不是“当前文档前后几段”，而是和目标内容直接相关的主入口、上下游文件、阶段位置和知识层级。
- 同一文档库内的页面跳转，默认优先使用 `[[wikilink]]`，不要写死本机绝对路径。
- [[log]] 不做对话转录；新记录按时间降序插在前面，并按“日期下的对话”组织；详细写法与合并规则统一见 [[log-writing-rules]]。
- 原始来源只进 `raw/`，临时待处理内容只进 `inbox/`，整理稿不要回塞 `raw/`。
- 支持性图片、截图、图表和 canvas 等辅助文件优先放 `assets/`。
- 不再作为默认入口但仍需保留的页面放 `archive/`。
- 如果暂时不知道怎么归类，先放 `inbox/`。
- 只要新增模块或新类型文件，就要同步更新上下文规则，不允许文档结构和规则描述脱节。
- 只有实际内容或结构变更才需要 commit；本地状态和缓存不纳入正式提交。

更细的会话级约束、读取顺序和提交规则，以 [[AGENTS]] 和 [[WORKFLOW]] 为准。
