---
name: knowledge-linking
description: 新增或大改长期知识页时确定主 owner、阅读入口和有意义的关联；修补孤页，避免重复正文与为过检查而堆链接。
maturity: leading
evidence_signals: [skill, README entry, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only knowledge-linking,skill-maturity
---

# Knowledge Linking

让长期知识能被找到、理解和维护。只涉及本轮新增或实质改变的页面，不因小修改扩成全库治理。

## 落位与关系

依据内容价值选主 owner：原始材料归 raw/inbox/assets，单篇材料整理归 articles，可复用概念归 concepts，执行规则归 governance，Agent 方法归 skills，字段骨架归 templates，项目事实归项目 owner，历史过程归 log。使用工程已有目录，不为每层预建文件。

维护可解释的关系画像：主入口、上位/owner、确有关系的邻接、需要时的反向回链、来源与适用边界。邻接页不存在时无需凑数量；知识页至少能从非 log 的稳定入口被发现。跨层内容只维护一个正文 owner，其他页面引用并补上下文。

需要外部事实时区分原文观察、已验证事实、方法启发与设计推论，并查证可能变化的来源；链接存在不证明内容正确。

## 写入与检查

按影响更新已有 README / INDEX / registry 或上位入口，回看链接确实说明概念、案例、规则、模板或证据关系。Markdown 表达规则按需要读 [[governance/markdown-document-governance-profile.v1]]，不复制进本技能。

相关检查：`python3 scripts/check_all.py --only knowledge-linking,markdown-document-governance`。sensor 检查结构，语义关系由内容判断；不能用更多链接补偿错误关系。项目路径、运行状态和一次性结论不晋升通用知识。

规则 owner：[[governance/knowledge-linking-rules]]；迁移见 [[skills/knowledge-linking/TRANSFER]]。
