# 问题聚焦式图文呈现迁移清单

## 能力目标

让目标工程的 agent 在面对复杂文档、跨文档主题、项目状态、风险、决策、计划、验收或知识材料时，能自动生成带背景框、证据边界、可视结构和导出配置的图文 lens，而不是只输出长文字摘要。

## 源资料路径

- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/problem-focused-visual-presentation/SKILL.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/templates/problem-focused-lens-template.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/problem-focused-information-presentation.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/ai-era-information-presentation.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/response-mode-routing.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/scripts/check_problem_focused_visual_presentation.py`

## 上游归一状态

- **来源工程 / 来源技能**：LifeOS 的 `/Users/hai/Documents/Life/rules/problem-focused-lens.md`、`/Users/hai/Documents/Life/.codex/skills/problem-focused-lens/SKILL.md`、`/Users/hai/Documents/Life/templates/lens.md` 和 `automation/scripts/check_problem_focused_lens.py`。
- **已抽象反哺到上游源能力**：已吸收关注对象和 lens 类型、证据边界、source pack 守卫、首屏用户价值优先、照片证据排版、矩阵主对象不可被摘要 / 折叠替代、同矩阵不重复渲染、标签必须有区分力、矩阵密度质量、持久 lens provenance、`views/` 落位硬合同、current / snapshot、HTML lens 的 PDF / PNG ignored export 与对话 PNG 预览完成合同、registry 和 sensor 检查口径。
- **未吸收内容**：LifeOS 的项目事实、搬家场景、生活领域页、现场照片路径、日志、current lens 实例和本地项目状态。
- **迁移时使用口径**：目标工程只读取 AcknowledgeBase 源资料；LifeOS 仅作为已反哺的历史来源，不作为目标工程直接复制源。

## 可以吸收

- 触发条件：信息乱、阅读不方便、一图胜千言、图文混排、HTML 呈现、看文档或看主题。
- 工作流：关注合同、主 `focus_object` / `lens_type` 判定、source pack、source pack 守卫、背景框、证据边界、图文结构选择、证据追溯、持久化判断。
- 判断目的：看懂、比较、行动、验收、追责、回顾、学习、沉淀；不要把所有判断压成“拍板”或“复盘”。
- 输出形态选择：短答、Markdown 真相源、图文 lens、HTML report、print view、export config、snapshot；先按当前问题选最低噪声形态，不默认 HTML 化。
- 输出格式：一眼判断、背景框、图文主体、`confirmed / likely / possible / blocked` 证据边界、证据与追溯、未覆盖边界。
- 视觉类型：表格、脑图、框图、流程图、关系图、时间线、状态卡、证据链图。
- 矩阵 / 热力图视觉编码：行列交叉状态矩阵优先作为概览前置；状态单元格优先整格填色，不用白底胶囊承担主视觉；状态之间要有明显色相 / 明度 / 饱和度差异，文字与背景保持强对比；具体证据和长说明下沉到详情卡、脚注或追溯区；当矩阵是主对象时，不用摘要卡、优先子集或折叠区替代它，不重复渲染同一矩阵，只有能产生区分的标签才进入行 / 单元格。
- lens 类型字段：status、plan、decision、risk、issue、acceptance、knowledge、resource、owner、timeline 的必填字段、反模式和验证点。
- 用户价值优先：首屏先呈现当前判断、关键风险、下一步、可执行 / 条件性 / 禁止上推和最重要证据；维护字段下沉。
- 照片 / 视觉证据排版：画幅家族、自然比例证据网格、竖图专题、`object-fit: contain`、不裁切证据图、判断卡不写排版说明。
- 导出能力：HTML print view、PDF / PNG export、A4 / A3 / custom 页面规格、横竖版选择、分页策略、页眉页脚、证据边界、同源一致性和 snapshot 规则。
- `views/` 落位硬合同：迁移后的目标工程只要生成或更新持久 HTML lens / print view，canonical HTML / source / manifest 必须落到目标工程的 `views/current/` 或 `views/snapshots/`，并同步 `views/lens-registry.md` 或等价 registry；不能落在仓库根目录、临时目录、handoff 目录或只留在聊天里。
- HTML lens 硬完成合同：只要本轮生成或更新持久 HTML lens，就必须同轮实际生成同源 PDF 和至少一张 PNG 截图 / 长图到 gitignore 忽略目录，并在最终回复用 Markdown 图片语法展示 PNG；只给 HTML 链接、HTML 代码块或“具备导出配置”不算完成。
- 同源一致性：PDF / PNG / SVG / slide 必须来自 canonical HTML 或同一 source manifest / render pipeline；禁止为对话展示单独手工重画 PNG。
- 持久化字段：`lens_id`、`focus_object`、`lens_type`、`judgement_purpose`、`source_pages`、`source_scope`、`generated_at`、`source_revision`、`evidence_boundary`、`context_frame`、`output_mode`、`visual_structure`、`photo_layout_strategy`、`export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports`、`conversation_png_preview`、`canonical_policy`、`snapshot_policy`、`staleness_policy`、`refresh_trigger`。
- 工程化保护：持久 lens 的 registry / 等价索引、模板字段和 sensor 检查口径。
- 回写守卫：不把 lens 当第二份真相源，不替代验收 / 关闭 / 准出。

## 只能抽象吸收

- AcknowledgeBase 的 `articles/`、`concepts/`、`skills/`、`views/` 命名方式。
- 本库的 `[[wikilink]]`、`log.md` 和 sensor 结构。
- Life、DocCustomeranalysis、prefect、fetch-adapter、DocFilmCommunity 这些样本事实。
- LifeOS 的 `rules/`、`templates/lens.md` 和 `automation/scripts/check_problem_focused_lens.py` 结构只能作为目标工程自适配参考，不要求照搬；但 `views/current/`、`views/snapshots/`、ignored exports 和 registry 所代表的持久呈现职责必须在目标工程建立等价层。

## 禁止复制

- 不复制本库具体项目状态、工程路径、服务实例、报告结论、issue 编号或一次性对话记录。
- 不复制 LifeOS 的搬家、生活事项、现场照片、日志、项目状态、视图实例或本地检查结果。
- 不照搬 AcknowledgeBase / LifeOS 的业务路径、实例和页面命名；但迁移问题聚焦技能时，目标工程必须建立或绑定自己的 `views/` 持久呈现层，不能把持久 HTML lens 改落到 handoff、临时目录或聊天输出。
- 不把 HTML 当唯一输出形式；目标工程可按工具栈选择 Mermaid、SVG、Canvas、PDF、slides 或 dashboard。
- 不把 PDF 当真相源；PDF 只能是导出、打印、分发或 snapshot 产物，必须能回到源 lens 和证据。
- 不把同一 lens 的 HTML、PDF、PNG、SVG 同步提交到仓库；PDF / PNG / SVG 下载件应进入 gitignore 忽略目录或由运行时生成。
- 不让不同导出形态各自维护内容；HTML / PDF / PNG / slide 必须同源同版，信息、结论、证据边界和版式语义一致。

## 目标工程落地模块

1. 在目标工程技能层新增等价 skill，写明触发条件、工作流、输出格式和禁止项。
2. 补 `focus_object` / `lens_type` 判定、证据边界、source pack 守卫、lens 类型字段、首屏用户价值优先和照片证据排版守卫。
3. 补矩阵 / 热力图视觉编码守卫：当 lens 使用状态矩阵、成熟度矩阵、缺口矩阵或验证矩阵时，默认前置概览矩阵，单元格整格填色，状态差异和文字 / 背景对比足够强，长说明下沉到详情；如果矩阵是主对象，不能被摘要、折叠或重复矩阵稀释，标签必须有区分力，行高和列宽要服务扫读密度。
4. 在目标工程 agent 入口规则中加入轻量触发：用户要直观看文档 / 主题 / 状态时，调用该 skill。
5. 在响应模式或 workflow 中加入“图文呈现”模式，说明默认读取、默认写入和持久化边界。
6. 建立或确认目标工程的 `views/` 持久呈现层：至少包含 `views/README.md`、`views/current/`、`views/snapshots/`、`views/lens-registry.md` 或等价 registry；PDF / PNG / SVG 导出缓存必须进入 gitignore 忽略的 `views/.exports/`、`views/exports/`、`views/**/.exports/` 或等价目录。
7. 补模板或等价字段清单；其中 HTML lens 必须把 `views/` 落位、`default_auto_exports`、`conversation_png_preview`、ignored export 目录和“未实际导出或展示的阻塞声明”写成硬完成合同，而不是只作为可选字段。
8. 补入口链接，让用户能从技能目录或专题目录找到该能力。

## LifeOS 对照覆盖矩阵

| LifeOS 来源模块 | 本库吸收位置 | 覆盖重点 |
| --- | --- | --- |
| `rules/problem-focused-lens.md` | `skills/problem-focused-visual-presentation/SKILL.md`、`TRANSFER.md` | 触发、关注对象、判断目的、输出形态、source pack、证据边界、图文结构、导出 / 打印、current / snapshot。 |
| `.codex/skills/problem-focused-lens/SKILL.md` | `skills/problem-focused-visual-presentation/SKILL.md` | agent 工作流、低噪声输出选择、照片布局、HTML 导出完成合同、禁止项。 |
| `templates/lens.md` | `templates/problem-focused-lens-template.md` | provenance 字段、`default_auto_exports`、`conversation_png_preview`、refresh / staleness / snapshot 字段。 |
| `views/lens-registry.md` | `views/lens-registry.md` | current / snapshot registry 字段、source revision、输出 / 导出 / 刷新策略。 |
| `automation/scripts/check_problem_focused_lens.py` | `scripts/check_problem_focused_visual_presentation.py` | 必要术语、registry 字段、HTML export profile、照片布局 guard、禁止追踪派生 PDF / PNG / SVG。 |

## 验证要求

- 用一份单文档样本验证：输出必须包含一眼判断、背景框、图文主体和追溯入口。
- 用一个跨多文档主题验证：输出必须呈现材料分层、关系 / 冲突 / 时间线或证据链。
- 用一个状态 / issue / 验收样本验证：输出必须标清主 `lens_type`、证据边界、不能上推范围和最新 source pack。
- 用一个矩阵样本验证：如果核心判断来自行列交叉状态，矩阵必须作为概览前置；状态格子应整格填色并形成足够强的状态差异和文字 / 背景对比，长说明不得塞进矩阵格子；检查主矩阵没有被摘要 / 折叠替代，没有重复渲染同一矩阵，没有对全量同类行重复无区分标签，并且版式密度足够支撑扫读。
- 如果目标工程有照片或视觉证据，用一个混合横竖图样本验证：必须保留证据细节，声明 `photo_layout_strategy`，避免裁切和固定高度大留白。
- 用一个 HTML 导出样本验证：输出必须声明 A4 / A3 或 custom、横竖版、边距、分页策略、忽略目录和同源一致性；如果本轮生成或更新持久 HTML lens，必须实际导出 PDF / PNG、检查图表裁切、页数、页脚来源、打印可读性以及 HTML / PDF / PNG 信息一致性，并在最终回复展示 PNG 预览。只返回 HTML 链接或 HTML 代码块判定为不合格。
- 如果目标工程建立持久 lens 模板或 registry，检查 provenance 字段、current / snapshot 和 staleness / refresh 规则齐全。
- 检查目标工程生成或更新的持久 HTML lens 是否落在 `views/current/` 或 `views/snapshots/`，并更新 `views/lens-registry.md` 或等价 registry；落在仓库根目录、handoff、临时目录或聊天代码块判定为不合格。
- 如果目标工程已有 HTML current lens，检查其 `@page`、`@media print`、`output_mode`、`export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports`、`conversation_png_preview` 和 same source pack / manifest 语义。
- 检查 Git diff 没有新增同一 lens 的重复 PDF / PNG / SVG 渲染物。
- 检查最终结果没有把历史快照当 current，没有把 lens 当验收或关闭结论。
- 跑目标工程既有检查，并提交同一主题改动。
