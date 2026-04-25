# 更新工作流

这页属于治理层，统一由 [[governance/README]] 收口。

这份流程适合每天反复用。目标不是一次写完，而是让文档系统持续长大。

## 0. 会话级执行规则

每次对话里，只要发生实际文件变更，都按下面顺序执行：

1. 先判断这次问题是简单更新，还是复杂问题。
2. 如果是复杂问题，先拆成几个中间节点，再逐个完成，不要一次改一大坨。
3. 开始改之前，先建立全局背景，再找这次问题的主入口、单一信息源和相关跳转页。
4. 更新时优先改主页面，其他页面只补链接、简短说明或导航，不复制正文。
5. 每个中间节点完成后，检查结构、链接、阶段映射和职责是否仍然清楚。
6. 复杂问题在中间节点完成后就提交；只要这次对话产生了实际内容变更或结构变更，保底在对话结束前提交一次。
7. 只要这次对话产生了实际内容变更或结构变更，就同步补一条 `[[log]]` 记录；不要因为“还是同一主题”就省略。
8. 如果这轮是在对一份新方案或新架构稿逐项拍板，拍板后不能只留下决策结论；必须把与该项决策直接相关的原稿信息同步沉淀到 `projects/design/` 的当前主设计页或设计储备页，避免后续重复回读原稿。

如果这次是大量同类材料的连续处理，再先多做一步：

1. 先判断能不能进入“轻量批处理模式”。
2. 如果能，先做一次批次级全局校准，再在同批材料中复用，不要对每一份材料重复读同一组入口页。
3. 只要某一份材料开始涉及规则、结构、项目状态、关键取舍或记忆路由，立刻退出轻量批处理模式，回到默认重路径。

判断是否属于复杂问题，可以看这几个信号：

- 涉及多个目录或多个页面
- 同时改结构、流程和内容
- 需要跨知识库层和项目层回写
- 改完后必须同步多个入口页或索引页

判断能不能进入轻量批处理模式，可以看这几个信号：

- 这次要连续处理很多份同类型材料
- 每份材料的目标主要是摘要、归类、补链接、回链或轻量整理
- 这批工作不会直接改规则、结构、项目阶段、项目级状态或冲突结论
- 同一批材料共享同一组主入口和判断框架

不适合进入轻量批处理模式的典型情况：

- 这批材料里混着需求拍板、设计取舍、状态推进或规则调整
- 不同材料分属不同项目阶段、不同主入口或不同读者层
- 需要一份一份重新做完整上下文判断，不能复用同一套前置校准

不需要提交的典型情况：

- 只改本地界面状态
- 只产生临时缓存或草稿
- 没有实际改变文档内容、结构、规则或链接关系

判断主入口和单一信息源时，优先这样看：

- 状态、范围、下一步：看 `projects/README.md`
- 需求边界和验收：看 `projects/requirements.md`
- 方案、接口、数据流：看 `projects/design/README.md`
- 未拍板但需要持续推进的设计专题：看 `projects/design/topics/README.md`
- 业务架构、页面动作、状态机：看 `projects/design/architecture.md`
- 前后端模块和接口落点：看 `projects/design/backend-frontend-structure.md`
- 权限真相源和分层：看 `projects/design/permission-boundary.md`
- 写操作边界和服务端收口规则：看 `projects/design/write-boundary.md`
- 数据模型和迁移：看 `projects/design/database.md`
- 环境、发布和回滚：看 `projects/design/deployment.md`
- 监控、告警、重试和补偿：看 `projects/design/runtime-quality.md`
- 关键取舍：看 `projects/decisions.md`
- 项目级稳定记忆：看 `projects/memory/README.md`
- 治理层总边界：看 [[governance/README]]
- 共享背景：看 [[BRAIN]]
- 规则和优先级：看 [[POLICY]]
- 过程记录和排障：看 `projects/development/worklog.md`
- 发布和回滚：看 `projects/releases.md`
- 事故和复盘：看 `projects/incidents/README.md`
- 长期概念和通用知识：看 `concepts/`、`articles/`、`indexes/`

### 0.1 共享脑怎么用

- [[log]] 只负责按时间降序呈现每次对话的主题、用户意图、关键动作和结构变化，不负责主动参与后续思考。
- [[BRAIN]] 负责承接已经跨多轮确认、后续应该自动生效的共享背景。
- [[POLICY]] 负责承接规则、优先级和自动沉淀边界。
- `projects/memory/README.md` 负责承接项目级稳定记忆。
- 以后开始一个新任务时，默认把 [[BRAIN]] 当作背景之一，不要求用户再重复同一件事。
- 如果一个结论只是这一次的过程记录，不进 [[BRAIN]]。
- 如果一个结论会长期影响判断、多人协作或后续结构，就要考虑提升到 [[BRAIN]]。
- 如果一个结论会改变路由、优先级或自动沉淀边界，就要考虑提升到 [[POLICY]]。
- 如果一个结论只对当前项目长期有效，就写进 `projects/memory/`。

### 0.2 内容写到哪里

- [[AGENTS]]：写硬约束和 agent 必须遵守的行为。
- [[BRAIN]]：写多轮确认后的共享背景和共同前提。
- [[POLICY]]：写规则、优先级和记忆路由边界。
- `projects/memory/README.md`：写项目级稳定记忆。
- [[projects/trace]]：写需求从原始意图、约束变化到最终实现范围的演进链。
- `workspace-memory`：写个人稳定偏好和重复习惯。
- `projects/decisions.md`：写项目阶段的冲突、取舍和正式决策。
- [[log]]：写时间降序、按对话组织的主题化记录，收口用户意图、关键动作和结构调整。

### 0.2.1 收尾怎么执行

当用户明确下达“收尾 / 执行收尾 / finalize”这类执行命令时，本轮切到收尾模式；如果用户只是在讨论收尾规则、排查收尾失败或询问怎么收尾，不切模式。

收尾模式只做当前主题的收口，不继续扩需求或顺手做下一轮功能。默认顺序：

1. 先确认这轮真正要收的范围，只看本轮已经发生的内容和结构变更。
2. 回看受影响主入口和必要邻接页，确认职责、链接和阶段映射没有被破坏。
3. 补齐与本轮 diff 直接相关的同步项，例如入口页、规则页、索引页或项目页。
4. 补写 [[log]]，确保记录的是这轮真实用户意图、关键动作和结构变化，而不是一句“已收尾”。
5. 做一次最小一致性检查：内部链接、主入口、单一信息源、命名口径、受影响页面之间是否一致。
6. 提交当前主题改动，不把无关脏改动一起打包。

收尾模式的边界：

- 不新增业务功能，不顺手继续设计下一轮方案。
- 不扩大成整库巡检，只处理和本轮 diff 直接相关的同步与检查。
- 如果存在本轮未触及的预存脏改动，默认不纳入本次收尾；只有用户明确要求，才一起处理。

### 0.3 分层记忆怎么路由

- 临时会话信息和还没确认的草稿，先留在会话或 `inbox/`
- 项目里已经开始推进的一轮需求、约束变化、修补性需求和最终实现口径，只要会影响当前 trace 主题，就优先在同轮写进 [[projects/trace]]
- 只对当前项目长期有效的稳定事实，写进 `projects/memory/`
- 跨任务、跨会话、后续还会持续影响工作的共享背景，写进 [[BRAIN]]
- 会改变后续判断方式、优先级或自动沉淀边界的内容，写进 [[POLICY]]
- 发生项目内冲突或取舍时，先写进 `projects/decisions.md`
- 已经稳定到可以复用的结论，再提炼到 `articles/`、`concepts/` 或 `indexes/`

### 0.3.1 需求演进 trace 怎么写

`[[projects/trace]]` 不是 `[[log]]` 的第二份，也不是 `[[projects/decisions]]` 的替身。

- `[[log]]` 记录这轮对话在推进什么主题、做了哪些关键动作。
- [[projects/trace]] 记录一轮需求怎样从原始意图、约束变化、修补性需求一路收敛到最终实现口径。
- 原始来源材料的收口、改名、PDF 到 Markdown / PDF->md、链接清理和格式整理，不属于 [[projects/trace]] 的内容。
- `projects/decisions.md` 只记录真正需要拍板的冲突和取舍，不重复抄整条演进链。

默认写法：

1. 先确认这轮是否已经进入项目推进，而不只是聊天或资料收集。
2. 如果已经进入需求、设计、实现或修补阶段，就在 [[projects/trace]] 维护同主题条目，而不是把这些变化只留在对话里。
3. 如果这轮只是整理来源材料、改文件名、做 PDF 到 Markdown / PDF->md、清理入口链接或补来源索引，不写进 [[projects/trace]]。
4. 每个主题优先保留一条主链，后续新增内容写成新的迭代块，不重复新建多条平行正文。
5. 条目里至少写清：原始意图、收敛后的可执行需求、关键决策变化、最终范围、关联页面。
6. 如果后续变化只是修补 agent 本轮实现引出的偏差，要明确标成修补性需求，不把它抬升成原始业务目标。
7. 详细写法统一见 [[trace-writing-rules]]；默认模板见 [[templates/trace-entry-template]]，不要在流程页复制第二份模板正文。
8. 记录人默认写在迭代块里，不默认挂在主题主链顶层；需要标注时优先用当前仓库的 `git user.name`。
9. 日期默认写到天，只有同一天多次收敛需要区分时才升级到分钟；如果需要表达参与视角，再按迭代块补 `角色`。

建立全局背景时，至少先回答这几个问题：

- 这次更新服务的是知识库模式，还是研发模式
- 它处在项目的哪个阶段
- 这一段内容的主入口是哪一页
- 哪些页面会被这次更新影响
- 这次写进去的内容是长期知识，还是阶段性上下文

建立上下文时，建议按这个顺序做：

1. 先判断目标属于证据层、项目运行层、知识沉淀层、导航层还是历史层。
2. 再判断它在当前项目里属于哪个阶段：调研、设计、开发、发布、事故、归档。
3. 找到这个目标的主入口页，不允许绕开主入口直接写局部文件。
4. 找到它的上游文件和下游文件。
5. 确认这次写入的是来源、判断、过程、结论还是导航。
6. 再决定该改主页面、补支撑页，还是把结论提升到知识库层。

上下游关系可以这样理解：

- 上游：这段内容依赖哪些来源、需求、设计、决策、阶段判断
- 下游：这段内容会影响哪些页面的理解、状态、跳转、结论
- 主入口：这一类信息最终由哪一页负责解释和收口

对当前这个单项目系统，默认上下文链路是：

- 外部来源进入 `raw/` 或 `inbox/`
- 当前项目判断和推进进入 `projects/`
- 稳定结论沉到 `articles/`、`concepts/`、`indexes/`
- 失去主入口职责但仍需保留的内容进入 `archive/`

不同目标文件，默认先看这些关联文件：

- `projects/README.md`：`requirements.md`、`design/README.md`、`decisions.md`、`development/README.md`、`projects/memory/README.md`、[[POLICY]]
- `projects/requirements.md`：`projects/README.md`、相关 `raw/`、已有 `projects/design/README.md`、[[projects/trace]]
- `projects/codebase/README.md`：`projects/README.md`、`projects/STRUCTURE.md`、`projects/requirements.md`、`projects/design/README.md`、`projects/decisions.md`
- `projects/design/README.md`：`projects/README.md`、`projects/requirements.md`、`projects/design/topics/README.md`、[[projects/trace]]、`projects/decisions.md`、`projects/memory/README.md`、[[POLICY]]、相关 `concepts/`
- `projects/design/architecture.md`、`projects/design/backend-frontend-structure.md`、`projects/design/permission-boundary.md`、`projects/design/write-boundary.md`、`projects/design/database.md`、`projects/design/deployment.md`、`projects/design/runtime-quality.md`、`projects/design/topics/*.md`：先读 `projects/design/README.md`，再按主题补读相邻设计子页 / 专题页、`projects/requirements.md`、[[projects/trace]] 和 `projects/decisions.md`
- [[projects/trace]]：`projects/README.md`、`projects/requirements.md`、`projects/design/README.md`、`projects/decisions.md`、当前相关开发页
- `projects/decisions.md`：`projects/README.md`、`projects/requirements.md`、`projects/design/README.md`、[[projects/trace]]、`projects/memory/README.md`、[[POLICY]]、相关过程记录
- `projects/development/worklog.md`：`projects/README.md`、[[projects/trace]]、当前相关 `projects/decisions.md`
- `projects/releases.md`：`projects/README.md`、`projects/design/README.md`、`projects/decisions.md`、[[POLICY]]
- `projects/incidents/README.md`：`projects/README.md`、`projects/releases.md`、`projects/development/worklog.md`、`projects/decisions.md`、`projects/memory/README.md`
- `articles/`：对应 `raw/`、相关 `concepts/`、必要时读相关项目页
- `concepts/`：相关 `articles/`、相关项目页、相关 `indexes/`
- `indexes/`：它所指向的主页面

如果这次变更新增了模块、目录、模板、入口页或新的高频文件类型，还要额外做这一步：

1. 判断它属于哪一层，服务什么职责。
2. 判断它的主入口是谁，它依赖哪些上游文件，又会影响哪些下游文件。
3. 把这些关系同步补进 [[AGENTS]] 的上下文模型、关联关系、最小读取集。
4. 如果它影响总入口理解，再补 `README.md`。
5. 在 [[log]] 记录这次结构扩展，并写明对应主题和用户意图。

如果新增的是设计层高频子页，还要再补这一步：

1. 先把它挂到 [[projects/design/README]]。
2. 再把它补进 [[projects/README]] 和 [[projects/STRUCTURE]]。
3. 如果它会影响“先看哪、后看哪”的默认顺序，再同步更新 [[README]]、[[INDEX]] 和当前相关流程说明。

如果新增的是“未拍板但需要持续推进”的设计专题，还要再补这一步：

1. 先把它挂到 [[projects/design/topics/README]]，而不是先塞到会议页。
2. 再在相关会议材料里引用这张专题页，不复制第二份正文。
3. 如果专题最终拍板并进入主设计，再同步更新 [[projects/design/README]]、[[projects/decisions]] 和 [[projects/trace]]。

也就是说，结构一变，上下文规则就要在同一次变更里一起更新，不后补。

如果这次变更还形成了新的共享背景，再额外做这一步：

1. 判断它是不是跨多轮确认、且后续还会反复影响判断。
2. 如果是，补进 [[BRAIN]]。
3. 如果它是规则、优先级或自动沉淀边界，补进 [[POLICY]]。
4. 如果它是项目级稳定记忆，补进 `projects/memory/README.md`。
5. 如果它只是个人偏好，再写进 `workspace-memory`，不塞进共享脑。
6. 如果它和已有背景冲突，先升级到 `projects/decisions.md`，不要直接改写共享脑。

## 0.4 轻量批处理模式

这不是另一套平行流程，而是默认流程在“批量同类处理”场景下的减载版本。

适用范围：

- 批量技术文章摘要
- 批量设计草稿整理
- 批量补链接、补回链、补索引
- 批量把来源材料收口到既有主页面

不适用范围：

- 规则变更
- 结构变更
- 项目阶段推进
- 关键设计取舍
- 记忆路由调整
- 冲突拍板

执行顺序：

1. 先做一次批次级校准，确认这批材料服务哪个主题、哪个阶段、哪个主入口、哪类读者。
2. 先读一遍这批材料共享的入口页和单一信息源。
3. 再按单份材料补读它自己的直接来源、对应主页面和必要邻接页。
4. 每处理完一小批就回看链接、命名和落点，不要攒到最后一起兜底。
5. 如果出现规则、结构、状态、取舍或路由变化，立即升级回默认流程。

推荐的共享读取方式：

- 批量文章：先读 `README.md`、`INDEX.md`、相关 `articles/` / `concepts/` 主页面；再逐篇补读来源和直接回链目标。
- 批量设计材料：先读 `projects/README.md`、`projects/STRUCTURE.md`、相关设计主入口、当前相关需求页或决策页；再逐份补读材料本身和必要的相关 `concepts/`。

核心原则只有一句：

- 复用批次级校准，避免把“每轮必读集”按材料份数线性放大。

控制规则体积时，按这个顺序处理：

1. 先改已有规则。
2. 只有旧规则确实容纳不下，才新增新条目。
3. 新规则加完后，回看有没有重复段落可以删掉。

## 0.5 模板反哺模式

当用户要求把某个下游项目的文档系统进化反哺回模板库时，按 [[template-feedback-rules]] 执行。

默认顺序：

1. 先确认来源项目和模板库各自的当前状态，不把来源项目的预存脏改动并入模板提交。
2. 读取来源项目的入口页、结构页、治理页、规则页、模板页、记忆页和 [[log]]，只抽取系统层变化。
3. 把候选变化分成系统规则、系统结构、系统流程、系统模板、系统记忆路由、自动化契约和项目材料。
4. 对反哺项做脱敏和抽象，删掉项目名、业务名、具体数据、具体状态、具体技术拍板和一次性会议内容。
5. 只要候选项是规则，默认需要反哺；如果决定不反哺，必须能说明它为什么只是项目材料。
6. 按路由更新模板：结构进 [[projects/STRUCTURE]] 和入口页，流程进 [[WORKFLOW]]，硬约束进 [[AGENTS]]，规则和记忆路由进 [[POLICY]]，共享背景进 [[BRAIN]]，可复制写法和模板骨架进 `templates/`。
7. 如果反哺新增模块、目录、入口页或高频文件类型，同轮补齐 README、入口链接、上下游关系、最小读取集和 [[log]]。
8. 交付前检查没有项目专名泄漏、没有缺失 wikilink、没有复制第二份模板正文。

判断是否可以反哺：

- 规则、流程、结构、记忆路由、写法、模板和自动化契约，去掉项目事实后仍然能跨项目成立，就回模板。
- 规则默认反哺；规则里夹带项目事实时，只抽象规则，不复制事实。
- 只是下游项目的业务决策、技术选择、会议结论、状态推进或实现结果，留在下游项目。
- 如果某项变化会改变模板维护方式，必须同步更新 [[template-feedback-rules]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]] 和相关入口页。

## 1. 收集

- 新文章、链接、会议纪要、想法，先放进 `inbox/` 或 `raw/`。
- 保留来源、时间、作者、上下文。
- 先记录原始内容，不急着分类。

## 1.1 新目录怎么起步

当你要新建一个目录时，先做这三件事：

- 先建一个 `README.md`，说明这个目录放什么。
- 模板和索引按需创建，不要为了完整性先铺满。
- 需要入口时，再从 `INDEX.md` 或总入口补一条链接过去。

推荐做法：

- `projects/` 这种目录，适合放项目材料和项目索引。
- `people/` 这种目录，适合放人物笔记和关联资料。
- `topics/` 这种目录，适合放主题研究和跨文章概念。

## 1.2 raw / inbox 的边界

- `raw/` 只放原始来源，优先保持原样，不做二次总结。
- `inbox/` 只做临时收口和待清洗队列，不要长期堆积。
- 项目内正式会议的纪要、行动项和回看，最终收口到 [[projects/meetings/README]]；`raw/` 和 `inbox/` 只负责临时收集。
- 原始来源如果已经处理完，去 `articles/`、`concepts/` 或 `indexes/`，不要再回写成 raw。
- 图片、截图、导图和其他支持性附件，如果不是原始来源，优先放 `assets/`。
- 如果来源还没确认，先放 `inbox/`，确认后再分流到正确层。

## 1.3 新建目录

新建目录前先问三个问题：

1. 这个目录是不是一个新的稳定主题，而不是已有目录的子集？
2. 现有 `articles/`、`concepts/`、`indexes/`、`raw/`、`inbox/` 能不能复用？
3. 这个目录后面会不会需要单独检索、单独索引、单独模板？

如果答案都偏向“是”，再新建目录。新建时按这个顺序：

1. 先建目录本身。
2. 先补 `README.md`，说明目录用途和边界。
3. 如果目录会反复产出同类文件，再补一个模板文件。
4. 如果目录需要导航，再补 `INDEX.md` 或挂到总 `INDEX.md`。
5. 如果它是新主题，把入口链接加到上层索引。

已有目录优先扩展，不要平行复制一个新目录。目录太大时，优先拆子目录和索引，不要先删旧结构。

## 1.4 新建文件 / 新增文件

新建文件时先确定它属于哪一层：

- 原始资料，放 `raw/`
- 临时收口，放 `inbox/`
- 支持性附件，放 `assets/`
- 活跃研发项目文档，放 `projects/`
- 正式会议入口和会议纪要，放 `projects/meetings/`
- 摘要卡片，放 `articles/`
- 概念或实体页，放 `concepts/`
- 导航页，放 `indexes/`
- 退役或历史页，放 `archive/`

然后按这个顺序处理：

1. 用模板开头，避免每次格式漂移。
2. 写最小可用内容，先能检索、能链接、能追溯。
3. 加上相关 `[[双向链接]]`。
4. 如果是高频类型，再抽成模板。
5. 如果这是一次重要 ingest，在 [[log]] 顶部新增一条主题化记录。

如果是从网页或外部资料新建文件，优先保留原始来源，再生成整理版，不要直接拿整理版覆盖原文。

## 1.5 修改文件

修改文件的默认原则是“先读后改、少改、保留结构”。

1. 先打开现有文件，确认它已经承担的角色。
2. 只改需要改的段落，不要重写整篇，除非它本来就是空壳。
3. 改完后检查相关链接、标题和索引是否仍然成立。
4. 如果改的是文件名或目录名，确保内部链接一起更新。
5. 如果改动影响结构、入口或约定，把变更写进 [[log]]，先写主题和用户意图，再写动作和影响。

### 1.5.0 `[[log]]` 怎么写

- `[[log]]` 默认按时间降序维护，新记录插在最前面。
- 同一天内如果有多条记录，也保持降序；当天最新的一条放在该日期下面最前面。
- `[[log]]` 只负责承接历史记录，不承担完整规则正文。
- 详细写法、合并与拆解标准、跨日期边界，统一见 [[log-writing-rules]]。
- 默认模板见 [[templates/log-entry-template]]；如果直接手写，也按同一骨架记录。
- 如果这次只是对上一条相关记录的补完、纠偏、重命名、格式统一或样例同步，优先直接完善旧记录，不新开并列记录。
- 如果这次已经需要换一句话概括用户意图，或者开始解释“上一条为什么写错、为什么漏记、怎样长期避免”，就按新对话记录处理，不要继续并到旧记录里。
- 同一天内围绕同一页面发生多轮对话是正常的；不要因为都在改 `[[log]]`，就把它们压成一条单日总记录。
- 写 `[[log]]` 时，重点优先靠顺序来强调：标题写主变化，主题按重要性排序，关键动作第 1 条先写本次最重要的决定、修正或收口。
- 渲染层面推荐轻量强调：字段名和短标签可以加粗，但不要把整条用户意图或整条关键动作整段加粗。
- 只要一条记录采用“标签：内容”的展开式写法，默认把冒号前的标签加粗，统一写成 `**标签**：内容`，不要同一页里一半加粗、一半裸写。

### 1.5.1 Markdown 引用校验

每次改完 Markdown，都把引用格式检查当作交付前必做动作，不是可选优化。

- 本库内页面引用只允许使用 `[[wikilink]]` 及其变体：`[[page]]`、`[[page|alias]]`、`[[page#heading]]`、`[[page#^block-id]]`。
- 如果语义上是在指向本库的页面，而不是单纯讨论文件名字符串，也统一改成 `[[wikilink]]`，不要保留 [[BRAIN]]、[[POLICY]]、`log.md` 这类裸文件名引用。
- 外部资源只使用普通 Markdown 链接：`[title](https://example.com)`。
- 发现本库内 `.md` 相对链接、空链接、占位链接、写死本机绝对路径时，当场修正，不留到后续再清理。
- 如果一次处理里改了标题、文件名、目录名或段落结构，结束前必须回看受影响页面，确认引用仍然能跳转、别名仍然可读、没有残留旧路径。
- 如果无法在当轮确认目标页名，就先停留为纯文本说明并明确标注，不要制造一个看起来像链接但实际会失效的引用。

### 1.5.1.1 模板与内部链接专项检查

只要这次改动碰到模板页、模板入口、`README` / `WORKFLOW` / `log` 这类入口页，交付前额外检查这两件事：

- 模板正文是不是只保留在对应的 `templates/` 页面里；其他页面只能写说明和 `[[wikilink]]`，不能复制第二份模板正文。
- 语义上指向本库页面的内容，是不是都写成了 `[[wikilink]]`；不允许保留反引号文件名、裸文件名或纯文本路径。

在 Obsidian 里，建议开启自动更新内部链接，这样重命名文件时引用不会散掉。

### 1.5.2 链接怎么写

- 同一文档库内的页面跳转，优先写成 `[[wikilink]]`。
- 不要在仓库文档里写死本机绝对路径；换电脑后会失效。
- 如果只是引用当前文档库的其他文档，不要继续写 `./xxx.md` 这类相对 Markdown 链接，优先改成 `wikilink`。
- 如果要引用页内标题、区块或显示别名，继续沿用 `wikilink` 变体，不退回 `.md#heading` 形式。
- 如果链接目标在文档库外部，比如官网、GitHub、微信文章，继续使用普通 Markdown 链接。
- 改完页面标题或路径后，回看内部链接是否仍然自然、可读、可迁移。

## 1.6 处理已有目录

处理已有目录时，优先做四件事：

1. 先读每个目录里的 `README.md` 和 `INDEX.md`。
2. 看看它到底在服务什么主题，是否和别的目录重复。
3. 如果目录已经在用，就在它下面扩展，不要另起平行目录。
4. 如果目录职责太杂，就拆子目录和索引，但保留旧入口一段时间。

对已有目录的常见动作：

- 补 `README.md`
- 补模板
- 补索引
- 补回链
- 补 `log.md`

不要因为目录“看起来旧”就直接清空；更稳妥的做法是先把它标成归档或低优先级，再逐步迁移。

## 1.7 文档生命周期

一份内容通常会经历这几个状态：

1. `inbox/`：临时收口，等待清洗。
2. `raw/`：确认是原始来源后，作为证据层保留。
3. `articles/` / `concepts/` / `indexes/`：整理后的主知识层。
4. `archive/`：不再作为默认入口，但还需要保留历史价值。

处理规则：

- 合并重复内容时，保留一个主页面，其他页面转为指向主页面的说明或历史记录。
- 页面失效但仍有参考价值时，放进 `archive/`，不要直接丢弃。
- 只有空文件、误建页、无引用重复页，才考虑删除。
- 任何归档、合并、删除动作都要同步更新链接、索引和 `log.md`。

## 1.8 附件和 Canvas

- 原始 PDF、图片、下载包等如果是证据来源，继续放 `raw/`。
- 截图、图表导出、示意图、Canvas、Excalidraw 这类支持性文件，优先放 `assets/`。
- 这类文件的名字尽量稳定，最好能看出日期、主题和用途。
- 如果某个 Canvas 只是在表达结构关系，优先在 `indexes/` 或 `concepts/` 里挂入口，再把可视化文件放到 `assets/`。

## 1.8.1 项目层平铺还是分目录

- 不要为了看起来模块化，就把只有一个 `README.md` 的内容放进子目录。
- 如果一个模块当前只有一个主文件，优先平铺，例如 `releases.md`。
- 如果一个模块已经有多个职责明确的文件，就保留目录，例如设计主入口 `design/README.md` 加上它的子页 `design/architecture.md`、`design/backend-frontend-structure.md`、`design/permission-boundary.md`、`design/write-boundary.md`、`design/database.md`、`design/deployment.md`、`design/runtime-quality.md`。
- `incidents/` 这类天然会累积多条独立记录的模块，默认保留目录。
- 现有内容优先保留；先根据内容是否已经长成多文件模块判断，再决定要不要收平。

## 1.9 软件研发模式

软件研发模式不是另一套系统，而是 `projects/` 的运行方式。

### 1.9.1 项目推进先读什么

1. 先读 `projects/README.md`
2. 再读 `projects/status.md`
3. 再读 `projects/STRUCTURE.md`
4. 再读 `projects/requirements.md`
5. 再读 `projects/design/README.md`
6. 再读 `projects/design/tech-selection.md` 和 `projects/design/architecture.md`
7. 涉及代码落点时再读 `projects/design/backend-frontend-structure.md` 和 `projects/design/permission-boundary.md`
8. 涉及写动作收口时再读 `projects/design/write-boundary.md`
9. 涉及状态、字段和迁移时再读 `projects/design/database.md`
10. 涉及部署、发布、回滚、监控或补偿时，再读 `projects/design/deployment.md` 和 `projects/design/runtime-quality.md`
11. 有冲突再读 `projects/decisions.md`
12. 涉及记忆或规则再读 `projects/memory/README.md` 和 [[POLICY]]
13. 如果这次主要是会议材料或会议规则，再读 `projects/meetings/README.md` 和 `projects/meetings/worklog.md`

### 1.9.2 项目主页怎么用

- 项目主页负责状态、范围、下一步和关键链接。
- 项目主页不写长篇设计，不写长篇决策，不写过程流水。
- 如果项目主页和其他页面冲突，以项目主页和 `projects/decisions.md` 为准。

### 1.9.3 记忆 / 规则怎么用

- [[BRAIN]] 负责共享背景。
- `projects/memory/` 负责项目级稳定记忆。
- [[POLICY]] 负责规则、优先级和自动沉淀边界。
- `projects/decisions.md` 负责项目冲突和拍板。

### 1.9.4 需求到设计

- 需求先说明为什么做、做给谁、范围是什么。
- 如果输入材料是一份 PRD 或需求草稿，先按 [[concepts/prd-writing]] 的结构收成问题、目标、范围、规则和验收，再写进 `projects/requirements.md`。
- 设计再说明怎么做、模块怎么切、数据怎么走。
- 如果 PRD 里混了多个候选方案或争议口径，先回到 `projects/decisions.md` 拆清楚，不要直接塞进设计正文。
- 如果设计会改变记忆路由或规则接线，先在设计页留入口，再回写相关页面。

### 1.9.5 设计到决策

- 设计里出现多个可选方案时，把比较结果写到决策页。
- 决策页默认保持单页主入口，不为每条决策先拆详情目录；优先在同一页里通过“当前生效决策摘要 -> 正式决策记录 -> 已覆盖 / 历史决策”三层结构来解决扫读和回看问题。
- 顶部摘要默认用数字编号条目，写成“`主题`：`决策`。`影响`：`影响摘要`”这种短句。
- `主题` 可以直接挂页内跳转，默认直接链接到同页正式条目的标题，不再引入 `^decision-03` 这类复杂 block id。
- 摘要区的 `决策` 和 `影响` 都只写一句摘要，不展开成长段，也不在摘要区罗列影响文件清单。
- `正式决策记录` 和 `已覆盖 / 历史决策` 里的决策标题默认保持简洁稳定，不额外加正文编号。
- 决策页默认按这组顺序写：`**背景**`、`**要决策什么**`、`**可选项**`、`**最终决策**`、`**影响**`、`**各自优劣**`、`**风险点**`。
- `**最终决策**` 和 `**影响**` 必须放在 `**各自优劣**`、`**风险点**` 之前，先让读者看到拍板结果和它影响什么，再看比较过程和风险。
- 决策记录要把背景、待拍板问题、候选方案、各自优劣和风险点写完整，不要只留下结论，也不要把整页写成第二份设计正文。
- 决策标题默认保持稳定，把日期写进字段，不写进标题；摘要和交叉引用默认直接链接标题。
- 设计页保留方案总览，不重复写所有争论细节。

### 1.9.6 决策到开发

- 开发页记录实际推进。
- 如果开发过程中发现决策不成立，先回到决策页，不要在开发页里悄悄改口径。
- 开发页如果发现稳定背景有变化，回写 `projects/memory/`。

### 1.9.6.1 完整架构包到研发拆解

当完整架构包已经成型，而下一步要进入实现拆解时，默认按这条链推进：

`完整架构包 -> 功能点 -> 接口 / 数据变更 -> 验证项 -> 发布项`

先后顺序不要反过来。不要一上来直接写功能点实现卡，也不要跳过验证和发布回填。

#### 第一步：先读完整架构包

1. 先看 `projects/design/README.md`，确认当前完整架构包是否已经收口。
2. 再按顺序读：
   - `projects/design/tech-selection.md`
   - `projects/design/architecture.md`
   - `projects/design/backend-frontend-structure.md`
   - `projects/design/permission-boundary.md`
   - `projects/design/write-boundary.md`
   - `projects/design/database.md`
   - `projects/design/deployment.md`
   - `projects/design/runtime-quality.md`
3. 读完后先回答 5 个问题：
   - 这轮要落的主链路是哪一段
   - 这段链路对应哪些页面 / 角色 / 动作
   - 涉及哪些 API / 服务端动作
   - 涉及哪些表、字段、状态机或迁移
   - 涉及哪些验证、发布、回滚或补偿约束

如果这 5 个问题还答不清，就先回设计层补齐，不进入研发拆解。

#### 第二步：从架构包拆成功能点

1. 先按业务闭环拆，不按技术文件拆。
2. 一个功能点至少要能回答：
   - 它属于哪个模块
   - 它完成的是哪一段用户动作或运营动作
   - 它的验收口径是什么
   - 它依赖哪几个设计页和决策页
3. 功能点粒度要满足“单独推进、单独验证、单独记录结果”。
4. 如果一个条目同时跨太多页面、接口、状态和角色，就继续往下拆。
5. 如果一个条目只是很小的实现细节，不足以独立验收，就并回所属功能点，不单开卡。

拆完后，把功能点写进 `projects/development/feature-points/`，并让 `projects/development/README.md` 只保留活跃入口和整体推进状态。

#### 第三步：为每个功能点补接口 / 数据变更

每个功能点至少补齐这 4 件事：

1. 相关页面或入口动作
2. 相关 API / 服务端动作
3. 相关数据表、字段、状态机或迁移
4. 相关部署、运行质量或补偿约束

推荐写法：

- 页面和角色边界，回链到 `projects/design/architecture.md`
- 代码落点和模块边界，回链到 `projects/design/backend-frontend-structure.md`
- 表、字段、索引、迁移，回链到 `projects/design/database.md`
- 上传、环境、回滚、监控、幂等、补偿，回链到 `projects/design/deployment.md` 和 `projects/design/runtime-quality.md`

如果某个功能点需要新增接口、迁移或运行约束，而设计页还没有对应口径，先回设计页补，不直接在功能点页发明第二套方案。

#### 第四步：为每个功能点补验证项

验证项不要等到发布前再补。功能点拆出来时就一起写。

最少覆盖：

1. 主链路成功路径
2. 关键状态迁移
3. 权限和角色边界
4. 失败路径或异常路径
5. 如果涉及上传、异步、补偿或回滚，再补运行侧验证

验证记录的落点：

- 功能点自己的验收和结果，写在对应功能点页
- 时间顺序的实现、联调、排障和验证过程，写到 `projects/development/worklog.md`
- 如果验证结果改变了当前实现口径，再同步回 `projects/trace.md`

#### 第五步：为每个功能点补发布项

不是所有功能点都立即进入发布，但每个功能点都要提前判断发布影响。

至少回答：

1. 是否涉及数据库迁移
2. 是否涉及配置变更
3. 是否涉及上传 / 下载链路变更
4. 是否需要补监控、告警或补偿任务
5. 上线后如果失败，最小回滚动作是什么

当一组功能点准备上线时，再把这些内容汇总到 `projects/releases.md`，不要等发布时重新从头猜。

#### 第六步：同步回写

这条链路里每一步都不是孤立文件操作。

默认同步关系：

- 功能点目录和实体页：`projects/development/feature-points/`
- 整体推进状态：`projects/development/README.md`
- 过程流水：`projects/development/worklog.md`
- 实现口径变化：`projects/trace.md`
- 新取舍或冲突：`projects/decisions.md`
- 稳定背景：`projects/memory/README.md`
- 发布结论：`projects/releases.md`

#### 第七步：交付前最小检查

进入收尾前，至少检查：

1. 架构包里对应设计页是否都能回链到当前功能点
2. 功能点是否已经带上接口 / 数据 / 验证 / 发布影响
3. `projects/development/README.md`、功能点页、`projects/status.md` 是否一致
4. 如果口径有变化，`projects/trace.md` 是否已经同步
5. 如果准备发布，`projects/releases.md` 是否已经有最小可执行内容

### 1.9.7 开发到发布

- 发布页说明上线范围、验证方式和回滚方案。
- 发布结束后，如果有稳定结论，优先回写到 `projects/memory/` 或知识库层。

### 1.9.8 发布到事故

- 事故页只负责事故总览、单条事故和复盘入口。
- 事故复盘里得到的长期结论，优先回写到 `projects/memory/`、[[POLICY]] 或 `projects/decisions.md`。

### 1.9.9 智能体功能研发：从需求到设计

- 先把问题定义清楚，再把输入、输出、边界和验收写清楚。
- 如果原始输入是一份 PRD，先把它收敛成 `projects/requirements.md`，再让智能体进入设计拆解。
- 如果要让智能体参与推进，至少要有项目主页、需求页和设计页三件套。

### 1.9.10 智能体功能研发：从设计到决策

- 设计里所有会影响后续自动化的判断，都应当单独落到决策页。
- 决策页要能回溯到需求、设计和当时约束。

### 1.9.11 智能体功能研发：从决策到开发

- 开发推进时，先读决策页，再读设计页。
- 如果智能体需要项目级长期背景，就先读 `projects/memory/`。

### 1.9.12 智能体功能研发：从开发到上线

- 上线前先回看发布页和事故入口。
- 如果上线后产生了稳定结论，把它们回写到 `projects/memory/`、[[POLICY]] 或知识库层。

### 1.9.13 功能点双轴模型

- 设计拆成模块以后，再把模块拆成功能点。
- 功能点用两个正交字段管理：`status` 和 `phase`。
- `status` 只表示生命周期：`planned`、`active`、`blocked`、`done`、`released`、`archived`。
- `phase` 只表示串联步骤：`design`、`implementation`、`verification`、`release`。
- `status` 和 `phase` 不是平级标签，而是串联关系。
- `blocked` 是叠加态，可以落在任何 `phase` 上。
- 旧的 `in_progress` 口径以后统一拆成 `status=active + phase=*`，不再作为单字段主轴。
- 功能点模板放在 [[projects/development/README]]。
- 功能点实体页放在 [[projects/development/feature-points/README]]，每个功能点一页，不把多个功能点正文塞在同一页。
- `status` 和 `phase` 写在功能点页的 frontmatter 或页面属性里。
- 三层职责固定为：`projects/README.md` 偏首席技术官 / 项目负责人视角，`projects/development/README.md` 偏研发经理视角，`projects/development/feature-points/README.md` 和其下实体页偏工程师视角。
- 过程日志放在 [[projects/development/worklog]]。
- 全局状态镜像放在 [[projects/status]]。
- 发布结论放在 [[projects/releases]]。
- 异常和复盘放在 [[projects/incidents/README]]。
- 稳定背景回写 [[projects/memory/README]]，取舍回写 [[projects/decisions]]，规则变化回写 [[POLICY]]。

### 1.9.14 状态怎么维护

- 开始前，先把功能点所属模块、目标、验收、依赖和负责人写清楚。
- 先定 `phase`，再定 `status`。
- `phase` 表示现在做到哪一步，`status` 表示这张卡是否活跃、被卡住、已完成或已发布。
- 功能点实体页一页一个功能点，不把多个功能点放在同一页。
- 进行中，`phase` 只沿串联链路前进，不要在 `design`、`implementation`、`verification` 之间来回改口。
- `status` 只在生命周期切换时改，比如 `planned -> active -> blocked -> done -> released -> archived`。
- 验证通过后，再把 `status` 从 `active` 收到 `done`；真正上线后，再改成 `released`。
- 如果被卡住，保留当前 `phase`，只把 `status` 改成 `blocked`，并写清阻塞原因、依赖对象和下一步。
- 如果功能点不再推进，就归到 `archived`；如果被替代，就标成 `superseded`。
- 如果一个功能点在 `done` 之后又要做修复，不要直接倒回原卡，优先新开修复点或事故记录，保留原卡的完成结果。

### 1.9.15 会议管理：从议程到纪要到分流

- 正式会议优先有一个明确的会议标题、目标和结论记录，不把逐字转录当主正文。
- 会前材料和议程先收在 `inbox/` 或 `raw/`，确认是项目内材料后，归入 `projects/meetings/` 所辖的会议入口。
- 如果会前需要发给对方提前看，就先单独做一页可分享的会前材料 / 议程页；`projects/meetings/worklog.md` 主要承担会后归档和时间线，不作为对外预读的唯一入口。
- 如果某场会已经有独立会前材料页，这张页就是会前信息的单一信息源；`projects/meetings/worklog.md` 不再重复维护讨论方式、会议节奏、完整议题、会前材料清单和预期结果，只保留链接、会后结论、待办和分流。
- 如果同一场会同时在独立会议页和 `projects/meetings/worklog.md` 出现了大段重复正文，优先保留独立会议页里的会前内容，并在同一轮把 `worklog` 收平；不要接受“两边都保留完整信息，之后再慢慢整理”的中间态。
- 会中只记结论、待办、风险、owner 和需要继续确认的问题。
- 正式会议默认要有“会后可回看”的结论和待办清单，不能长期停留在“待会议确认”的空壳状态。
- 会议待办默认至少写清：动作内容、owner、时间、当前状态。
- 会议待办正文放在各自会议记录里：普通会议写在 `projects/meetings/worklog.md` 对应条目下；大型会议如果单独拆页，就写在该会议文件内部；`WORKFLOW` 只定义维护规则，不汇总各场会的任务清单。
- 单条会议记录内部也要职责分离：
  - `议题` 只写待回答问题，不重复结论。
  - `结论` 只写会后确认结果，不重复背景、链接或动作说明。
  - `行动项` 只保留会后仍需跟踪的事项；已经完成且不再需要追踪的同步动作，优先并入 `结论` 或直接删除，不再占一个 action。
  - `分流` 和 `关联链接` 只保留这场会真正需要额外指向的页面；默认分流、重复链接和模板占位不保留。
- 会后按结果分流：
  - 拍板和取舍进 `projects/decisions.md`
  - 需求变化和范围收敛进 `projects/trace.md`
  - 开发动作和验证进 `projects/development/worklog.md`
  - 稳定背景进 `projects/memory/README.md`
- 当分流后的承接页推进了会议中的某条事项，同轮把对应会议记录里的结论或待办状态一起回写；这里要求显式同步，不做隐藏自动流控。
- 如果只是开发过程中的临时讨论、联调插会或排障沟通，可以直接记到 `projects/development/worklog.md`；如果是正式会议，默认写 `projects/meetings/worklog.md`
- 会议记录默认一场会对应一条记录，不把多场会揉成一条总记录
- 如果某类会议开始反复出现，再考虑把固定字段继续收紧成模板或索引；会议记录模板优先看 [[templates/meeting-entry-template]]
