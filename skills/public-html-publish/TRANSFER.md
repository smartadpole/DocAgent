# Public HTML Publish 迁移边界

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

## 禁止复制

- 不复制 LifeOS host、`/life/views/` prefix、share secret、token、LaunchAgent label、screen session 或本机运行状态。
- 不复制其他工程的业务事实、项目状态、私有路径、服务名或一次性 readback 结果。
- 不默认公开 `.exports`、PDF / PNG / SVG、Markdown、日志、项目页、assets、raw data 或整个仓库。

## 本仓库落位

- skill：[[skills/public-html-publish/SKILL]]
- publication profile：[[views/publication]]
- sensor：`python3 scripts/check_all.py --only public-html-publish`
- canonical HTML source root：`views/current/` 与 `views/snapshots/`
- 默认状态：`blocked`，直到本仓库配置真实 host / deploy target 并完成 live readback。

## 验证要求

- 静态验证：`python3 scripts/check_public_html_publish.py`
- 门禁验证：`python3 scripts/check_all.py --only public-html-publish`
- 公网读回：`python3 scripts/check_public_html_publish.py --live`

没有真实 host 或 live readback 时，`--live` 必须保持 blocked，不得把本机文件、localhost、截图或导出件当作公网完成证据。
