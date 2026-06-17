---
type: publication-profile
domain: views
status: blocked
source_capability: AcknowledgeBase
updated_at: 2026-06-17
tags: [views, html, public, publish]
---

# Public HTML Publication Profile

本页定义当前 wiki 仓库 HTML views 的公网发布口径。它只承接发布入口和访问边界，不替代 Markdown 真相源、项目状态、验收关闭或发布裁决。

## 当前方案

- 发布方式：blocked；尚未配置真实公网 host、静态托管项目、tunnel 或 deploy token。
- 公网入口：未配置。
- 本机或部署服务：未配置。
- 当前运行模式：blocked。
- 可选运行模式：share-only live host、static site deploy、internal preview。
- host：未配置，不能复用 LifeOS host。
- path prefix：`/wiki/views/`，仅作为本仓库独立 prefix 候选，未绑定真实 host。
- source root：`views/current/` 与 `views/snapshots/`。
- public_url 公式：`https://<host>/wiki/views/<canonical-relative-path>`；host 缺失时输出 blocked 原因。
- access shape：blocked。
- secret / token 存放：未配置；未来只能使用本仓库自己的 ignored local secret / deploy config。
- cache / headers：未配置。
- revoke / rotation：未配置。

## HTML Only

默认公网对象只包含 canonical HTML：

- 发布：`views/current/**/*.html`、`views/snapshots/**/*.html`。
- 排除：`views/exports/`、`views/.exports/`、`views/**/.exports/`、PDF / PNG / SVG 导出件。
- 不默认公开：Markdown 真相源、`projects/`、`raw/`、`assets/`、日志、Obsidian 配置、凭据、密钥、个人信息或整个仓库。

这个边界用于避免把源文档、日志、导出缓存、原始附件、凭据、健康 / 合同 / 票据 / 个人信息或整个仓库随 HTML 一起公开。

## Multi-Host Boundary

- host 是部署或机器级入口，不是项目真相源。
- 每台主机或部署环境使用自己的 token、secret、hostname、service 或 deploy target。
- 当前 host 的 live readback 不能上推到其他电脑、环境或工程。

## Multi-Project Boundary

- 多工程共享同一 host 时必须用 path prefix 分隔。
- 当前工程 prefix：`/wiki/views/`。
- 其他工程不得复用该 prefix。
- 不把 LifeOS 或其他工程的 Cloudflare / Netlify / Pages 业务事实写入当前工程规则；只吸收 AcknowledgeBase 的通用发布合同和验证口径。

## 自动公开合同

只要满足以下条件，新增 HTML 可以获得 public URL：

1. 文件位于 canonical HTML source root。
2. 文件不是 `.exports`、隐藏文件、导出缓存或非 HTML。
3. host / deploy / tunnel / preview 环境可用。
4. public_url 生成命令或 deploy output 可用。
5. live readback 能读取 public URL。

当前状态为 `blocked`，不能声称公网完成。生成或刷新 canonical HTML 后，最终回复必须给出 public URL；如果没有给出，必须说明未生成 HTML、未发布、服务不可用、权限缺失、隐私阻塞或其他具体原因。

根域名、全局目录、直接路径、导出缓存和非公开对象必须按本 profile 返回 404 / 403 / blocked。

## 验证

静态检查：

```sh
python3 scripts/check_public_html_publish.py
```

公网读回：

```sh
python3 scripts/check_public_html_publish.py --live
```

生成某个 HTML 的 public URL：

```sh
# blocked until host/deploy target is configured.
```

启动或部署服务：

```sh
# blocked until this repository owns a host/deploy target.
```
