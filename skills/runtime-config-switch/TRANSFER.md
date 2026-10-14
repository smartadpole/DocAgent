# Runtime Config Switch Transfer

## 能力目标

将配置修改与live service默认路径消费证明闭环。 运行入口为 [[skills/runtime-config-switch/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- 配置源/优先级、活动任务、变更窗口、最小编辑、runbook与rollback。
- live readback与default path proof，请求override不能替代默认路径。
- 低风险smoke、receipt与持久化readback、synthetic cleanup及owner回写。
- secret保护及配置证据不能上推模型、性能或发布验收。

## 只能抽象吸收

具体key、部署方式、端口、地址、重启命令、验证账号与清理方式只在目标授权环境确定。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

分别验证文件已改但服务未消费、override生效而默认未切换、smoke存在持久化副作用；缺readback保持partial/blocked。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
