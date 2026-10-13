"""Regression guards for conditional instruction loading; no model calls."""
import unittest
from pathlib import Path

from agent_guidance import AREAS, inspect_entry, resolve_area, inspect_adapters


ROOT = Path(__file__).resolve().parents[1]


class GuidanceTests(unittest.TestCase):
    def test_live_entry_and_all_routes(self):
        self.assertEqual(inspect_entry(ROOT), [])
        for area in AREAS:
            self.assertTrue(resolve_area(ROOT, area).is_file())

    def test_skill_projections_resolve_to_unique_source(self):
        for source in (ROOT / 'skills').glob('*/SKILL.md'):
            link = ROOT / '.agents/skills' / source.parent.name
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), source.parent.resolve())

    def test_platform_adapters_only_import_root(self):
        self.assertEqual(inspect_adapters(ROOT), [])

    def test_cold_start_stays_in_always_loaded_root(self):
        root = (ROOT / 'AGENTS.md').read_text()
        for marker in ('P0 首次接触冷启动', '零工具', '零读盘', '零命令',
                       '可以从这几个方向开始：', '推荐第一步：'):
            self.assertIn(marker, root)

    def test_no_stale_skill_projection(self):
        for link in (ROOT / '.agents/skills').iterdir():
            self.assertTrue((link / 'SKILL.md').is_file(), str(link))
            self.assertTrue(link.is_symlink(), str(link))

    def test_unknown_area_is_rejected(self):
        with self.assertRaises(ValueError):
            resolve_area(ROOT, "../../outside")

    def test_missing_root_commit_guard_cannot_hide_in_guidance(self):
        root = (ROOT / "AGENTS.md").read_text()
        self.assertTrue(inspect_entry(ROOT, root.replace("默认本地提交", "提交由细则决定")))

    def test_unlinked_owner_is_not_discoverable(self):
        root = (ROOT / "AGENTS.md").read_text()
        self.assertTrue(inspect_entry(ROOT, root.replace(AREAS["execution"][:-3], "missing-owner")))

    def test_full_text_regression_is_rejected(self):
        root = (ROOT / "AGENTS.md").read_text()
        self.assertTrue(inspect_entry(ROOT, root + "重复细节" * 3000))


if __name__ == "__main__":
    unittest.main()
