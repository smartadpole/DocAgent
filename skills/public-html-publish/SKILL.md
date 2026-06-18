---
name: public-html-publish
description: HTML 公开发布技能。用于把本仓库 canonical HTML views 通过受控 public URL、静态托管或等价公网入口发布给外部阅读者，同时维护 HTML-only 边界、host / prefix 分离、public_url 公式、live readback 和 blocked 口径。
maturity: active
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
4. 默认只发布 `views/current/**/*.html` 与 `views/snapshots/**/*.html`；不默认公开 Markdown、`projects/`、`raw/`、日志、assets、`.exports` 或整个仓库。
5. 按 publication profile 生成 public_url：host + path prefix + canonical relative path；缺少 host / deploy / token / live readback 时只输出 blocked 原因。
6. 发布前检查 HTML 中是否包含本不该公开的本机绝对路径、内部系统地址、凭据、密钥、票据、健康、合同或个人联系信息。
7. 完成前运行静态检查；有公网条件时再运行 live readback 和 denial readback，并确认 multi-project / multi-host 边界没有互相借用。
8. 生成或刷新 canonical HTML 后，最终回复必须给出 public URL；如果不能给出，必须说明具体 blocked 原因。

## 成熟度与证据信号

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

当前仓库默认目标为 L3；除非 [[views/publication]] 有真实 host 和 live readback，否则状态保持 `blocked`。

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
