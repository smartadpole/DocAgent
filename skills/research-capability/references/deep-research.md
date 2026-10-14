# 深度研究与信息流处理

仅在 R2+、正式研究报告或重复采集/解析的外部信息流任务读取。公共判断规则在 [[skills/research-capability/SKILL]]；以下模块按触发加载，不要求每项同时发生。

## R2+ 证据计划与覆盖

广泛采集前完成 Source Plan checkpoint：关键问题对应什么来源类型、哪些一手证据不可缺、coverage target、contradiction plan、access boundary、停止条件和行动 owner。复用已有合同，短计划可以直接留在当前 owner，无需建立平行目录。

coverage matrix 对每个关键问题标 covered / partial / blocked，保留 supporting evidence、counter-evidence、stale evidence 与下一项取证。来源数量、报告长度不等于覆盖；一项 blocked 限制对应 claim，不能把其余已验证事实一概降级。

R2 验证计划写样本、指标、基线、成功与退出条件；R3 解释机制、替代路线和敏感性；R4 对关键承诺做相互独立的三角核验与风险分级。Adopt 需要与 claim scope 相符的一手证据及本地验证，不能仅靠桌面资料宣称生产可用。

## 信息流 Intake

需要持续采集、归档或解析外部材料时，用 [[templates/research-intake-template]] 保存 Research Intake / source package：source_type、source_ref、访问权限/限制、capture method、raw landing、extraction quality 与目的落点。单个短答材料无需填全集。

保留原文与派生摘要的区别；截图/OCR/截断内容标清提取缺口。若使用 parser agent 或 evaluator oracle，记录实际角色和验证证据；未使用时不捏造。A3 compensation 仅在对应自动化动作需要补偿时定义，不能以读取授权推导自动外写或绕过访问控制。

正式归档应提供可追溯原文、source ledger 或数据快照，不把浏览器历史和聊天摘要当唯一来源。事实质量取决于原文与核验，不因有/无 parser 或表格就自动认定 L1/confirmed。

## 新证据与修订

Evidence Delta Re-open 先判 materiality：duplicate、clarification、conclusion-changing、architecture-changing。影响结论时保留直接观察，补必要一手核验和反证，重算受影响结论、行动等级与风险；记录哪些 owner 已更新，哪些未授权/blocked。无关判断无需重算。

评价失败或关键缺口影响结论时，用 Revision Brief 明确问题、Delta Source Plan 明确最小补证、next-run decision 明确继续/等待/停止。修订不能无限扩范围或预算。

## 报告、评价与边界

Research Case Packet 是证据集合，不是必须新建的目录：可组合 Original Problem Brief、Research Contract、Source Plan、Source Ledger、Coverage Matrix、Evidence Delta、结论、采用合同和 Revision Brief。使用 [[templates/technology-research-contract-template]]、[[templates/technology-research-report-template]]、[[templates/technology-research-evidence-matrix-template]]、[[templates/technology-research-adoption-contract-template]] 的适用部分。

deterministic validator 检查结构；独立 evaluator / 人工 reviewer 评价证据覆盖、反证和结论校准；实际采用或读者任务证明 outcome/utility。未做独立评价就写 outcome review 未验证，不伪造 provenance，也不把缺独立 reviewer 变成无法交付已有研究的阻塞。

外部原文索引和研究结论应可相互追溯。desk evidence、local validation、PoC、service/runtime readback、human approval 分开记录，专业批准与正式状态关闭由各 owner 裁决。
