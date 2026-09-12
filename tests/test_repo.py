import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RepoTest(unittest.TestCase):
    def test_core_skill_frontmatter(self):
        for name in ['business-build','business-grow','business-evaluate','business-pack-author']:
            text=(ROOT/'skills'/name/'SKILL.md').read_text()
            self.assertTrue(text.startswith('---\n'))
            self.assertIn(f'name: {name}',text)
            self.assertRegex(text,r'description: .+')
    def test_canonical_specs(self):
        for n in range(1,7):
            self.assertTrue(list((ROOT/'docs').glob(f'{n:02d}-*.md')))
    def test_full_apache_license(self):
        text=(ROOT/'LICENSE').read_text()
        self.assertIn('TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION', text)
        self.assertIn('END OF TERMS AND CONDITIONS', text)
    def test_pack_showcase_prompt(self):
        text=(ROOT/'extension-packs'/'professional-services'/'PACK.md').read_text()
        self.assertIn('## Showcase exact prompt',text)
    def test_representative_levels(self):
        for level in range(1,6):
            self.assertTrue((ROOT/'examples'/f'level-{level}').exists())
if __name__=='__main__': unittest.main()
