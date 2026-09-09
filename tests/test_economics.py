import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills'/'business-build'/'scripts'/'economics.py'
FIX=ROOT/'tests'/'fixtures'/'service-economics.json'
class EconomicsTest(unittest.TestCase):
    def test_fixture(self):
        p=subprocess.run([sys.executable,str(SCRIPT),str(FIX)],capture_output=True,text=True,check=True)
        d=json.loads(p.stdout)
        self.assertEqual(d['variable_cost_total'],850.0)
        self.assertEqual(d['contribution'],1550.0)
        self.assertEqual(d['cash']['closing'],2550.0)
    def test_missing_field_fails(self):
        p=subprocess.run([sys.executable,str(SCRIPT)],input='{"currency":"GBP"}',capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0)
if __name__=='__main__': unittest.main()
