---
type: template
id: TEMPLATE-PUBLIC-HTML-PUBLICATION-001
status: active
updated: 2026-06-18
tags: [template, views, html, public-html-publish]
---

# Public HTML Publication Profile Template

用于目标工程建立 HTML 公开发布 profile。它只定义发布对象、URL 合同和验证边界，不替代 Markdown 真相源、项目状态、验收关闭或发布裁决。

## 当前方案

- 发布方式：
- 公网入口：
- 本机或部署服务：
- 当前运行模式：share-only live host / static site deploy / internal preview / blocked
- host：
- path prefix：
- source root：
- public_url 公式：
- access shape：share-only signature / static path / preview URL / login / blocked
- secret / token 存放：
- cache / headers：
- revoke / rotation：

## HTML Only

- 可以发布：
- 必须排除：
- 不默认公开：

用于避免把源文档、日志、导出缓存、原始附件、凭据、健康 / 合同 / 票据 / 个人信息或整个仓库随 HTML 一起公开。

## Multi-Host Boundary

- host 是部署或机器级入口，不是项目真相源。
- 每台主机或部署环境使用自己的 token、secret、hostname、service 或 deploy target。
- 当前 host 的 live readback 不能上推到其他电脑、环境或工程。

## Multi-Project Boundary

- 多工程共享同一 host 时必须用 path prefix 分隔。
- 当前工程 prefix：
- 其他工程不得复用该 prefix。
- 不把其他工程的 Cloudflare / Netlify / Pages 事实写入当前工程规则。

## 自动公开合同

新增 HTML 可以获得 public URL 的条件：

1. 文件位于 canonical HTML source root。
2. 文件不是 `.exports`、隐藏文件、导出缓存或非 HTML。
3. host / deploy / tunnel / preview 环境可用。
4. public_url 生成命令或 deploy output 可用。
5. live readback 能读取 public URL。

生成或刷新 canonical HTML 后，最终回复必须给 public URL；如果没有给出，必须说明未生成 HTML、未发布、服务不可用、权限缺失、隐私阻塞或其他具体原因。

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
# Fill with target project command.
```

启动或部署服务：

```sh
# Fill with target project command.
```
