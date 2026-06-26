# Public HTML Publish 迁移边界

## 能力目标

让目标工程具备 HTML-only 的公开发布能力：canonical HTML 可以映射到可解释 public URL，非公开对象不会被默认暴露，静态检查和 live readback 能区分 published、partial 和 blocked。

## 来源

- 源能力：AcknowledgeBase `skills/public-html-publish/SKILL.md`
- 源模板：AcknowledgeBase `templates/public-html-publication-template.md`
- 源检查：AcknowledgeBase `scripts/check_public_html_publish.py`

当前 wiki 仓库只采用 AcknowledgeBase 已抽象后的能力，不直接读取或复制 LifeOS 的 host、prefix、secret、启动器、screen session、照片路径、领域事实或一次性 live readback。

## 可以吸收

- HTML-only 发布对象边界。
- `share-only live host`、`static site deploy`、`internal preview`、`blocked` 四类发布模式。
- host / path prefix / source root / canonical path / public_url 公式分离。
- 多工程、多主机边界：每个工程维护自己的 prefix、profile、secret / deploy config 和 readback。
- live readback 与 denial readback：公开 HTML 返回 200 且包含稳定标记，非公开对象返回 404 / 403 / blocked。
- 最终回复合同：生成或刷新 canonical HTML 后必须给 public URL，不能给时说明具体 blocked 原因。

## 只能抽象吸收

- LifeOS、AcknowledgeBase 或其他工程的 host、prefix、secret、启动方式、部署脚本和拒绝路径只能抽象成目标工程自己的 publication profile 字段。
- 目标工程可以使用 `views/`、`reports/html/`、`docs/views/` 或自己的 canonical HTML root，不强制照搬目录。
- 检查脚本可以用 Python、Node、Makefile、CI job 或平台 CLI 实现，重点是 HTML-only、public_url、live readback 和 blocked 口径。
- Cloudflare Tunnel、Cloudflare Pages、Pages Direct Upload、Netlify、GitHub Pages 或本机 share-only host 都只是发布模式候选；目标工程必须写自己的 host / prefix / deploy target / secret / denial path / live readback，不能借用来源工程事实。

## 禁止复制

- 不复制 LifeOS host、`/life/views/` prefix、share secret、token、LaunchAgent label、screen session 或本机运行状态。
- 不复制其他工程的业务事实、项目状态、私有路径、服务名或一次性 readback 结果。
- 不默认公开 `.exports`、PDF / PNG / SVG、Markdown、日志、项目页、assets、raw data 或整个仓库。

## 目标工程结构自检

1. 是否已有 canonical HTML 生成层、views registry 或 report 输出目录？
2. 是否已有真实 host、static deploy、tunnel、preview URL 或登录态预览？
3. public_url 是否能从 source root、path prefix 和 canonical path 稳定生成？
4. 哪些路径必须 404 / 403 / blocked？
5. 没有 live readback 时，最终回复是否明确 blocked 而不是声称已发布？

## 本仓库落位

- skill：[[skills/public-html-publish/SKILL]]
- governance：[[public-html-publish-rules]]
- template：[[templates/public-html-publication-template]]
- publication profile：[[views/publication]]
- sensor：`python3 scripts/check_all.py --only public-html-publish`
- canonical HTML source root：`views/current/` 与 `views/snapshots/`
- 默认状态：`blocked`，直到本仓库配置真实 host / deploy target 并完成 live readback。

## 验证要求

- 静态验证：`python3 scripts/check_public_html_publish.py`
- 门禁验证：`python3 scripts/check_all.py --only public-html-publish`
- 公网读回：`python3 scripts/check_public_html_publish.py --live`

没有真实 host、secret、mount、deploy target 或 live readback 时，`--live` 必须保持 blocked，不得把本机文件、localhost、截图、Cloudflare / Pages 配置存在或导出件当作公网完成证据。


## L5 live profile update (2026-06-19)

This project now treats public-html-publish as a live share-only publication contract. A valid publication claim must include `public_url`, HTML-only source scope, `host / prefix`, canonical path mapping, live readback, denial readback, multi-project prefix isolation, and multi-host boundary notes. If any host, secret, prefix, or live denial check is unavailable, the result must downgrade to blocked instead of claiming L5.
