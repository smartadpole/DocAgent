---
type: governance-profile
id: GOV-MARKDOWN-DOCUMENT-PROFILE-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-29
tags: [markdown, documentation, obsidian, links, rendering, validation]
---

# Wiki Markdown 文档治理 Profile v1

上游设计 owner：AcknowledgeBase 的 `projects/design/topics/knowledge-organization/markdown-document-governance/README.md`。

本页只维护 wiki 的本地采纳值和例外，不复制上游完整设计。

```yaml
markdown_profile:
  profile_id: wiki-obsidian-vault-v1
  dialect: obsidian-vault
  document_roots:
    - .
  primary_renderer: obsidian
  secondary_renderers:
    - github-gfm
    - markdown-owner-viewer
  internal_link_style: wikilink
  external_link_style: markdown
  heading_contract: body-h1
  frontmatter_contract: wiki-document-type-schema
  asset_policy: wiki-assets-and-view-source-owner
  generated_paths:
    - views
  validation_commands:
    - python3 scripts/check_all.py --only markdown-document-governance
    - python3 scripts/check_all.py --only knowledge-linking
  exceptions:
    - raw source bodies
    - archive history
    - fenced syntax examples
```

## 本地规则

- wiki 内部页面语义跳转使用 wikilink，外部来源使用普通 Markdown link。
- qualified path、通用文件名和页内锚点在读者面使用短语义显示名。
- `页面` 导航表中的 wikilink 别名分隔符写成 `\|`，避免被表格 parser 拆列。
- 可点击链接不放进 inline code；命令、物理路径字符串和语法示例可以使用反引号。
- `views/` 是派生阅读层；修改生成视图前先找 canonical Markdown / manifest / generator。
- 结构、链接、frontmatter、资产或生成内容变化时运行 Markdown 专项 sensor；用户可见渲染问题还需要 primary renderer readback。

## 与相邻 owner 的边界

- [[knowledge-linking-rules]]：判断知识之间是否需要上位、邻接、来源、应用和反向关系。
- [[topic-visual-presentation-rules]]：判断主题读者界面和图文呈现质量。
- [[documentation-maintenance-rules]]：执行 owner discovery、stale / duplicate-rule 和传播。
- 本页：声明 wiki 实际使用的 Markdown 方言、renderer 和验证命令。
