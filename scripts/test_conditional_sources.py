"""Fail closed when progressive-disclosure owners lose their real routes."""
import tempfile
import unittest
from pathlib import Path
from agent_guidance import read_conditional_sources

class ConditionalSourcesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'skills/demo').mkdir(parents=True)
        self.rel = 'skills/demo/SKILL.md'
    def write(self, declaration, link='[[skills/demo/deep]]'):
        (self.root / self.rel).write_text('---\nconditional_sources: '+declaration+'\n---\n只在跨服务验收时读 '+link+'\n入口')
        (self.root / 'skills/demo/deep.md').write_text('service-side readback')
    def test_explicit_linked_owner_is_included(self):
        self.write('[skills/demo/deep.md]'); errors=[]
        self.assertIn('service-side readback', read_conditional_sources(self.root,self.rel,errors)); self.assertEqual(errors,[])
    def test_unlisted_neighbor_not_included(self):
        self.write('[]'); errors=[]
        self.assertNotIn('service-side readback', read_conditional_sources(self.root,self.rel,errors)); self.assertEqual(errors,[])
    def test_missing_route_fails(self):
        self.write('[skills/demo/deep.md]', '没有链接'); errors=[]
        self.assertNotIn('service-side readback', read_conditional_sources(self.root,self.rel,errors)); self.assertTrue(errors)
    def test_missing_file_fails(self):
        self.write('[skills/demo/deep.md]'); (self.root/'skills/demo/deep.md').unlink(); errors=[]
        read_conditional_sources(self.root,self.rel,errors); self.assertTrue(errors)
    def test_escape_fails(self):
        self.write('[../outside.md]', '[[../outside]]'); errors=[]
        read_conditional_sources(self.root,self.rel,errors); self.assertTrue(errors)
    def test_duplicate_fails(self):
        self.write('[skills/demo/deep.md, skills/demo/deep.md]'); errors=[]
        read_conditional_sources(self.root,self.rel,errors); self.assertTrue(errors)
    def test_cycle_fails(self):
        self.write('[skills/demo/SKILL.md]', '[[skills/demo/SKILL]]'); errors=[]
        read_conditional_sources(self.root,self.rel,errors); self.assertTrue(errors)
    def test_malformed_manifest_fails(self):
        self.write('skills/demo/deep.md'); errors=[]
        read_conditional_sources(self.root,self.rel,errors); self.assertTrue(errors)

if __name__ == '__main__': unittest.main()
