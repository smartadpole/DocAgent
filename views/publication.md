---
type: publication-profile
domain: views
status: live
updated_at: 2026-06-19
tags: [views, html, public, publish]
---

# Public HTML Publication Profile

本页定义 Software Wiki 的 public-html-publish 发布口径。

## 当前方案

- 发布方式：共享本机 Cloudflare Tunnel 后端上的 share-only static HTML。
- 公网 host：`https://hai-macbook-pro.smartadpole.com`。
- 本仓 mount：`/wiki/views/` -> `views/`。
- source root：`views/`。
- path prefix：`/wiki/views`。
- access shape：share-only；无目录入口；直接文件路径、隐藏目录、`.exports` 和非 HTML 默认返回 404。
- public_url 公式：`views/<relative>.html` + `.codex/local/public-html-share.env` 中的 `PUBLIC_HTML_SHARE_SECRET` -> `https://hai-macbook-pro.smartadpole.com/wiki/views/share/<relative-stem>--<signature>.html`。
- sample canonical HTML：`views/current/public-html-publish-status.html`。
- sample public URL：运行 `python3 scripts/check_public_html_publish.py --url` 生成。
- live readback：运行 `python3 scripts/check_public_html_publish.py --live`，必须同时验证 200 share URL 和 404 denial paths / denial readback。
- secret / token storage：`.codex/local/public-html-share.env` 只保留在本机，不提交 Git。
- service command：`python3 /Users/hai/Documents/Life/automation/scripts/start_public_views_screen.py --restart`。
- revoke / rotation：删除或替换本仓 `.codex/local/public-html-share.env` 后重启 `lifeos-public-views`，旧 URL 自动失效。

## HTML Only

默认只发布 `views/**/*.html` 中的 canonical HTML，排除 `.exports`、Markdown、PDF / PNG / SVG、日志、项目页、数据库导出、原始 assets、密钥和本地运行状态。

## Multi-Host Boundary

`https://hai-macbook-pro.smartadpole.com` 只证明当前 MacBook Pro 的 tunnel 和本机服务可用；其他主机必须配置自己的 host、secret、mount 和 live readback。

## Multi-Project Boundary

多工程共享同一 host，但必须用 path prefix 隔离。本工程固定使用 `/wiki/views`，不能复用其他工程 prefix；其他工程的 live readback 不能替代本工程验收。

## 自动公开合同

新增 HTML 只有在以下条件同时成立时才可声称已发布：

1. 位于 `views/` 下且后缀为 `.html`。
2. 不在隐藏目录、`.exports` 或导出缓存中。
3. `lifeos-public-views` screen session 正在运行，并挂载了 `/wiki/views=<repo>/views`。
4. 使用本仓 secret 生成 semantic share URL。
5. `python3 scripts/check_public_html_publish.py --live` 通过 share 200 和 denial readback 404 验证。

最终回复如声称本工程 HTML 已公开，必须给出对应 public URL；不能用 `file://`、localhost、截图或静态检查替代公网 live readback。
