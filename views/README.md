# 图文呈现层

`views/` 用于存放问题聚焦式 HTML lens。它只负责呈现，不替代 `articles/`、`concepts/`、`projects/`、`log.md` 等 Markdown 真相源。

## 目录

- `current/`：当前可反复打开的 canonical lens。
- `lens-registry.md`：lens id、关注对象、来源和失效条件索引。
- `exports/`、`.exports/`：PDF / PNG / SVG 等派生导出缓存，已由 `.gitignore` 忽略，不作为可提交真相源。

## 维护原则

- HTML lens 必须写清来源、更新时间、证据边界和未覆盖边界。
- 同一 lens 的 PDF / PNG / SVG 只能作为从 HTML 派生的导出件，不和 HTML 同步提交。
- 重要节点如果需要固化，另建 snapshot；普通追问默认更新 current lens。
