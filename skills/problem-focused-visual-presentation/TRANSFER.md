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
- **已抽象反哺到上游源能力**：已吸收关注对象和 lens 类型、证据边界、source pack 守卫、首屏用户价值优先、照片证据排版、持久 lens provenance、current / snapshot、registry 和 sensor 检查口径。
- **未吸收内容**：LifeOS 的项目事实、搬家场景、生活领域页、现场照片路径、日志、current lens 实例和本地项目状态。
- **迁移时使用口径**：目标工程只读取 AcknowledgeBase 源资料；LifeOS 仅作为已反哺的历史来源，不作为目标工程直接复制源。

## 可以吸收

- 触发条件：信息乱、阅读不方便、一图胜千言、图文混排、HTML 呈现、看文档或看主题。
- 工作流：关注合同、主 `focus_object` / `lens_type` 判定、source pack、source pack 守卫、背景框、证据边界、图文结构选择、证据追溯、持久化判断。
- 输出格式：一眼判断、背景框、图文主体、`confirmed / likely / possible / blocked` 证据边界、证据与追溯、未覆盖边界。
- 视觉类型：表格、脑图、框图、流程图、关系图、时间线、状态卡、证据链图。
- lens 类型字段：status、plan、decision、risk、issue、acceptance、knowledge、resource、owner、timeline 的必填字段、反模式和验证点。
- 用户价值优先：首屏先呈现当前判断、关键风险、下一步、可执行 / 条件性 / 禁止上推和最重要证据；维护字段下沉。
- 照片 / 视觉证据排版：画幅家族、自然比例证据网格、竖图专题、`object-fit: contain`、不裁切证据图、判断卡不写排版说明。
- 导出能力：HTML print view、PDF / PNG export、A4 / A3 / custom 页面规格、横竖版选择、分页策略、页眉页脚、证据边界、同源一致性和 snapshot 规则。
- 持久化字段：`lens_id`、`focus_object`、`lens_type`、`source_pages`、`source_scope`、`generated_at`、`source_revision`、`evidence_boundary`、`context_frame`、`output_mode`、`visual_structure`、`photo_layout_strategy`、`export_profile`、`print_profile`、`equivalence_profile`、`canonical_policy`、`snapshot_policy`、`staleness_policy`、`refresh_trigger`。
- 工程化保护：持久 lens 的 registry / 等价索引、模板字段和 sensor 检查口径。
- 回写守卫：不把 lens 当第二份真相源，不替代验收 / 关闭 / 准出。

## 只能抽象吸收

- AcknowledgeBase 的 `articles/`、`concepts/`、`skills/`、`views/` 命名方式。
- 本库的 `[[wikilink]]`、`log.md` 和 sensor 结构。
- Life、DocCustomeranalysis、prefect、fetch-adapter、DocFilmCommunity 这些样本事实。
- LifeOS 的 `rules/`、`views/current/`、`views/snapshots/`、`templates/lens.md` 和 `automation/scripts/check_problem_focused_lens.py` 结构，只能作为目标工程自适配参考，不要求照搬。

## 禁止复制

- 不复制本库具体项目状态、工程路径、服务实例、报告结论、issue 编号或一次性对话记录。
- 不复制 LifeOS 的搬家、生活事项、现场照片、日志、项目状态、视图实例或本地检查结果。
- 不把目标工程不存在的 `views/` 目录硬套进去。
- 不把 HTML 当唯一输出形式；目标工程可按工具栈选择 Mermaid、SVG、Canvas、PDF、slides 或 dashboard。
- 不把 PDF 当真相源；PDF 只能是导出、打印、分发或 snapshot 产物，必须能回到源 lens 和证据。
- 不把同一 lens 的 HTML、PDF、PNG、SVG 同步提交到仓库；PDF / PNG / SVG 下载件应进入 gitignore 忽略目录或由运行时生成。
- 不让不同导出形态各自维护内容；HTML / PDF / PNG / slide 必须同源同版，信息、结论、证据边界和版式语义一致。

## 目标工程落地模块

1. 在目标工程技能层新增等价 skill，写明触发条件、工作流、输出格式和禁止项。
2. 补 `focus_object` / `lens_type` 判定、证据边界、source pack 守卫、lens 类型字段、首屏用户价值优先和照片证据排版守卫。
3. 在目标工程 agent 入口规则中加入轻量触发：用户要直观看文档 / 主题 / 状态时，调用该 skill。
4. 在响应模式或 workflow 中加入“图文呈现”模式，说明默认读取、默认写入和持久化边界。
5. 如果目标工程有专题目录或视图目录，建立 current / snapshot / exports 或等价呈现层；`exports` 必须被 gitignore 忽略，没有则先只输出聊天图文 lens。
6. 如果目标工程需要持久 lens，补模板或等价字段清单；如果高频使用，再补 sensor。
7. 补入口链接，让用户能从技能目录或专题目录找到该能力。

## 验证要求

- 用一份单文档样本验证：输出必须包含一眼判断、背景框、图文主体和追溯入口。
- 用一个跨多文档主题验证：输出必须呈现材料分层、关系 / 冲突 / 时间线或证据链。
- 用一个状态 / issue / 验收样本验证：输出必须标清主 `lens_type`、证据边界、不能上推范围和最新 source pack。
- 如果目标工程有照片或视觉证据，用一个混合横竖图样本验证：必须保留证据细节，声明 `photo_layout_strategy`，避免裁切和固定高度大留白。
- 用一个 HTML 导出样本验证：输出必须声明 A4 / A3 或 custom、横竖版、边距、分页策略、忽略目录和同源一致性，并在实际导出 PDF / PNG 时检查图表裁切、页数、页脚来源、打印可读性以及 HTML / PDF / PNG 信息一致性。
- 如果目标工程建立持久 lens 模板或 registry，检查 provenance 字段、current / snapshot 和 staleness / refresh 规则齐全。
- 检查 Git diff 没有新增同一 lens 的重复 PDF / PNG / SVG 渲染物。
- 检查最终结果没有把历史快照当 current，没有把 lens 当验收或关闭结论。
- 跑目标工程既有检查，并提交同一主题改动。
