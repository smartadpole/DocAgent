---
type: governance
id: GOV-PUBLIC-HTML-PUBLISH-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-18
tags: [governance, views, html, public-html-publish]
---

# Public HTML Publish Rules

本页是 [[skills/public-html-publish/SKILL]] 的治理裁定页。它定义当前 wiki 仓库何时可以声称 HTML 已公开发布、何时只能给本地路径或 blocked 原因。

## 裁定规则

- 公开发布对象只能是 canonical HTML：`views/current/**/*.html` 与 `views/snapshots/**/*.html`。
- Markdown 真相源、`projects/`、`raw/`、`assets/`、日志、Obsidian 配置、凭据、密钥、个人信息、`.exports` 和 PDF / PNG / SVG 导出件不默认公开。
- public URL 必须来自 [[views/publication]] 声明的 host、path prefix、source root 和 canonical path 公式。
- 没有真实 host / deploy target / token / tunnel / public_url 命令 / live readback 时，结论只能是 `blocked`。
- 本机打开、`file://`、`localhost`、截图、PDF、PNG 或构建成功不能替代公网读回。
- 多工程共享 host 时必须使用工程级 prefix；本仓库候选 prefix 是 `/wiki/views/`，不能复用其他工程 prefix。
- 多主机或多部署环境不能互相上推 live readback 证据。

## 质量门

发布前至少检查：

- publication profile 已声明状态、source root、public_url 公式、HTML-only 边界、multi-host / multi-project 边界和 blocked 口径。
- `.gitignore` 忽略导出缓存和 PDF / PNG / SVG 派生产物。
- HTML 中没有本不该公开的本机绝对路径、内部系统地址、凭据、密钥、票据、合同、健康或个人联系信息。
- 公开 URL 能 200 读回并包含稳定标题或标记；非公开路径按 profile 返回 404 / 403 / blocked。

## 验证

```sh
python3 scripts/check_all.py --only public-html-publish
```

如果有真实公网条件，再运行：

```sh
python3 scripts/check_public_html_publish.py --live
```

当前仓库没有公网 host，因此 `--live` 返回 blocked 是正确结果。

## 禁止项

- 不复制来源工程、上游知识库或其他工程的 host、prefix、secret、token、服务名、运行状态或一次性 live readback。
- 不把 public HTML 变成第二份真相源。
- 不把 publication profile 当项目发布裁决、验收关闭或安全审查。
- 不为了矩阵信号创建无真实发布语义的空 view。
