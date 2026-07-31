---
type: publication-profile
domain: views
status: blocked
updated_at: 2026-07-31
tags: [views, html, public, publish]
---

# Public HTML Publication Profile

本页定义 Software Wiki 的 public-html-publish 发布口径。当前只保留通用能力合同，本仓没有已发布页面。

## 当前方案

- 发布方式：未配置。
- host: none
- path prefix：未配置。
- source root：`views/`。
- public_url：无。
- live readback：未配置，`python3 scripts/check_public_html_publish.py --live` 应返回 blocked。
- 边界：不借用其他工程的 host、prefix、secret、mount、服务状态或 live readback 证明本仓已发布。

## HTML Only

未来如启用发布，只允许发布 `views/**/*.html` 中的 canonical HTML，并排除 `.exports`、Markdown、PDF / PNG / SVG、日志、项目页、数据库导出、原始 assets、密钥和本地运行状态。

## Multi-Host / Multi-Project Boundary

其他工程的公开页面、host、prefix、签名地址和 live readback 不记录在本 profile，也不能替代本工程验收。未来如需发布，必须为本仓单独配置并验证。

## 自动公开合同

未来新增 HTML 只有在以下条件同时成立时才可声称已发布：

1. 位于 `views/` 下且后缀为 `.html`。
2. 不在隐藏目录、`.exports` 或导出缓存中。
3. 本仓拥有独立声明的 deploy target、host / prefix 和撤销方式。
4. 本仓生成自己的 public URL，不借用其他工程地址。
5. live readback 与 denial readback 同时通过。

最终回复如声称本工程 HTML 已公开，必须给出对应 public URL；不能用 `file://`、localhost、截图或静态检查替代公网 live readback。
