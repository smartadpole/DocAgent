# Component Semantic Manifest

本页定义问题聚焦式 lens 的组件语义。组件名称用于模板、HTML meta 和 sensor 检查，不承接具体事实。

## 组件角色

每个组件在 HTML manifest 中至少声明 `semantic_role`、`visual_weight` 和 `export_fallback`，用于说明它在页面里的判断职责、视觉权重和导出失败时的降级呈现。

- `verdict-strip`：首屏一眼判断，必须回答当前读者要判断什么。
- `context-frame`：上位背景、来源背景、历史背景、关系背景和使用边界。
- `source-pack-rail`：已读来源、未读但相关来源、更新时间和 source revision。
- `evidence-boundary`：confirmed / likely / possible / blocked 四级边界。
- `trace-link`：回到 owner 页面、source page、report、issue、decision、memory、trace 或 registry。
- `matrix-cell`：用整格状态表达矩阵判断，长说明下沉到证据区。
- `timeline-node`：事件、版本、阶段或状态变化节点。
- `relation-edge`：关系图中的引用、冲突、依赖、包含、替代或待确认关系。
- `concept-cluster`：知识 / 概念 lens 的主题簇。
- `boundary-block`：可证明范围、不可上推范围、权限或数据边界。
- `action-router`：把发现分流到 issue、risk、decision、report、memory、trace、skill、template、sensor 或 owner 页面。
- `export-badge`：HTML / PDF / PNG 是否同源导出以及导出文件是否在忽略目录。
- `static-qa-block`：layout、type、spacing、palette、component、accessibility、export、rubric 和 review artifact 留痕。

## 组合规则

- 持久 HTML 至少包含 `verdict-strip`、`context-frame`、`source-pack-rail`、`evidence-boundary`、`trace-link`、`export-badge` 和 `static-qa-block`。
- 状态 / issue / 验收 lens 必须包含 `boundary-block`。
- 矩阵 lens 必须包含 `matrix-cell`，并让状态色覆盖整格。
- 知识 lens 必须包含 `concept-cluster` 或 `relation-edge`。
- 时间线 lens 必须包含 `timeline-node`。
- 发现行动项时必须出现 `action-router`，但行动项不能停留在 lens 目录形成平行看板。
