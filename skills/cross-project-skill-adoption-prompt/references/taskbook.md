# 迁移任务书模式

仅在用户只要提示词、目标不可写或交由另一 agent 执行时读取。主入口为 [[skills/cross-project-skill-adoption-prompt/SKILL]]；此模式不改变已授权直接执行的默认交付。

## 使目标 agent 可以行动

写明需要升级的能力、目标结果、可访问源材料、allowed write roots、目标入口规则、当前范围和禁止项。目标工程先查等价 owner、技能发现入口、检查与提交规则，然后选择最小原生落点；不预设目录或强制先建新体系。

模块只覆盖源能力实际需要的目标、判断项/字段、落位、边界和验证。材料可来自 SKILL、TRANSFER、reference、schema、模板或 sensor；说明它们各自作用，不要求一律全读。缺少 TRANSFER 时从源正文提炼明确边界，不把文件缺席当成必然阻塞。

用户要求完整能力包时，列逐能力覆盖矩阵及未吸收原因；用户要求单能力时不混入其他主题字段。既有模板 [[templates/skill-transfer-contract-template]] 和 [[templates/skill-transfer-manifest-template]] 按需要取用，不强制固定章节或字段全集。

任务书应让目标 agent 知道如何验证、如何处理失败和何时停止；按目标规则完成提交并读回。最终回执应区分已修改、已验证、未验证、实际 commit 与阻塞，而不是仅宣称采纳。

## Golden 与外部评价

已有强样稿/golden baseline 时比较能力、专业边界、可执行性和验证覆盖。`generated >= baseline` 指语义和行为不退化；更短、改顺序或采用目标原生结构不是失败。

外部 evaluator 任务才补 Matrix Recognition Capsule：candidate files / scanned surfaces、baseline、true-gap / recognition-gap / signal-only-gap、验证方式及 external readback。Goodhart guard 是不为 marker/篇幅制造能力；expected impact 与实测结果分开。

系统级迁移才映射各系统层及 intelligence evidence lens，说明仍为 insufficient-evidence 的维度。评审者独立性据实际 provenance 声明，不用目标 agent 自述替代 external readback。
