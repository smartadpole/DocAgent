# Visual Finish Rubric

本页给问题聚焦式 lens 做人工完成度判断。sensor 只能检查字段和留痕，不能替代人审或视觉模型判断美感。

## 等级

字段锚点：`finish_grade`、`rendered_visual_review`、`visual_acceptance_result`。

- `draft`：source pack 和证据边界存在，但视觉主角弱，适合内部草稿。
- `usable`：首屏能回答问题，主视觉和追溯入口清楚，PDF / PNG 导出可用。
- `polished`：视觉主角强，信息层级清晰，组件语义稳定，导出分页和截图裁切通过。
- `blocked`：缺少关键来源、导出失败、证据边界不清或 owner 回写未分流。

## Gate

- `visual_strength_gate`：是否有一个明确视觉主角，而不是标题 + 卡片 + 表格。
- `hierarchy_amplitude_gate`：首屏、主图、证据和追溯是否有足够层级差。
- `component_variety_gate`：组件是否服务语义，不是同一种卡片复制。
- `color_budget_single_hero_gate`：是否只有一个主色 / 主视觉承担注意力，语义色不互相抢戏。
- `export_render_check`：PDF、PNG、print view 是否来自同源 HTML 或同一 source manifest。
- `accessibility_checks`：标题顺序、对比度、alt / aria、移动端溢出和打印分页是否至少自检。

## 人审问题

1. 首屏不用读完整文，能否知道这张 lens 在回答什么？
2. 视觉主角能否表达结构，而不是只做装饰？
3. confirmed / likely / possible / blocked 是否能一眼区分？
4. 长说明是否下沉，矩阵格是否整格表达状态？
5. PDF / PNG 是否来自同源 HTML，且没有裁切关键信息？
6. lens 是否清楚说明它不能替代哪些 owner 页面？

## Anti-Goodhart

- 字段齐全不等于视觉完成。
- 文件存在不等于导出验证。
- 截图好看不等于事实 confirmed。
- 传感器通过不等于人审通过。
