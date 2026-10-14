# Public Html Publish Transfer

## 能力目标

在明确发布授权下提供HTML-only公网访问及隔离读回。 运行入口为 [[skills/public-html-publish/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- host / prefix / canonical path与public_url映射，发布模式、live readback和denial readback。
- multi-project / multi-host隔离、敏感内容检查、撤销与凭据边界。
- 发布状态仅归publication profile与现场证据，不在技能写死live或blocked。
- 本地HTML生成不隐含发布；公开assets或导出件需要明确allowlist。

## 只能抽象吸收

host、prefix、部署目标、secret、拒绝路径和供应商机制由目标工程自行配置；不能借用其他工程运行事实。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

验证公开页面响应与内容、非公开路径拒绝、内部链接及撤销边界；没有公网读回不能宣称published，普通本地HTML不必报告公网阻塞。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
