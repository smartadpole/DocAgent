---
name: problem-focused-visual-presentation
description: 问题聚焦式图文呈现技能。用于用户要看一份文档、一个主题、一个状态、风险、决策、计划、验收结论或复杂信息集合，并希望直观、图文混排、一图胜千言、HTML / 图表 / 脑图 / 框图 / 时间线 / PDF 导出 / 打印呈现时，生成可读、可追溯、带背景框和导出配置的 lens。
---

# Problem-Focused Visual Presentation

## 定位

本技能把复杂文字、文档、专题或项目状态重组为面向当前关注问题的图文 lens。

它不是摘要技能，也不是固定 dashboard 技能。它先判断用户现在想看什么，再选择表格、脑图、框图、流程图、关系图、时间线、状态卡或 HTML 组合版式，让用户先一眼看懂结构和判断，再按需追溯原文。

方法论主入口：[[concepts/problem-focused-information-presentation]]。

## 适用场景

- 用户说“信息乱”“阅读不方便”“一图胜千言”“做成图文”“直观展示”“HTML 呈现”。
- 用户要看一个文档，并需要知道它讲什么、在哪里、和哪些背景有关。
- 用户要看一个主题，且主题覆盖多个文档、报告、issue、计划、决策、log 或资产。
- 用户要看状态、风险、计划、决策、故障、验收、知识、资源、owner 或时间线。
- 用户要求把当前回答、专题材料或知识库内容整理成可阅读的图文视图。

## 边界

- Markdown、数据、报告和原始材料仍是真相源；图文 lens 只负责呈现，不成为第二份事实源。
- 不为了好看牺牲证据边界；必须写清来源、更新时间、未读来源和不可上推范围。
- 不默认创建持久 HTML 文件；只有用户要求持久呈现、专题沉淀或当前仓库已有 `views/` 体系时，才落文件。
- HTML 是默认容器但不是上限；HTML 不足时可用 Mermaid、SVG、Canvas、ECharts / D3、Excalidraw 图、PDF / slide、图片或 HTML + assets 组合包表达，但同一 lens 的 PDF / PNG / SVG 导出不能作为可提交资产重复保存。
- 趋势不是把所有内容 HTML 化，而是按当前问题生成可交互、可视化、可追溯的页面化 lens；简单问题仍然短答，说明文档仍然优先 Markdown。
- PDF / PNG 是导出 / 打印 / 分发产物，不是真相源；只要本轮生成或更新持久 HTML lens，就必须同步生成同源 PDF 和至少一张 PNG 截图 / 长图，放入 gitignore 忽略的导出目录，并在最终回复里展示 PNG 预览。如果 PDF 固化验收、决策、发布、事故或复盘节点，应按 snapshot 处理并保留生成源、版式配置和证据边界。
- 同一 lens 的 HTML、PDF、PNG 或 slide 必须来自同一源和同一 export profile，信息、结论、证据边界和版式语义保持一致；允许的差异只限于分页、纸张尺寸、交互降级、链接脚注 / 二维码等介质适配。
- 不在 Git 中同时提交同一 lens 的 HTML、PDF、PNG、SVG 等重复渲染物；可提交的是 canonical HTML / source / manifest，导出件进入 gitignore 忽略的 `views/exports/`、`views/.exports/`、`assets/views/` 等目录，或作为运行时下载生成。
- 如果本轮涉及验收、准出、关闭、状态推进或规则升级，必须回到对应主入口，不能用图文 lens 替代正式裁决。

## 工作流

### 1. 识别关注合同

先判断这次用户要看的对象和目的：

| 维度 | 选项 |
| --- | --- |
| 关注对象 | 状态 / 计划 / 决策 / 风险 / issue / 验收 / 知识 / 资源 / owner / 时间线 |
| 对象粒度 | 单文档 / 跨文档主题 / 项目状态 / 运行实例 / 决策 / 计划 / 风险 / 验收 / 知识 |
| 判断目的 | 看懂 / 比较 / 行动 / 验收 / 追责 / 回顾 / 学习 / 沉淀 |
| 输出载体 | 短答 / Markdown 真相源 / 聊天图文 / Markdown + Mermaid / HTML / HTML + assets / HTML report / print view / PDF download / PNG download / slide / 临时 artifact / 持久 view / snapshot |
| 持久性 | 临时回答 / canonical current / snapshot |
| 导出需求 | 不导出 / HTML 可打印 / PDF 下载 / PNG 下载 / PDF snapshot / slide |
| 版式配置 | A4 / A3 / custom，portrait / landscape，边距、页眉页脚、分页策略 |

如果用户只是要快速确认一个位置或名字，直接简答，不启动完整 lens。

### 1.1 选择输出形态

先判断本轮应输出什么，不要默认把所有内容做成 HTML：

| 场景 | 优先输出 |
| --- | --- |
| 简单问答、一次性判断 | 短 Markdown |
| 状态、风险、计划、验收 | lens 页面、状态卡、矩阵 |
| 故障排查、证据链 | 时间线、证据表、fault tree |
| 决策比较 | decision matrix |
| 项目 / 知识库长期维护 | canonical current lens；关键节点另存 snapshot |
| 数据量大、要筛选钻取 | HTML report、Notebook、dashboard、data app |
| 只是说明文档或规则源 | Markdown 真相源 |
| 生成或刷新持久 HTML lens / print view | HTML print view + ignored PDF + ignored PNG screenshot，默认自动生成并在对话中展示 PNG |
| 需要下载、打印或线下流转 | HTML print view + ignored PDF / PNG export |

### 2. 组装 source pack

按对象粒度读取最小必要源：

- 单文档：当前文档、frontmatter、出链 / 入链、相关入口、最近 log 或 report。
- 主题：主题入口、概念页、相关文章、相关报告、决策、log、raw / assets。
- 状态 / 验收 / issue：状态页、事项页、报告、issue、风险、服务台账或运行证据。
- 运行 / 代码事实：代码位置、日志、测试、artifact、服务状态和相关文档。

source pack 要标明：

- 已读来源。
- 未读但相关来源。
- 最新性或更新时间。
- 哪些结论来自证据，哪些只是推断。

Source pack 守卫：

- 状态 lens 至少读取状态源或当前项目 / 主题入口，不能只读历史报告。
- 计划 lens 必须读取目标、约束、依赖、时间窗或资源条件，不能只列 TODO。
- 决策 lens 必须读取候选、取舍维度、裁决入口和待确认项，不能把讨论过程写成最终决策。
- issue / 故障 lens 必须保留原始现象和影响范围，不能用根因候选改写事实。
- 验收 lens 必须读取关闭标准、最新证据、回归范围和人工确认边界，不能把局部通过写成完整通过。
- 知识 lens 必须读取上位主题、来源证据和适用边界，不能只做摘要。
- 资源 lens 必须验证位置、版本、用途、权限或归档入口，不能只在聊天里描述路径。
- owner lens 必须区分已确认、待确认和责任边界，不能让 agent 伪造人工确认。
- 时间线 lens 必须回到事件源和转折证据，不能把流水账当当前判断。
- 涉及现实世界会变化的事实，例如营业时间、价格、天气、政策、路线限制和排期，需要联网或现实核验；不能把旧 lens 当现状。

### 3. 建立背景框

每个 lens 都必须有背景框：

- **上位背景**：属于哪个项目、主题、概念、计划或事件。
- **来源背景**：读取了哪些文档，哪些只是邻接未读。
- **历史背景**：它是新结论、旧结论修正、阶段快照，还是历史证据。
- **关系背景**：它和哪些文档、owner、任务、风险、决策或资产相连。
- **使用边界**：当前结论适合用于什么判断，不适合上推到哪里。

### 3.1 标注证据边界

每个 lens 都必须把核心判断标成四级证据边界：

| 边界 | 含义 |
| --- | --- |
| `confirmed` | 已由源页面、记录、截图、票据、决策、人工确认、脚本检查或可靠数据支撑。 |
| `likely` | 证据较强，但缺少关键确认、最新核验或完整闭环。 |
| `possible` | 合理候选、解释或推断，不能写成当前结论。 |
| `blocked` | 缺少权限、现实核验、人工确认、数据快照或源页面，不能生成完整判断。 |

目标工程可以增加自己的证据边界，例如 `local`、`service-side`、`end-to-end`、`manual-confirmation` 或 `real-world-unverified`，但必须解释为什么可信、不能证明什么，以及不能上推到哪里。

### 4. 选择图文结构

按判断目的选择视觉结构：

| 目的 | 优先结构 |
| --- | --- |
| 一眼看状态 | 状态卡、看板、红黄绿矩阵 |
| 比较方案 / 版本 / 缺口 | 表格、评分矩阵、差异热力表 |
| 理解主题结构 | 脑图、树图、主题地图 |
| 理解系统或边界 | 框图、架构图、边界图 |
| 推进计划或排障 | 流程图、泳道图、行动地图 |
| 回看演进 | 时间线、里程碑图 |
| 看多文档关系 | 关系图、引用地图、证据链图 |
| 验收或关闭 | 证据层级表、缺口矩阵、不可上推边界 |

如果输出只剩长段文字，说明 lens 还没完成；继续把关系、结构、路径、比较和状态图形化。

### 4.1 按 lens 类型补必填字段

持久 lens 或复杂对话内 lens 必须按主 lens 类型补最小字段：

| lens_type | 必填字段 | 反模式 |
| --- | --- | --- |
| status | 当前态、阶段、阻塞、下一步、状态来源、更新时间、证据边界 | 用历史报告冒充当前态，隐藏未确认项 |
| plan | 目标、约束、依赖、可执行动作、blocked 条件、时间窗、资源 | 只列 TODO，把愿望写成安排 |
| decision | 候选方案、取舍维度、已确认、待确认、当前倾向、裁决入口 | 把讨论过程写成最终决策 |
| risk | 触发条件、影响对象、概率 / 影响、缓解动作、剩余风险、监控点 | 把未发生风险预建成 issue，省略剩余风险 |
| issue | 原始现象、影响范围、证据链、根因候选、验证边界、下一步 | 把候选根因写成 confirmed |
| acceptance | 验收对象、关闭标准、证据层级、缺口、人工确认边界、回归范围 | 把局部通过写成完整通过 |
| knowledge | 结论、来源、上位概念、邻接关系、适用边界、禁用场景 | 只写摘要，不建立来源和适用边界 |
| resource | 位置、版本、权限、用途、owner、归档入口、追溯入口 | 只在聊天里描述位置 |
| owner | owner、协同方、确认状态、责任边界、依赖对象、升级条件 | 让 agent 伪造人工确认 |
| timeline | 关键节点、转折点、状态变化、证据回链、未闭合影响 | 把流水账当当前判断 |

一个输入可以命中多个 lens，但必须先选主 lens，再把其他对象作为辅助层。不要用一个固定总览页回答所有问题。

### 4.2 用户价值优先

问题聚焦式呈现面向用户，而不是面向系统维护者。首屏必须先回答“我现在该看什么 / 能做什么 / 不能上推什么”。

- 首屏优先：当前判断、关键风险、下一步、可执行 / 条件性 / 禁止上推、资源位置和最重要证据。
- 维护信息下沉：`lens_id`、`source_revision`、`output_mode`、`export_profile`、`print_profile`、`equivalence_profile`、`canonical_policy`、`snapshot_policy`、`staleness_policy`、`refresh_trigger` 等字段必须保留，但默认放在底部、折叠区、脚注或 registry。
- 不把 metadata 表当作内容主体；metadata 只证明 lens 如何生成和维护，不回答用户当前要判断什么。
- 如果用户反馈“看不出价值”，先检查是否把维护字段放到了主体区域，或是否缺少一眼判断。

### 4.3 照片和视觉证据排版

照片密集型 lens 必须先服务用户扫读和判断，不按上传顺序机械平铺。

- 先按用户扫读路径、内容类型、信息价值、行动用途和画幅家族重排照片；上传顺序只作为证据编号。
- 证据照片、判断卡、行动卡、风险边界和维护信息要分层，不混成同一类卡片。
- 混合横图、竖图和近似方图时，显式选择排版体系：横图标准证据网格、竖图专题行 / 专题列、主图 + 辅图、图文配对、证据表 + 图集、masonry 或 dense mosaic。
- 同画幅横图优先使用自然比例证据网格；不要把 16:9 横图放进固定高度格子造成内部大留白。
- 证据照片默认不裁剪，HTML / print view 默认使用 `object-fit: contain`；只有非证据性封面、装饰图或用户明确要求时才可裁剪。
- 竖图可以跨 2 到 3 行；相邻区域用横图、同组照片或高价值判断卡补位。
- 判断卡只承接用户要看的结论、风险、边界或下一步，不写排版设计说明。
- 打印 / PDF 视图要保留同一排版语义，不能在导出时退化成混乱列表。

### 5. 输出 lens

默认输出顺序：

```markdown
**一眼判断**
- 当前结论：
- 下一步 / 当前动作：
- 风险或缺口：

**背景框**
- 上位背景：
- 来源背景：
- 历史背景：
- 关系背景：
- 使用边界：

**图文主体**
- 表格 / 脑图 / 框图 / 流程图 / 时间线 / 关系图 / 状态卡：

**证据边界**
- confirmed：
- likely：
- possible：
- blocked：

**证据与追溯**
- 已读来源：
- 关键证据：
- 原始入口：

**导出、打印与对话预览**
- 导出需求：
- 页面规格：
- 分页策略：
- PDF / snapshot 边界：
- PDF 路径：
- PNG 预览路径：
- 对话中是否已展示 PNG：

**未覆盖边界**
- 未读来源：
- 不能上推：
- 需要人工确认：
```

聊天内可优先用 Markdown 表格和 Mermaid。持久呈现时优先生成 HTML；需要复杂图形时配套 assets。

持久 lens 至少包含这些 provenance 字段：

- `lens_id`
- `focus_object`
- `lens_type`
- `judgement_purpose`
- `source_pages`
- `source_scope`
- `generated_at`
- `source_revision`
- `evidence_boundary`
- `context_frame`
- `output_mode`
- `visual_structure`
- `photo_layout_strategy`，仅照片密集型必填
- `export_profile`
- `print_profile`
- `equivalence_profile`
- `default_auto_exports`
- `conversation_png_preview`
- `canonical_policy`
- `snapshot_policy`
- `staleness_policy`
- `refresh_trigger`

snapshot 额外包含 `snapshot_of`；current lens 不应把 `snapshot_of` 写成当前事实来源。

### 5.1 导出与打印设计

如果用户要求 HTML、下载、PDF、打印、A4 / A3、横排或竖排，设计阶段就必须写清 `export_profile`。如果本轮生成或刷新持久 HTML lens / print view，即使用户没有单独要求 PDF / PNG，也必须默认自动生成同源 PDF 导出和 PNG 截图 / 长图导出：

| 字段 | 说明 |
| --- | --- |
| page_size | A4 / A3 / Letter / custom |
| orientation | portrait / landscape；默认按内容判断，不强制 |
| margins | print margins，默认留出装订和批注空间 |
| print_mode | current export / snapshot export / handout / appendix |
| pagination | 关键图表是否允许跨页、表格如何分页、页眉页脚是否重复 |
| assets_policy | 只允许提交源级支持资产；PDF / PNG / SVG 预览和下载件放 gitignore 导出目录 |
| provenance_policy | 来源、生成时间、证据边界放在页脚、封底或附录 |
| equivalence_policy | HTML / PDF / PNG / slide 的信息、结论、证据边界和版式语义如何保持一致 |
| default_auto_exports | 本轮是否默认自动生成 PDF / PNG，生成命令或工具是什么 |
| conversation_png_preview | 最终回复是否展示 PNG 预览，无法展示时的阻塞原因 |

HTML 视图要优先支持 `@media print` 和 `@page`，让同一份页面可以导出 PDF。设计时避免只适合屏幕滚动的结构：

- 关键卡片、矩阵、图表和证据表不要被分页切断。
- 长表格要有重复表头和可读的分页。
- A4 适合报告、验收、单文档 lens；A3 适合架构图、主题地图、关系图、时间线和大矩阵。
- 横排适合矩阵、流程图、时间线和架构图；竖排适合报告、清单、证据包和阅读型材料。
- 打印版要保留来源、更新时间、lens id、证据边界和未覆盖边界，不能只留下漂亮图。
- PDF / PNG / slide 不应重新排一套内容；必须由同一 HTML / source / manifest 生成，保持信息和版式语义一致。
- 禁止为对话展示单独手工重画 PNG；除非它来自同一 source manifest / render pipeline（same source manifest / render pipeline），并在 `equivalence_profile` 中说明一致性边界。

导出 PDF / PNG 时优先从 HTML / print CSS 生成；可用浏览器打印、Playwright / Chromium、系统 print-to-PDF / screenshot 或项目既有导出工具。没有实际生成和检查导出件时，不要声称“已导出”，只能说明已具备导出配置或待执行导出。生成持久 HTML lens 后，最终回复必须用 Markdown 图片语法展示 PNG 预览，例如 `![lens preview](/absolute/path/to/preview.png)`；如果环境限制导致图片无法渲染，也要给出 PNG 绝对路径。

存储规则：

- `views/current/` 默认只提交 canonical HTML / source / manifest，不提交同名 PDF、PNG、SVG。
- `views/snapshots/` 默认只提交 snapshot HTML / manifest / source_revision；PDF 只是可再生成的 snapshot export，除非用户明确要求归档外部分发件。
- `views/exports/`、`views/.exports/`、`views/**/.exports/`、`assets/views/` 或目标工程等价目录必须被 `.gitignore` 忽略，用于放 PDF / PNG / SVG 下载缓存。
- `assets/` 只放源级支持材料、真实证据截图、原始图片或不可再生附件；不要把由 HTML lens 生成的 PNG 预览放进可提交 assets。

### 6. 持久化判断

只有满足以下条件之一，才写入持久文件：

- 用户明确要求生成或更新 HTML / 图文文件；一旦生成持久 HTML，同轮必须生成 ignored PDF 和 ignored PNG 预览，并在对话中展示 PNG。
- 用户明确要求可下载、可打印、PDF / PNG、A4 / A3、横排 / 竖排或对外分发；这只触发导出配置或 ignored export，不等于把导出件提交进仓库。
- 当前主题已稳定，适合成为 canonical current lens。
- 本轮形成决策、验收、发布、事故、阶段复盘或外部分发 snapshot。
- 当前仓库已有 `views/` / `artifacts` / `reports` 等明确呈现层。

没有明确呈现层时，先在最终回复里给图文 lens，并说明建议落位，不静默新建目录。

如果目标工程已有持久呈现层，新增或刷新持久 lens 后必须同步 registry 或等价索引；如果目标工程没有 registry，只在当前回答中说明建议建立的最小字段，不硬套 AcknowledgeBase 的目录名。

## 自检

- 是否先回答“用户现在要看什么”，而不是机械摘要全文。
- 是否选定主 `focus_object` 和 `lens_type`，没有用固定总览页回答所有问题。
- 是否覆盖单文档或跨文档主题的背景框。
- 是否按 `confirmed / likely / possible / blocked` 或目标工程等价边界标注核心判断。
- 是否有至少一种视觉结构承载核心关系、路径、状态或比较。
- 是否把首屏留给用户价值，而不是让 metadata 抢占主体。
- 如果有照片或视觉证据，是否声明 `photo_layout_strategy`，保留证据细节且避免无意义固定高度网格。
- 如果是复杂或持久 lens，是否按 lens 类型补齐必填字段和反模式检查。
- 是否写清 source pack、更新时间、未读来源和证据边界。
- 是否避免把历史快照当 current。
- 是否避免把图文 lens 当正式验收、关闭、准出或规则裁决。
- 如果生成或更新持久 lens，是否包含 `lens_id`、`focus_object`、`lens_type`、`judgement_purpose`、`source_pages`、`generated_at`、`evidence_boundary`、`context_frame`、`output_mode`、`export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports`、`conversation_png_preview`、`canonical_policy`、`snapshot_policy`、`staleness_policy` 和 `refresh_trigger`。
- 如果生成或更新持久 HTML lens，是否在设计阶段声明 page size、orientation、margins、pagination、print CSS、PDF / PNG 生成方式和 snapshot 边界。
- 如果生成或更新持久 HTML lens，是否实际导出 PDF 和 PNG 截图 / 长图，检查页数、分页、图表裁切、链接 / 来源和打印可读性，并在最终回复中展示 PNG。
- 是否确认 HTML / PDF / PNG / slide 来自同一源，信息、结论、证据边界和版式语义一致。
- 是否确认没有为对话预览另画一张与 canonical HTML / source / manifest 不同源的 PNG。
- 是否确认导出件在 gitignore 忽略目录或运行时下载中，没有把同一 lens 的 PDF / PNG / SVG 作为重复渲染物提交。
- 如果生成文件，是否遵守当前仓库目录规范并补入口 / 回链 / 检查。

## 相关页面

- [[concepts/problem-focused-information-presentation]]
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]
- [[concepts/ai-era-information-presentation]]
- [[response-mode-routing]]
- [[knowledge-linking-rules]]
