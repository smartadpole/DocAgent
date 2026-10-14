# Loop 的委派运行

仅在循环确需委派且已获授权时读取。单 agent 循环继续使用 [[skills/loop-engineering/SKILL]]，不为拓扑而启动 Worker。

## Worker 合同

主控维护同一 Loop Contract；只有独立运行身份、恢复或合流需要时使用 [[templates/run-capsule-template]]。Worker 接收：本轮目标与输入发现项、scope、allowed writes、必要 inherited context、required evidence、limits、状态与 next-run recommendation。

缺少 limits 或回传无法关联输入项时，先补证据，不能用于关闭整体循环。Worker 只证明自己执行的范围，不把局部 passed 提升成全局完成。

涉及子工程代码时做 Subproject Git preflight：目录、branch/upstream、remotes、必要的 fetch、ahead/behind/diverged、dirty/untracked 与 local-only risk。遵守目标更新策略；未授权不更新，默认不 pull/merge/rebase/reset；明确允许且安全时才做 ff-only update。

## 合流与恢复

主控依据 oracle 独立判断发现项是否真实/重复、结果证据覆盖什么、需要重试/退避/拆分/停止还是人工确认。Evaluator 可以是确定性脚本、独立 agent、人工或真实运行工具，不强迫每轮额外开模型。

合流记录消费项、Worker 输出状态、关键证据、失败/阻塞与下一轮决策。丢失 Worker、重复消息或恢复重跑不能造成重复副作用；持久状态和幂等标识应承担这一约束。跨线程通信和外部动作沿用实际授权，不由 Loop 隐含授予。
