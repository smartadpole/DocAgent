"""Exercise stage and impact boundaries using compact Markdown work items."""
import unittest

from staged_contracts import validate

BASE = """---
type: task
contract_profile: staged-v1
id: TASK-001
parent_ep: EP-001
owner: maintainer
status: planned
impact: [local]
---
# Task
- 目标：修复正文链接
- 范围：指定文档
- 完成条件：链接解析正确
- 验证计划：检查受影响链接
"""
EXEC = "\n- 授权依据：本轮用户要求修复\n- 执行范围：当前文档仓\n- 下一动作：更新链接并检查\n"
DONE = "\n- 验证结果：passed\n- 证据：reports/link-check.md\n- 回归守卫：链接解析检查\n- 不上推边界：不证明服务可用\n"


class StagedTests(unittest.TestCase):
    def test_duplicate_metadata_cannot_downgrade_contract(self):
        for old, new in (
            ('status: planned', 'status: done\nstatus: planned'),
            ('impact: [local]', 'impact: [production]\nimpact: [local]'),
            ('contract_profile: staged-v1', 'contract_profile: staged-v1\ncontract_profile:'),
            ('owner: maintainer', 'owner: maintainer\nowner: maintainer'),
        ):
            with self.subTest(field=old):
                self.assertTrue(validate(BASE.replace(old, new) + EXEC))

    def test_empty_profile_cannot_disable_current_contract(self):
        self.assertTrue(validate(BASE.replace('contract_profile: staged-v1', 'contract_profile:')))

    def test_duplicate_body_cannot_override_failed_evidence(self):
        doc = BASE.replace('planned', 'done') + EXEC + DONE
        for duplicate in (
            '- 验证结果：failed\n- 验证结果：passed',
            '- **验证结果**：failed\n- 验证结果：passed',
            '- 验证结果：passed\n- 验证结果：passed',
        ):
            with self.subTest(duplicate=duplicate):
                self.assertTrue(validate(doc.replace('- 验证结果：passed', duplicate)))

    def test_examples_do_not_create_duplicate_current_fields(self):
        for fence in ('```', '~~~', '````'):
            for ending in ('\n' + fence, ''):
                with self.subTest(fence=fence, ending=ending):
                    doc = BASE + '\n' + fence + 'markdown\n- 目标：示例' + ending
                    self.assertEqual(validate(doc), [])

    def test_inline_backticks_cannot_hide_conflicting_evidence(self):
        doc = BASE.replace('planned', 'done') + EXEC + DONE
        duplicate = 'note ```\n- 验证结果：failed\nnote ```\n- 验证结果：passed'
        self.assertTrue(validate(doc.replace('- 验证结果：passed', duplicate)))

    def test_minimal_registration(self):
        self.assertEqual(validate(BASE), [])

    def test_missing_parent(self):
        self.assertTrue(validate(BASE.replace('parent_ep: EP-001', 'parent_ep:')))

    def test_execution_needs_authority(self):
        self.assertTrue(validate(BASE.replace('planned', 'in_progress')))
        self.assertEqual(validate(BASE.replace('planned', 'in_progress') + EXEC), [])

    def test_unknown_impact_blocks_execution(self):
        self.assertTrue(validate(BASE.replace('planned', 'in_progress').replace('[local]', '[unknown]') + EXEC))

    def test_done_requires_evidence(self):
        self.assertTrue(validate(BASE.replace('planned', 'done') + EXEC))
        self.assertEqual(validate(BASE.replace('planned', 'done') + EXEC + DONE), [])

    def test_untested_done_rejected(self):
        self.assertTrue(validate((BASE.replace('planned', 'done') + EXEC + DONE).replace('passed', 'untested')))

    def test_service_cannot_close_on_local_proof(self):
        self.assertTrue(validate((BASE.replace('planned', 'done') + EXEC + DONE).replace('[local]', '[service]')))

    def test_production_requires_current_action_and_recovery(self):
        doc = BASE.replace('planned', 'in_progress').replace('[local]', '[production]') + EXEC
        self.assertTrue(validate(doc))
        self.assertEqual(validate(doc + '\n- pre_action_check：allowed: 当前动作 / 目标 / 证据已核验\n- 恢复方法：按服务合同回退\n'), [])

    def test_cross_repo_needs_preflight_and_handoff(self):
        doc = BASE.replace('planned', 'in_progress').replace('[local]', '[cross_repo]') + EXEC
        self.assertTrue(validate(doc))
        self.assertEqual(validate(doc + '\n- Git preflight：clean and aligned\n- 回传入口：父项\n'), [])

    def test_issue_unknown_root_cause_can_register(self):
        doc = BASE.replace('type: task', 'type: issue').replace('status: planned', 'status: open')
        doc += '\n- 用户可见症状：打开链接报错\n- 期望行为：页面能打开\n- 影响范围：单文档\n- 证据：用户报告\n'
        self.assertEqual(validate(doc), [])
        self.assertTrue(validate(doc.replace('status: open', 'status: closed')))

    def test_invalid_stage_and_placeholder(self):
        self.assertTrue(validate(BASE.replace('planned', 'almost_done')))
        self.assertTrue(validate(BASE.replace('maintainer', '待补')))

    def test_blocked_action_cannot_become_execution_permission(self):
        doc = BASE.replace('planned', 'in_progress').replace('[local]', '[production]') + EXEC
        self.assertTrue(validate(doc + '\n- pre_action_check：blocked: 没有部署授权\n- 恢复方法：回退\n'))

    def test_failed_service_proof_cannot_close_task(self):
        doc = BASE.replace('planned', 'done').replace('[local]', '[service]') + EXEC + DONE
        self.assertTrue(validate(doc + '\n- service-side validation：failed\n- end-to-end validation：untested\n- 非默认值 / 边界值：尚未验证\n'))

    def test_service_closure_with_all_required_proofs(self):
        doc = BASE.replace('planned', 'done').replace('[local]', '[service]') + EXEC + DONE
        proof = '\n'.join('- ' + key + '：passed: reports/service.md' for key in ('service-side validation', 'end-to-end validation', '非默认值 / 边界值'))
        self.assertEqual(validate(doc + '\n' + proof), [])

    def test_profile_removal_cannot_bypass_new_work_item(self):
        self.assertTrue(validate(BASE.replace('contract_profile: staged-v1\n', '')))

    def test_required_contract_cannot_hide_in_body_or_unclosed_metadata(self):
        examples = (
            BASE.replace('\n---\n# Task', '\n# Task'),
            '# Work item without metadata',
            '---\ntitle: example\n---\n```yaml\n' + BASE + '\n```',
        )
        for doc in examples:
            with self.subTest(doc=doc):
                self.assertTrue(validate(doc, require_contract=True))

    def test_native_templates_instantiate_minimal_records(self):
        import re
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        for kind, replacements in (
            ('task', {'owner:': 'owner: maintainer', '- 目标：': '- 目标：修复链接',
                      '- 范围：': '- 范围：文档', '- 完成条件：': '- 完成条件：链接可解析',
                      '- 验证计划：': '- 验证计划：运行链接检查'}),
            ('issue', {'owner:': 'owner: maintainer', '- 期望行为：': '- 期望行为：页面可访问',
                       '- 影响范围：': '- 影响范围：指定页面'}),
        ):
            with self.subTest(kind=kind):
                template = (root / f'templates/development-{kind}-template.md').read_text()
                metadata = re.search(r'```yaml\n(---.*?---)\n```', template, re.S)[1]
                body = template.split('```', 2)[2]
                # New issues copy the original phenomenon first; closure fields are conditional.
                if kind == 'issue':
                    body = body.split('## 按调查进展补齐')[0]
                doc = metadata + '\n' + body
                for old, new in replacements.items():
                    doc = doc.replace(old, new)
                self.assertEqual(validate(doc), [])

    def test_legacy_is_not_retroactively_reformatted(self):
        self.assertEqual(validate('# Historical work item'), [])


if __name__ == '__main__':
    unittest.main()
