---
name: public-html-publish
description: HTML 公开发布技能。用于把本仓库 canonical HTML views 通过受控 public URL、静态托管或等价公网入口发布给外部阅读者，同时维护 HTML-only 边界、host / prefix 分离、public_url 公式、live readback 和 blocked 口径。
maturity: mature
evidence_signals: [skill, TRANSFER, governance, template, publication-profile, quality-gate, sensor, views]
transfer_ready: true
source_capability: AcknowledgeBase
sensor: python3 scripts/check_all.py --only public-html-publish
---

# Public HTML Publish

## 定位

本技能承接当前 wiki 仓库内 canonical HTML views / lens / report 的公网发布合同。它只负责发布入口、访问边界、URL 生成和公网读回验证，不替代 Markdown 真相源、项目状态、验收关闭、发布裁决或人工确认。

本仓库统一采用 AcknowledgeBase 的 `public-html-publish` 源能力；只吸收抽象后的 HTML-only、host / prefix / canonical path、public_url、live readback、拒绝路径和 blocked 口径。禁止复制 LifeOS 的 host、prefix、secret、LaunchAgent、screen session 或任何一次性运行事实。

## 触发

- 用户要求 HTML / views / lens / report 能公网访问、远程查看、外部分发或获得可分享 URL。
- 用户要求新增 HTML 后自动得到 public URL。
- 用户要求检查 public_url、host、path prefix、Cloudflare / Netlify / Pages / 静态托管、live readback 或拒绝路径。

## 工作流

1. 读取 [[views/publication]]、[[views/README]]、相关 canonical HTML 和本技能的 `TRANSFER.md`。
2. 区分发布对象：canonical HTML、Markdown 真相源、导出缓存、原始 assets、snapshot 和全局目录入口。
3. 判定发布模式：`share-only live host`、`static site deploy`、`internal preview` 或 `blocked`。
   - `Cloudflare Pages` / `Pages Direct Upload` 可作为 static site deploy 模式；只有完成部署读回、路径隔离、回滚或撤销说明后，才能写为可公开访问。
   - `Cloudflare Tunnel` 或本机 share-only host 只证明当前隧道 / profile 可访问，不等同于 Pages 持久部署。
4. 默认只发布 `views/current/**/*.html` 与 `views/snapshots/**/*.html`；不默认公开 Markdown、`projects/`、`raw/`、日志、assets、`.exports` 或整个仓库。
5. 按 publication profile 生成 public_url：host + path prefix + canonical relative path；缺少 host / deploy / token / live readback 时只输出 blocked 原因。
6. 发布前检查 HTML 中是否包含本不该公开的本机绝对路径、内部系统地址、凭据、密钥、票据、健康、合同或个人联系信息。
7. 完成前运行静态检查；有公网条件时再运行 live readback 和 denial readback，并确认 multi-project / multi-host 边界没有互相借用。
8. verification-loop 必须包含证据计划、检查方式、行动 owner、完整产物和上层抽象：静态检查证明合同，live readback 证明公网访问，denial readback 证明拒绝路径，artifact completeness 证明 public URL / canonical HTML / source page / export QA 可互相追溯。
9. 生成或刷新 canonical HTML 后，最终回复必须给出 public URL；如果不能给出，必须说明具体 blocked 原因。

## 成熟度与证据信号

- `maturity`：`mature`。本技能已有 skill、TRANSFER、governance、publication profile、canonical HTML sample、template、views registry 和 sensor；具体公开可访问结论必须另有 live readback，缺失时降级为 blocked。
- `skill`：本页定义触发、发布对象、工作流、验收口径和禁止项。
- `TRANSFER`：跨工程迁移边界见 [[skills/public-html-publish/TRANSFER]]。
- `governance`：公开发布裁定见 [[public-html-publish-rules]]。
- `template`：publication profile 骨架见 [[templates/public-html-publication-template]]。
- `views`：当前仓库发布 profile 见 [[views/publication]]。
- `sensor`：`python3 scripts/check_all.py --only public-html-publish` 检查 skill、TRANSFER、governance、template、profile、gitignore 和 canonical HTML 边界。
- `evidence boundary`：结构接线和静态检查只能证明发布合同存在；真实公网完成必须以 live readback 为准。

| Level | 名称 | 最低要求 |
| --- | --- | --- |
| L1 | local export | 只有本机 HTML 或导出文件；不能声称公网可用。 |
| L2 | publish profile | 有 publication profile，区分 canonical HTML、导出缓存、源文档和 assets。 |
| L3 | URL contract | 有可重复 public_url 公式、host / prefix / canonical path 分离、gitignore 和静态检查。 |
| L4 | live readback | 有公网 200、内容标记、拒绝路径和内部链接可达验证。 |
| L5 | multi-project safe publish | 支持多工程 / 多主机边界、撤销 / secret rotation、隐私审查和迁移验证。 |

当前仓库按 [[views/publication]] 使用 share-only live host；只有 `python3 scripts/check_public_html_publish.py --live` 同时通过 share 200、denial 404 和 multi-project prefix 边界时，才能声称本仓 HTML 已公开。若 host、secret、mount、Cloudflare Tunnel / Pages Direct Upload / 其他 deploy target 或 live readback 缺失，必须降级为 `blocked`。

## 输出格式

```markdown
**Public HTML Publish**
- Canonical HTML:
- Publication profile:
- Public URL:
- Mode:
- Static check:
- Live readback:
- Denial readback:
- Cloudflare Pages / Pages Direct Upload:
- verification-loop:
- Artifact completeness:
- Blocked reason:
- Not published:
```

## 验收口径

- 任意 canonical HTML 都能按 [[views/publication]] 的 public_url 公式得到可解释 URL，或得到明确 blocked 原因。
- 发布对象限定为 canonical HTML；`.exports`、PDF / PNG / SVG、Markdown、日志、项目页、原始 assets、凭据和整个仓库不默认公开。
- 公网验证必须使用 `python3 scripts/check_public_html_publish.py --live` 或等价 `curl -L -A 'Mozilla/5.0'` 读回。
- 根路径、全局目录、导出缓存和非公开对象必须按 profile 返回 404 / 403 / blocked。

## 禁止项

- 不把 `file://`、`localhost`、截图、PDF、PNG、构建成功或本机打开当作公网发布完成。
- 不混用 Cloudflare Tunnel、Pages、Workers、Netlify、GitHub Pages、本机服务和内网预览事实。
- 不默认公开 assets、logs、projects、raw data、Markdown 真相源或整个仓库。
- 不让 public HTML 成为第二份真相源。
- 不复制 LifeOS host、path prefix、share secret、LaunchAgent、screen session 或运行状态。

## 相关入口

- [[skills/public-html-publish/TRANSFER]]
- [[public-html-publish-rules]]
- [[templates/public-html-publication-template]]
- [[views/publication]]
- [[views/README]]
- [[skills/problem-focused-visual-presentation/SKILL]]


## L5 live profile update (2026-06-19)

This project now treats public-html-publish as a live share-only publication contract. A valid publication claim must include `public_url`, HTML-only source scope, `host / prefix`, canonical path mapping, live readback, denial readback, multi-project prefix isolation, and multi-host boundary notes. If any host, secret, prefix, or live denial check is unavailable, the result must downgrade to blocked instead of claiming L5.
