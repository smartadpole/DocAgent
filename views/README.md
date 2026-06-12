# 图文呈现层

`views/` 用于存放问题聚焦式 HTML lens。它只负责呈现，不替代 `articles/`、`concepts/`、`projects/`、`log.md` 等 Markdown 真相源。

## 目录

- `current/`：当前可反复打开的 canonical lens。
- `snapshots/`：验收、决策、发布、事故、阶段复盘、外部分发或审计证据需要冻结时使用。
- `lens-registry.md`：lens id、关注对象、来源和失效条件索引。
- `exports/`、`.exports/`、`**/.exports/`：PDF / PNG / SVG 等派生导出缓存，已由 `.gitignore` 忽略，不作为可提交真相源。

## 当前视图

- [[views/current/knowledge/xinzhi-ruisheng-company.html]]：芯智睿声企业调研 lens。
- [[views/current/knowledge/codex-goal-public-guide.html]]：可对外发布的 Codex Goal 使用教程一页式 lens，突出 “Goal = 目标 + 证据 + 停止条件”。
- [[views/current/governance/skill-maturity-matrix.html]]：跨工程技能与治理能力成熟度矩阵，动态发现所有工程的技能项，按调研、复盘、文档维护、项目上下文等主题归并成大项，并按通用 / 可迁移能力与项目 / 领域绑定能力分表呈现，同时标注源头工程、底层子项、发现工程和相对成熟度。

## 维护原则

- HTML lens 必须写清来源、更新时间、证据边界和未覆盖边界。
- 同一 lens 的 PDF / PNG / SVG 只能作为从 canonical HTML / source / manifest 派生的导出件，不和 HTML 同步提交；不得为对话预览另画一张不同源 PNG。
- 持久 HTML lens / print view 必须写清 `output_mode`、`export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports` 和 `conversation_png_preview`。
- 重要节点如果需要固化，另建 snapshot；普通追问默认更新 current lens。
