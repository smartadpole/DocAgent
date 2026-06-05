---
type: concept
id: CONCEPT-PROBLEM-FOCUSED-INFORMATION-PRESENTATION-001
status: active
updated: 2026-06-05
tags: [information-architecture, presentation, knowledge-base, lens, context]
---

# 问题聚焦式信息呈现

问题聚焦式信息呈现，是指在复杂知识库、项目系统、生活系统或运行系统中，不以“某个项目总览页”或“某种固定 dashboard”为中心，而以读者当前正在关注的问题为中心，临时组装最合适的阅读视角。

它的核心判断是：同一批 [[concepts/ai-era-information-presentation|Markdown 真相源、关系链接、索引和呈现层]]，在不同问题下应该生成不同 lens。用户不是每次都需要看完整系统，而是需要快速判断“这件事现在是什么状态、为什么、下一步是什么、证据在哪里、哪些边界不能上推”。

## 解决什么

复杂系统变乱，通常不是因为没有总览，而是因为所有问题都被迫进入同一种总览：

- 状态问题被塞进长文档，读者找不到当前态。
- 决策问题被塞进状态页，候选、取舍和待确认项混在一起。
- 计划问题只剩行动清单，看不到约束和依赖传播。
- 故障和 issue 只剩结论，看不到原始现象和证据层级。
- 知识专题只剩摘要，看不到来源、上位概念、邻接关系和适用边界。

问题聚焦式信息呈现的目标不是替代真相源，而是在每次阅读时生成一个低噪声、图文混排、适合一眼判断的阅读界面。

## 基本模型

每一次呈现都先回答六个问题：

| 步骤 | 要回答的问题 | 输出 |
| --- | --- | --- |
| 关注对象 | 用户此刻关心的是哪一类问题 | 状态、计划、决策、故障、验收、知识、资源、关系、时间线等 |
| 判断目的 | 用户要做什么判断 | 看懂、比较、行动、验收、追责、回顾、学习、沉淀 |
| 信息类型 | 本轮主要涉及哪些信息 | 事实、证据、状态、任务、约束、风险、owner、材料、代码、服务、资产 |
| 视图 lens | 哪种展示结构最省认知 | 状态卡、证据链、决策矩阵、行动地图、时间线、关系图、专题卡 |
| 证据边界 | 哪些结论可以上推，哪些只能辅助 | confirmed / likely / possible / blocked，或 local / service-side / end-to-end |
| 追溯入口 | 深挖时回到哪里 | 源页面、报告、log、raw、issue、TASK、决策、会议、数据快照 |

这套模型接在 [[concepts/ai-era-information-presentation]] 的五层架构之后：源、索引、关系、界面、归档解决信息系统怎么组织；问题聚焦式呈现解决读者面对一个具体问题时应该怎样看。

## 最终呈现形态

问题聚焦式信息呈现的最终阅读形态，复杂场景下应优先是图文混排 lens。HTML 是当前最适合作为默认容器的形态，但不是能力上限。

这里的趋势不是“HTML 本身成为趋势”，而是信息呈现从长 Markdown / 长文档转向可交互、可视化、可追溯的页面化 lens。Markdown / 数据 / 报告 / log 仍是真相源；HTML、Notebook、dashboard、Artifact、Canvas、Mermaid、ECharts / D3、SVG 和图片只是呈现层的不同载体。

这里要区分两件事：

| 层级 | 默认形态 | 职责 |
| --- | --- | --- |
| 真相源 / 生成输入 | Markdown、frontmatter、wikilink、报告、log、raw、数据快照 | 保存事实、关系、版本、证据和审计路径 |
| 处理 / 组装 | 搜索、索引、RAG、agent 摘要、规则化 lens 模板 | 从真相源中抽取当前问题需要的上下文 |
| 最终呈现 / 阅读界面 | HTML report、HTML card、Notebook、Artifact、dashboard、Obsidian webview、图表、脑图、框图 | 让人低成本比较、筛选、钻取、判断和行动 |
| 归档 / 分发 | 静态 HTML package、PDF、MHTML、WARC | 固化某次视图、筛选条件、数据快照和证据包 |

因此，Markdown 不应被当作复杂信息的最终阅读体验。它更适合作为可维护、可 diff、可链接、agent 友好的真相源；HTML 更适合作为面向人的呈现层，尤其当信息需要折叠、过滤、排序、状态色、关系图、时间线、证据 drill-down 或多视角切换时。

最小可行形态可以先用 Markdown 描述 lens 结构；但一旦信息复杂到影响阅读判断，就应生成图文 lens。HTML 如果能承载表格、脑图、框图、流程图、关系图、时间线、状态卡和证据 drill-down，就优先使用 HTML；如果 HTML 排版或交互表达不足，应补充 SVG、Canvas、Mermaid、ECharts / D3、Excalidraw 导出图、PDF / slide、独立图片或 HTML + assets 组合包。呈现层不能脱离源：页面必须暴露来源、更新时间、筛选条件、证据边界和回链，避免变成第二份不可审计的真相源。

## 图文混排能力

“一图胜千言”是这个专题的首要体验目标。复杂文字信息应尽量转成可视结构，让读者先看懂关系，再决定是否读原文。

| 信息形态 | 优先图文形式 | 适合解决的问题 |
| --- | --- | --- |
| 候选方案、状态对比、验收缺口 | 表格、矩阵、热力色块 | 哪个更好、哪里没闭合、差异是什么 |
| 主题结构、知识分支、来源分布 | 脑图、树图、主题地图 | 一个主题由哪些子问题和来源组成 |
| 系统结构、模块边界、服务调用 | 框图、架构图、边界图 | 谁依赖谁、边界在哪里、责任归谁 |
| 动作顺序、计划推进、故障处理 | 流程图、泳道图、行动地图 | 下一步怎么走、卡在哪里、谁接手 |
| 历史变化、阶段推进、事件链 | 时间线、里程碑图 | 为什么变成现在这样、关键转折是什么 |
| 文档 / 主题 / owner / 证据关系 | 关系图、网络图、引用地图 | 多个文档之间怎样互相支撑或冲突 |
| 当前态、风险、下一步 | 状态卡、看板、仪表块 | 一眼判断现在该知道什么 |

如果某个 lens 只能输出长段文字，说明它还没有完成呈现层任务。文字应主要承担解释、边界和追溯职责；关系、结构、状态、比较和路径应优先图形化。

## 展示对象粒度

用户要看的对象可以是一份文档，也可以是一个主题。两者的 source pack 和背景呈现不同：

| 对象粒度 | 主问题 | source pack | 必须呈现的背景 |
| --- | --- | --- | --- |
| 单文档 lens | 这份文档讲什么、是否可信、怎么用 | 当前文档、frontmatter、出链 / 入链、相关 log / report | 所属上位主题、产生原因、适用边界、相关文档、当前是否仍有效 |
| 主题 lens | 这个主题整体是什么状态、有哪些材料、结论怎么收敛 | 多份文档、入口页、概念页、报告、决策、log、raw / assets | 主题地图、材料分层、关键结论、争议 / 冲突、演进时间线、未覆盖来源 |

单文档 lens 不能只做摘要；它要告诉读者这份文档在整个知识网络里处于什么位置。主题 lens 不能只合并摘要；它要把多个文档之间的层级、证据关系、冲突、背景和当前裁决呈现出来。

每个图文 lens 都应有一个背景框：

- **上位背景**：属于哪个项目、主题、概念、计划或事件。
- **来源背景**：本轮读取了哪些文档，哪些只是邻接未读。
- **历史背景**：它是新结论、旧结论修正、阶段快照，还是历史证据。
- **关系背景**：它和哪些文档、owner、任务、风险、决策或资产相连。
- **使用边界**：当前结论适合用于什么判断，不适合上推到哪里。

## 图文 lens 生命周期

当多次对话都问到同一个关注问题时，不能每次都无条件生成一个平行呈现文件，也不能简单覆盖到失去历史。应把图文 lens 分成两类：

| 类型 | 更新方式 | 适用场景 | 保留内容 |
| --- | --- | --- | --- |
| 当前视图 / canonical lens | 同一关注对象持续更新同一个当前入口 | 用户反复查看同一个问题、状态、计划、风险或知识主题 | 最新结论、当前证据、当前下一步、源回链、更新时间 |
| 对话快照 / snapshot lens | 重要节点另存不可变快照 | 验收、决策、发布、事故、阶段复盘、外部分发、证据需要固化 | 当时的筛选条件、数据快照、生成时间、对话 / log / commit 回链 |

默认规则是：同一个稳定关注对象维护一个 canonical lens；只有当本轮视图具备审计、归档、分发或阶段证据价值时，才额外生成 snapshot。普通追问、轻量刷新和同一问题的连续澄清，应更新 canonical lens，而不是制造一堆无法辨认的新文件。

如果一个问题还没有稳定到可命名的关注对象，先用临时图文视图或对话内 artifact；等它稳定后再创建 canonical lens。临时视图不应悄悄混入长期视图体系。

## 图文 lens 存放体系

图文 lens 不应散落在各个源页面旁边。源文件属于记录层，呈现 lens 属于呈现层，两者职责不同。推荐未来单独设一个呈现层目录，例如：

```text
views/
  README.md
  lens-registry.md
  current/
    status/
    plans/
    decisions/
    risks/
    acceptance/
    knowledge/
    resources/
    timelines/
  snapshots/
    2026/
      06/
```

其中：

- `views/README.md`：面向用户的呈现层入口，说明有哪些常用视图。
- `views/lens-registry.md`：记录每个图文 lens 的稳定 id、关注对象、主源页面、当前视图、快照、更新时间和失效条件。
- `views/current/`：放当前可反复打开的 canonical lens，按用户关注对象组织。
- `views/snapshots/`：放需要固化的历史快照，按日期或事件归档。

HTML / 图文 lens 内部必须带最小 provenance：

| 字段 | 含义 |
| --- | --- |
| lens_id | 稳定视图 id |
| focus_object | 关注对象 |
| lens_type | status / plan / decision / risk / acceptance / knowledge / resource / timeline |
| source_pages | 生成该视图的主源页面 |
| source_scope | 单文档 / 主题 / 项目 / 运行实例等对象粒度 |
| generated_at | 生成或更新时间 |
| source_revision | 相关 commit、报告版本或数据快照 |
| evidence_boundary | 证据可上推范围和未验证边界 |
| context_frame | 上位背景、来源背景、历史背景、关系背景和使用边界 |
| snapshot_of | 如果是快照，指向 canonical lens |
| user_entry | 用户从哪个入口进入：看状态、要行动、要验收、找资源等 |
| canonical_policy | 什么时候覆盖当前视图，什么时候保留原视图 |
| snapshot_policy | 什么时候必须另存不可变快照 |
| staleness_policy | 哪些源变化会让当前视图过期 |
| refresh_trigger | 用户追问、源页面更新、报告新增、服务状态变化等刷新触发条件 |

## 同一问题再次被问起

当用户在多次不同对话中问到同一个稳定关注对象时，处理顺序应是：

1. 先解析关注对象和 lens 类型，找到或创建稳定 `lens_id`。
2. 查询 `views/lens-registry.md`，确认当前 canonical lens、主源页面、快照和失效条件。
3. 重新读取最小 source pack，而不是直接复述旧视图。
4. 如果源事实变化，更新 canonical lens；如果源事实未变，只更新访问记录或回答引用。
5. 如果本轮形成验收、决策、发布、事故、阶段复盘或外部分发证据，再额外生成 snapshot lens。
6. 最终回复引用更新后的 lens，并说明更新时间、证据边界和未刷新来源。

这个流程解决的是“同一问题到底更新同一个 current 视图，还是每次生成新文件”的问题：默认更新同一个 current lens；只有关键节点才新增 snapshot。

## 用户视角体系

图文 lens 体系应从用户视角组织，而不是从底层文件路径组织。用户打开呈现层时，第一层看到的不是 `projects/`、`articles/`、`raw/` 这些维护目录，而是自己想判断的事情：

| 用户入口 | 典型问题 | 对应 lens |
| --- | --- | --- |
| 我现在要看状态 | 这件事到哪了 | status lens |
| 我现在要行动 | 接下来做什么 | plan lens |
| 我现在要拍板 | 选哪个方案 | decision lens |
| 我现在担心风险 | 可能出什么事 | risk lens |
| 我现在要验收 | 能不能算完成 | acceptance lens |
| 我现在要理解知识 | 这个结论怎么复用 | knowledge lens |
| 我现在要找东西 | 文件、资产、服务在哪里 | resource lens |
| 我现在要复盘过程 | 为什么变成这样 | timeline lens |

同一个源页面可以被多个 lens 使用；同一个 lens 也可以引用多个源页面。体系的单一信息源仍是 Markdown / 数据 / 报告，用户视角体系只负责把这些源重组为可阅读、可钻取、可归档的图文视图。

## 跨工程校准结论

对 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 的只读抽样显示，问题聚焦式信息呈现不能只停留在“关注对象分类”，还必须解决 current / snapshot、源刷新、证据上推和用户入口体系：

| 样本暴露的压力 | 方案修正 |
| --- | --- |
| Life 这类生活系统把行动、约束、资产、知识和风险混在同一输入里 | 同一输入可生成行动 lens、计划 / 约束 lens、风险 lens 和知识 lens，但源仍按 LifeOS 的领域 / 项目 / 日志分层保存 |
| DocCustomeranalysis 这类主控系统里报告、issue、TASK、服务台账和状态页会互相引用 | 当前裁决必须来自 canonical status / issue / acceptance lens；历史报告只作为 snapshot evidence，不能自动代表当前态 |
| prefect 这类运行系统把 progress、stage_progress、artifact、log 和测试组合成用户可读状态 | 运行状态 lens 要展示原始 payload、规范化规则、用户可见日志、artifact 和测试证据之间的映射 |
| fetch-adapter 这类服务边界系统需要解释 run、artifact、handoff 和上游调度合同 | 服务 lens 不只显示健康检查，还要显示 run 锚点、阶段进度、产物位置、取消 / 重跑语义和归属边界 |
| DocFilmCommunity 这类研发主控系统状态页很长，阻塞和分工密集 | 默认入口应是 blocker-first status lens：一屏看当前能否推进、谁要交什么、为什么不能准出 |

详细样本分析见 [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]。

## 关注对象分类

关注对象是 lens 选择的第一层。用户说“我在看一个事情”时，先判断这个“事情”主要属于哪一类；一个问题可以命中多类，但必须先选主 lens，再把其他类作为辅助层。

| 关注对象 | 核心问题 | 默认展示重点 |
| --- | --- | --- |
| 状态 | 现在到哪了 | 当前态、阶段、阻塞、下一步、状态来源 |
| 问题 / 故障 / 异常 | 哪里不对 | 原始现象、影响范围、证据链、根因候选、验证边界 |
| 决策 | 该选哪个 | 候选方案、取舍维度、已确认、待确认、裁决记录 |
| 计划 | 接下来怎么做 | 目标、约束、时间窗、依赖、可执行动作、blocked 条件 |
| 风险 | 可能出什么事 | 触发条件、影响对象、概率 / 影响、缓解动作、剩余风险 |
| 验收 / 关闭 | 能不能算完成 | 验收对象、关闭标准、证据层级、缺口、人工确认边界 |
| 知识 | 这条知识怎么理解和复用 | 结论、来源、上位概念、邻接关联、适用边界 |
| 资源 / 资产 | 东西在哪里、能不能用 | 位置、版本、权限、用途、归档和追溯入口 |
| 关系 / owner | 谁和谁有关、谁确认 | 责任边界、协同方、依赖关系、确认状态 |
| 时间线 / 演进 | 事情怎么变成现在这样 | 关键节点、转折点、状态变化、仍未闭合的影响 |

如果用户的问题只说“这个问题怎么样”，不能直接套“问题 / 故障” lens；要先判断他要看的是状态、决策、计划、风险、验收还是知识。`问题` 在这里既可以是泛称，也可以是已发生异常，不能混用。

## 通用 lens

| 当前关注问题 | 一眼判断层 | 证据解释层 | 原始追溯层 |
| --- | --- | --- | --- |
| 当前状态是什么 | 状态、阶段、阻塞、下一步 | 状态来源、最近变化、未同步风险 | 项目主页、状态页、log、最新报告 |
| 接下来该做什么 | 可执行动作、优先级、依赖 | 约束传播、资源、时间窗、blocked 条件 | 计划页、会议、风险、外部确认 |
| 这个结论可信吗 | 裁决、证据等级、未验证边界 | 来源、样本、环境、反例、不能上推原因 | 原始证据、测试报告、数据快照 |
| 为什么变成这样 | 关键事件链、转折点 | 需求变化、决策、issue、风险触发 | trace、decisions、log、会议记录 |
| 是否可以关闭 / 验收 | 关闭结论、缺口、人工确认项 | local / service-side / end-to-end 证据和回归范围 | TASK / EP / issue / AP / report |
| 应该选哪个方案 | 推荐倾向、候选对比、待拍板项 | 评价维度、权衡、风险、适用条件 | 调研、决策页、设计专题、来源 |
| 这个风险怎么处理 | 风险等级、触发条件、当前处置 | 影响对象、缓解动作、剩余风险、准出影响 | risk、会议、决策、后续任务 |
| 这个知识怎么复用 | 一句话结论、适用场景、禁用场景 | 来源、上位概念、邻接概念、案例 | article、concept、template、skill |
| 这个东西在哪里 | 当前位置、所属层级、主入口 | 命名、目录、单一信息源、相关对象 | INDEX、README、目录页、原始路径 |
| 谁负责 / 谁确认 | owner、协同方、确认状态 | 权限、责任边界、会议或外部确认 | 会议、决策、风险、handoff |
| 发生过什么 | 时间线、关键节点、当前影响 | 每个节点的动作、证据和状态变化 | log、worklog、report、raw |

这些 lens 不是固定页面模板，而是阅读协议。简单场景可以只用 Markdown 生成简短视图；复杂场景的优先呈现形态应是图文混排 lens，可以由 HTML report、HTML card、Notebook、Artifact、dashboard、图表或图片组合承载。但任何呈现层都必须能回到源和证据。

## 输出形态选择

输出形态由当前关注对象和阅读压力决定，不由文件后缀决定：

| 场景 | 适合形式 | 判断理由 |
| --- | --- | --- |
| 简单问答、位置确认、一次性判断 | 短 Markdown | 用户只需要高信号答案，不需要持久视图 |
| 状态、风险、计划、验收 | lens 页面 / 状态卡 / 矩阵 | 需要同时看当前态、阻塞、下一步和证据边界 |
| 故障排查、证据链 | timeline + evidence table + fault tree | 需要保留现象、证据、根因候选和验证范围 |
| 决策比较 | decision matrix | 需要显式呈现候选、取舍维度、已确认和待确认 |
| 项目 / 知识库长期维护 | canonical current lens + snapshot 归档 | 高频问题要刷新当前视图，关键节点要固化证据 |
| 数据量大、需要筛选钻取 | HTML report / Notebook / dashboard / data app | 需要交互筛选、图表组合和复现 |
| 只是说明文档或稳定规则源 | Markdown | 真相源、版本管理、diff 和 agent 可读性优先 |

## 信息类型视角

面对所有信息类型时，优先判断它在当前问题中承担什么角色：

| 信息类型      | 展示重点              | 常见反模式           |
| --------- | ----------------- | --------------- |
| 事实        | 是否已确认、来源、更新时间     | 把历史事实当当前事实      |
| 证据        | 层级、环境、样本、可上推范围    | 用单个成功截图替代闭环证明   |
| 状态        | 当前态、状态来源、下一状态条件   | 在多个页面重复维护状态正文   |
| 计划        | 目标、约束、依赖、可执行动作    | 只列 TODO，不判可执行性  |
| 决策        | 候选、取舍维度、裁决和待确认    | 把讨论过程写成最终决策     |
| 风险        | 触发条件、影响对象、缓解和剩余风险 | 把未发生风险预建成 issue |
| 问题 / 故障   | 原始现象、当前裁决、验证边界    | 用推测根因改写用户可见现象   |
| 验收        | 对象、方案、证据层级、人工边界   | 把局部通过写成完整通过     |
| 知识        | 结论、适用边界、上位和邻接     | 只写摘要，不建立知识网络    |
| 资源 / 资产   | 位置、版本、权限、用途       | 只在聊天里描述，文件不可追溯  |
| 人 / owner | 职责、确认状态、协同路径      | 让 agent 代替人工拍板  |
| 时间线       | 事件、转折、影响、未闭合项     | 把流水账当当前判断       |

## 和现有专题的关系

- [[concepts/ai-era-information-presentation]] 回答信息的记录、组织、处理、呈现和归档如何分层。
- [[articles/2026-06-05-ai-era-information-presentation-research]] 提供格式、技术和历史谱系上的调研依据。
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]] 用 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 校准 current / snapshot、源刷新和用户入口体系。
- [[skills/problem-focused-visual-presentation/SKILL]] 把本专题升级为 agent 可执行的图文 lens 生成流程。
- [[governance/knowledge-linking-rules]] 回答新增知识如何建立上位、邻接、入口和反向链接。
- [[governance/response-mode-routing]] 回答 agent 本轮应快速诊断、沉淀、验收、实现还是规则升级。
- [[governance/state-constraint-reasoning]] 是计划型问题 lens 的底层方法。
- [[projects/development/plan/work-item-system-model]] 是研发事项、issue、验收和证据 lens 的一个具体应用。

## 设计原则

- 先定关注问题，再选展示结构。
- 先判这是短答、说明源文档、页面化 lens、交互报告还是归档快照；不要把“HTML 呈现”当成唯一答案。
- 展示层优先面向图文混排 lens 演进，HTML 是默认容器但不是上限；它不做第二份真相源，只重组、压缩、引用、可视化和钻取。
- 关系、结构、路径、比较和状态优先图形化；文字主要负责解释、边界和追溯。
- 无论对象是一份文档还是跨多文档主题，都必须呈现它所处的上位背景、来源背景、历史背景、关系背景和使用边界。
- 一眼判断层必须短，证据解释层必须能说明为什么，原始追溯层必须能回到源。
- lens 可以动态生成，但它的来源、更新时间、筛选条件和未验证边界要显式。
- 不同系统可以有不同默认 lens，但底层协议面对所有信息类型都一致。
- 视觉形式服从判断目的：有时是 HTML 状态卡，有时是交互时间线，有时是矩阵、脑图、框图或图谱；只有简单问题才退回 10 行高信号摘要。

## 常见误区

- 把问题聚焦式呈现误解成统一 dashboard。
- 把 Life、DocCustomer 或某个工程当成目标对象，而不是用于校准复杂度的参考样本。
- 因为真相源用 Markdown，就把最终阅读界面也停留在 Markdown。
- 因为 HTML 适合复杂呈现，就把所有内容都 HTML 化。
- 把 HTML / Artifact 当作方案本身，忽略表格、脑图、框图、时间线、关系图等真正降低认知成本的表达。
- 只总结当前文档，不呈现它所处的主题背景、历史背景和关系背景。
- 把所有信息类型都压成任务列表。
- 为了直观牺牲证据边界，导致读者误以为局部证据已经完整闭环。

## 后续演进

- 可以为高频问题沉淀 `lens` 模板，例如状态 lens、计划 lens、决策 lens、issue lens、验收 lens、知识复用 lens。
- 可以把 lens 作为 agent 最终回复、HTML report 或知识库页面 webview 的结构化输出要求。
- 如果未来进入产品化或工具化，优先由 Markdown frontmatter、wikilink、搜索索引和生成式摘要共同生成 HTML / Obsidian 视图；在此之前，本页只作为知识库专题方案，不进入开发链路。

## 相关页面

- [[concepts/ai-era-information-presentation]]
- [[articles/2026-06-05-ai-era-information-presentation-research]]
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]
- [[skills/problem-focused-visual-presentation/SKILL]]
- [[governance/knowledge-linking-rules]]
- [[governance/response-mode-routing]]
- [[governance/state-constraint-reasoning]]
- [[projects/development/plan/work-item-system-model]]
