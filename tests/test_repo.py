import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RepoTest(unittest.TestCase):
    def test_core_skill_frontmatter(self):
        for name in ['business-build','business-grow','business-evaluate','business-pack-author']:
            text