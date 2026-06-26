---
type: template
id: TEMPLATE-PUBLIC-HTML-PUBLICATION-CONTRACT-001
status: active
updated: 2026-06-26
tags: [template, public-html-publish, publication, contract, verification-loop]
---

# Public HTML Publication Contract Template

用于把 public-html-publish 的发布合同、验证闭环和产物完整性写成可扫描、可复用的结构件。它不替代 [[templates/public-html-publication-template]]，只补充深度证据和 action checkback 字段。

## Verification Contract

- **证据计划**：
- **检查方式**：
- **行动 owner**：
- **完成口径**：
- **上层抽象 / 可复用模式**：
- **举一反三 / 同类风险**：
- **完整产物 / artifact completeness**：canonical HTML、source page、public_url、export QA、report / log 互相追溯。

## Publish Modes

| Mode | Required readback | Boundary |
| --- | --- | --- |
| share-only live host | live readback + denial readback | 不等于持久部署 |
| Cloudflare Tunnel | tunnel URL + host / prefix | 不等于 Cloudflare Pages |
| Cloudflare Pages | deployment readback + public URL + rollback / revoke | 不复制其他工程 deploy 事实 |
| Pages Direct Upload | upload output + public URL + denial readback | 需要人工确认 token / project |
| blocked | blocked reason | 不能声称公网可用 |

## Verification Loop

1. static check：`python3 scripts/check_all.py --only public-html-publish`
2. live readback：`python3 scripts/check_public_html_publish.py --live` 或等价公网 `curl`
3. denial readback：确认非公开路径 404 / 403 / blocked
4. artifact completeness：确认 canonical HTML、public_url、source page、export QA 和最终回复一致
5. action checkback：记录行动 owner、检查方式、完成口径和下一次复查触发
