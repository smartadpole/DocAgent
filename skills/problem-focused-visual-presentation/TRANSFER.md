# Problem-Focused Visual Presentation Transfer

## 能力目标

让目标工程具备把复杂文档、主题、状态、风险、计划、验收、issue、知识或证据链转成问题聚焦图文 lens 的能力，并守住来源、证据边界、持久化、同源导出和回写边界。

## 可以吸收

- 统一入口：`problem-focused-visual-presentation` 是总入口，HTML、PDF、PNG、print view、current、snapshot 都是内部输出形态。
- 关注合同：`focus_object`、`lens_type`、`judgement_purpose`、`source_pack`、`evidence_boundary`、`output_mode`、`persistent_or_temporary`、`export_required`。
- source pack：已读、未读、更新时间、证据和推断。
- 背景框：上位、来源、历史、关系、使用边界。
- 证据边界：confirmed、likely、possible、blocked。
- lens 类型：status、plan、decision、risk、issue、acceptance、knowledge、resource、owner、timeline。
- 视觉流水线：`Source truth -> Content contract -> Visual strategy -> Page paradigm / slot schema -> Component semantic manifest -> Renderer implementation -> Export / accessibility / regression QA -> Human rubric`。
- 视觉策略字段：`art_direction_brief`、`information_topology`、`layout_morphology_plan`、`topic_visual_language`、`primary_visual_metaphor`、`theme_specific_elements`、`anti_information_listing_strategy`、`page_paradigm`、`component_semantic_manifest`、`human_rubric`、`result_cluster_diagnosis`。
- 静态视觉 QA 字段：`layout_frame`、`type_scale`、`spacing_rhythm`、`semantic_palette`、`component_roles`、`accessibility_checks`、`export_render_check`、`finish_grade`、`visual_strength_gate`、`hierarchy_amplitude_gate`、`component_variety_gate`、`color_budget_single_hero_gate`、`adjustment_loop`、`rendered_visual_review`、`review_artifact`、`visual_acceptance_result`。
- 图文结构选择：状态卡、矩阵、时间线、关系图、证据链、行动地图、概念图、边界图。
- visual_acceptance_floor：复杂或持久 lens 若声明 decision-lens / polished / full-page，最低必须达到 `impact-required`；只做到信息正确、字段齐全或卡片整齐时只能标为 usable / draft。
- 证据图片和截图默认 `object-fit: contain` 或等价不裁切策略，除非 source pack 明确允许裁切；裁切证据细节会降低证据可信度。
- 持久化守卫：canonical HTML / source、`views/current/`、`views/snapshots/`、snapshot、ignored exports、导出一致性、同源一致性、[[views/lens-registry]] 或等价 registry。
- sensor：检查入口、模板字段、HTML meta、`static_visual_qa`、导出缓存忽略规则和 registry 接线。

## 只能抽象吸收

- 源工程的 `skills/`、`views/`、`concepts/`、导出目录、registry、lens 字段和 CSS 只能作为参考。
- 目标工程已有报告、dashboard、artifact、docs site 或等价呈现层时，应映射到既有呈现层。
- 没有持久视图需求时，只迁移聊天内 lens 方法，不强行建 `views/`；一旦目标工程要生成持久 lens，必须建立或绑定等价 current / snapshot / registry / ignored exports。
- `[[wikilink]]`、检查脚本结构和样例路径只吸收为本工程可读的入口关系，不复制源工程路径事实。

## 禁止复制

- 不复制源工程具体 HTML、矩阵数据、项目状态、路径、排行、source revision、图片路径、运行 ID、log、截图或一次性对话记录。
- 不把 PDF / PNG / slide 写成第二份事实源。
- 不把图文呈现替代验收、关闭、准出、决策、issue 裁决或人工确认。
- 不为了聊天预览另画一张不同源 PNG；PNG / PDF 必须来自同一 source manifest 或 render pipeline。

## 目标工程结构自检

迁移前检查：

1. 是否已有 `views/`、`reports/`、dashboard、artifact、docs site 或等价呈现层。
2. 是否已有导出目录和 `.gitignore` 规则。
3. 是否需要 current / snapshot / temporary 三类视图。
4. 是否有 source manifest、registry、render pipeline 或截图 / PDF 工具。
5. 如果没有持久需求，只建立技能，不新增呈现目录。

## 验证要求

- 用单文档样本验证一眼判断、背景框、图文主体和追溯入口。
- 用跨文档主题样本验证材料分层、关系 / 冲突 / 时间线或证据链。
- 用状态 / issue / 验收样本验证 lens 类型、证据边界、不能上推范围和最新 source pack。
- 用知识 / 概念样本验证概念图、脑图、关系图或分层地图优先。
- 用矩阵样本验证前置概览、状态格整格填色和长说明下沉。
- 若生成持久 HTML，实际导出 PDF / PNG，检查裁切、分页、来源、边界和同源一致性，并确保导出件不会作为重复事实源提交。
- 最终回复写清呈现落位、来源、导出状态、检查结果、PNG 预览路径和未覆盖边界。
