---
name: public-html-publish
description: 将已授权的 canonical HTML 发布为可分享公网 URL，检查公开范围、路径隔离与真实读回；生成本地 HTML 本身不触发发布。
maturity: mature
evidence_signals: [skill, TRANSFER, governance, template, publication-profile, quality-gate, sensor, views]
transfer_ready: true
source_capability: upstream-publication-contract
sensor: python3 scripts/check_all.py --only public-html-publish
---

# Public HTML Publish

只在用户要求公网访问、外部分发或明确授权自动发布时使用。HTML 呈现与公开发布是独立动作；发布权限不由文件生成推导。

## 发布合同

读取 [[views/publication]] 与实际 canonical HTML，确认授权对象、host / prefix、部署模式和拒绝路径。当前运行状态只由 publication profile 与本轮读回承接，不在技能维护第二份 live/blocked 状态。

默认 HTML-only：本仓 canonical root 为 `views/current/` 与 `views/snapshots/`。Markdown、projects、raw、日志、原始 assets、`.exports`、PDF/PNG/SVG 或全仓目录不默认公开；确需新增资源时单独明确 allowlist。

public_url 按 host + path prefix + canonical relative path 生成，保持 canonical path 映射。share-only live host / Tunnel、static site deploy（如 Pages / Netlify）、internal preview 分开声明；临时隧道不等于持久部署。

发布前检查本机绝对路径、内部系统地址、凭据、个人或敏感业务信息。多工程使用各自 prefix/profile，multi-project / multi-host 的授权、撤销和 secret 边界不互相借用。

## 读回与交付

静态检查证明配置与范围；live readback 验证公网响应、稳定内容标记、内部链接；denial readback 验证根目录、导出缓存和其他非公开对象被拒绝。HTTP 200、构建成功、localhost、截图或配置存在不能单独证明发布完成。

已授权发布但缺 host、部署权限或读回时说明具体 blocked 原因，不编造 URL。成功后给可访问 public URL、canonical/source 追溯与撤销边界。普通本地 HTML 生成无需声明缺公网条件。

使用 [[templates/public-html-publication-template]] 补实际 profile；规则 owner 为 [[public-html-publish-rules]]。检查命令 `python3 scripts/check_public_html_publish.py`；公网条件具备时执行 `--live` 或等价实际读回。sensor 状态不能代替现场证据。迁移见 [[skills/public-html-publish/TRANSFER]]。
