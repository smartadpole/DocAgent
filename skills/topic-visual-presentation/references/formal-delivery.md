# 正式呈现与导出

仅在用户要求导出、正式 canonical bundle、治理评审或修改已有 v2 artifact 时读取；快速 HTML 路径在 [[skills/topic-visual-presentation/SKILL]]。

## 选择实际合同

单一格式导出按请求生成并读回该格式，不隐含完整五门治理。正式 `topic-presentation-contract.v2` bundle 使用 active profile 与 schema，保持唯一活动 writer；v1 只用于未修改历史 artifact 的只读兼容，不 dual-write。

完整 v2 bundle 规范化 subject_package / source_pack，记录信息单元、来源、lifecycle、typed_relations、organization_plan 与 reader_adaptation_profile。读者适配只采用明确任务/偏好证据，不推断敏感特征。

三轴为 task_state（understand/compare/decide/act/verify/review）、content_scope（topic/problem-focus）、materialization（inline/ephemeral/current/snapshot）；canonical-current 规范化为 current。需要 confidence/calibration 字段的正式合同使用版本化 calibration，不以模型自报替代。

## 保真与页面树

先按独立责任与阅读收益裁决 single-page / page-tree，一个 root 和 canonical edges 派生 breadcrumb、children、局部导航。每个 included unit 以 unit_id + claim_id + source_fragment_id + rendered_section_id 绑定本页，页面级来源链接不能替代正式合同的逐 claim binding。记录遗漏及理由，不能以拆页或视觉简化偷删专业信息。

完整 bundle 由同一源生成 HTML、PDF、桌面PNG与移动PNG，并读回内容、分页与视觉。仓内导出进入 gitignored `views/.exports/`；local-export-resolver 负责下载映射，时间带时区且 precision=minute。公开下载需要受控 endpoint；否则该下载保持 blocked，不暴露本机路径。

## 验证面

| 门 | 证明什么 | 不能替代 |
| --- | --- | --- |
| contract-schema | package/枚举/revision/representation合法 | 内容正确 |
| semantic-content | 来源绑定、未知项和语义覆盖 | 视觉或发布 |
| visual-quality | 布局、可访问性、导出读回 | 语义正确 |
| delivery-findability | canonical/registry/exports与适用的public live/deny | 读者任务成功 |
| reader-utility | 真实读者任务oracle | 业务关闭 |

只报告实际执行的门。正式独立语义/视觉评审需真实 builder-independent judge/reviewer provenance，真实 reader task 缺失则保持 unproven；不以静态 pass 提升其他门，也不把缺独立评审阻塞已授权的文件生成。业务验收与发布权限仍由对应 owner 裁决，不添加通用人工 veto。

## 机器入口与兼容

- schema：`governance/topic-presentation-contract.v2.schema.json`
- active profile：`governance/topic-presentation-active-profile.v2.json`
- inventory：`governance/topic-presentation-verification-inventory.v2.json`
- renderer：`python3 scripts/export_topic_presentation_bundle.py`
- portable：`python3 scripts/check_topic_visual_presentation.py --mode portable-structure`
- runtime：`python3 scripts/check_topic_visual_presentation.py --mode runtime-artifact-readback --regenerate`
- v1 zero-write：`python3 scripts/check_topic_visual_presentation.py --mode v1-compatibility`

portable 只读 tracked 合同，不要求导出已存在；runtime 才生成并读回 ignored immutable bundle。历史 artifact 按 `scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json` 做 grandfather 检查；未改不追补，同路径刷新记录 pre/post hash、reason 和 compatibility readback，不将旧正文改成 alias。
