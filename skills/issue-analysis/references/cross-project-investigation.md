# 跨工程调查与联测

仅在跨工程责任争议、多层状态冲突或联调修复时读取。快速诊断方法在 [[skills/issue-analysis/SKILL]]。

## 最小责任链

按实际问题追踪编排入口、服务合同、内部处理、外部依赖、持久化和展示。寻找最早知道真实状态的一层，以及未传播、未记录、错误展示或产生错误副作用的位置。根因、补观测和过期文档可能属于不同 owner。

检查配置、样本、时间、revision 和 ID 关联。未能进入服务内部时，报告已定位边界及需要子工程提供的日志/复现/readback，不伪装已确认内部原因。服务 raw output 与业务结果之间的变换必须遵守合同。

## 分工与授权

需要分工才列主责、协同方、输入依赖、写入范围、交付物、验收方式和回写 owner，标明 parallel / sequential / blocked。任务可以先由一个 agent 完成，不因“跨工程”自动创建多角色。

跨仓写入需要明确授权与 allowed roots；只读能力不等于修改权限。涉及子工程时按当地规则做 Git preflight，保护 dirty/untracked 和分叉历史，不为诊断自动 merge、reset 或覆盖。

## 验证对应 claim scope

- local validation：验证最小修复与原始复现。
- service-side validation：验证实际实例、参数消费、状态、artifact 或持久化。
- end-to-end validation：用户目标涉及跨工程链路时验证调用、后台副作用及最终 readback/UI。
- 非默认值/边界值：参数、重试、取消、并发、profile 等相关条件必须影响实际行为。
- 相关回归：只覆盖受影响合同、状态机、写入与展示边界。

哪些层适用由问题决定，不能强制每个文档问题跑三级联测。测试失败记录观察与未知，不把失败本身当作已知根因。

## 主控吸收

问题事实回 Issue；单次验证回 report；修复执行回 TASK；服务版本/配置回 service registry；合同变化回 design；范围/验收变化回 requirements/trace。主控按整体证据裁决，子工程 handoff 只证明自身范围，不自动关闭父项。
