"""Source-wiring contracts for native skills, independent of heading/output shape.

These guards preserve critical capability anchors through progressive disclosure.
They do not prove semantic correctness or model behavior; use real task probes.
"""
SKILL_INVARIANTS = {
    'cross-project-governance-audit': ('source-depth', 'true-gap', 'recognition-gap', 'signal-only-gap', '不授权', 'runtime validation', 'project-bound fact'),
    'cross-project-skill-adoption-prompt': ('allowed write roots', '保护未提交工作', '直接迁移', '验证、提交', '语义覆盖', 'external readback', '项目事实'),
    'delivery-retrospective': ('原始目标', '实际结果', '反证', 'open 行动', 'Issue', '验收', '既有 owner'),
    'documentation-maintenance': ('diff', '直接完成', 'Generated', 'thin adapter', 'owner', '方案尚未裁决', '未覆盖边界'),
    'goal-contract': ('用户明确要求 Goal', '原 owner', '预算', '停止', 'non-default', 'partial / blocked', '不能替代'),
    'historical-dialogue-retrospective': ('原始 session', 'memory', '用户纠偏', '时间窗', '反证', '一次偏差', 'owner'),
    'issue-analysis': ('原始现象', '最小根因候选', 'confirmed / likely / possible / blocked', 'receipt 不等于 DB readback', '非默认值', 'allowed write roots', '不自动'),
    'knowledge-linking': ('非 log', 'owner', '邻接', '来源', '反向回链', '不证明', 'Markdown'),
    'loop-engineering': ('Discovery source', 'Run queue', 'Persistent state', 'Evaluator oracle', 'Scheduler / trigger', 'Budget / stop', '单 agent', '恢复游标'),
    'performance-bandwidth-analysis': ('business denominator', 'timing ledger', 'coverage matrix', 'service-side readback', '重叠', '残差', '生产容量'),
    'public-html-publish': ('public_url', 'HTML-only', 'host / prefix', 'canonical path', 'live readback', 'denial readback', 'multi-project', 'multi-host'),
    'research-capability': ('R0', 'R4', 'L1', 'L6', 'R2+', 'Source Plan', 'coverage', 'Evidence Delta', 'counter-evidence', '停止', '独立 outcome'),
    'retrospective-capability': ('显式', '上轮行动兑现回检', 'projects/retrospectives/<year>/', 'by-theme', 'by-type', '不替代', '直接证据'),
    'runtime-config-switch': ('优先级', '活动任务', 'secret', 'reload/restart', 'default path proof', 'override', 'service-side readback', '清理', '回滚'),
    'technology-research': ('research-capability/SKILL', 'license/供应链', '替代', 'PoC', '源码', 'deal-breaker', '不证明生产可用'),
    'topic-visual-presentation': ('默认快速呈现', '不强制', 'PDF/PNG', '独立五门', 'page-tree', '单一 edges', 'topic-presentation-contract.v2', 'independent judge', '不成为第二真相源'),
    'transferable-skill-governance': ('true-gap', 'recognition-gap', 'signal-only-gap', 'project-bound-gap', 'recognize / complete / upgrade / merge / adapt / defer / reject', 'external readback', '不以变短判失败'),
    'work-item-auto-decomposition': ('transfer_ready: false', 'Gate -> FP -> EP -> TASK', '父 EP', '原始现象', '不能自动关闭', '不预建 Issue', '不另建看板'),
}

def skill_terms(name: str) -> tuple[str, ...]:
    return SKILL_INVARIANTS[name]
