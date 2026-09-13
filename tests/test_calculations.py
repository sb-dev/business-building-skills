"""Executed fixed-data checks, not a business runtime or agent benchmark."""
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from fractions import Fraction
import json
from pathlib import Path
import unittest

from validate_repository import facts_from_prompt, subject_matches

ROOT = Path(__file__).resolve().parents[1]


def number(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Expected explicit numeric string')
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal') from exc
    if not result.is_finite():
        raise ValueError('Non-finite decimal')
    return result


def ratio(numerator, denominator):
    return {'state': 'UNDEFINED', 'count': numerator, 'reason': 'zero denominator'} if denominator == 0 else {'state': 'DEFINED', 'value': numerator / denominator}


def cash_schedule(facts, orders, deposit):
    """E12 fixed observation/scenario calculation only; tax is supplied data."""
    o = facts['observations']
    cash = number(o['opening_usable_cash'])
    schedule = [('opening', cash)]
    cash += orders * (deposit - number(o['stock_cash_per_order_day_0']) - number(o['advertising_cash_per_order_day_0']))
    schedule.append(('day_0', cash))
    cash -= orders * number(o['payroll_cash_per_order_day_14'])
    schedule.append(('day_14', cash))
    cash -= number(o['tax_cash_day_30'])
    schedule.append(('day_30', cash))
    cash += orders * (number(o['price_per_order']) - deposit)
    schedule.append(('day_45', cash))
    return schedule


class FixedCalculations(unittest.TestCase):
    def test_e01_all_workloads_and_exact_boundary(self):
        f = json.loads((ROOT / 'examples/level-01/E01/input.json').read_text())
        self.assertEqual(f['currency'], 'GBP')
        o, s = f['observations'], f['scenarios']
        fixed, hourly, cost, labour = map(number, [s['fixed_fee'], s['hourly_price'], o['other_direct_cost_per_job'], o['labour_value_per_hour']])
        actual = [(h, fixed, fixed - labour*h - cost, hourly*h, hourly*h - labour*h - cost) for h in map(number, o['past_job_hours'])]
        self.assertEqual(actual, [(2, 120, 50, 80, 10), (3, 120, 20, 120, 20), (5, 120, -40, 200, 40)])
        self.assertEqual(Fraction(fixed - cost) / Fraction(labour), Fraction(11, 3))
        self.assertEqual(f['unknowns'], ['Willingness to pay under either new structure', 'Frequency of each workload at future volume'])

    def test_e12_cash_trough_and_conditional_deposit(self):
        f = json.loads((ROOT / 'examples/level-04/E12/input.json').read_text())
        before = deepcopy(f)
        self.assertEqual(f['currency'], 'GBP')
        baseline = cash_schedule(f, f['observations']['accepted_orders'], Decimal(0))
        conditional = cash_schedule(f, f['observations']['accepted_orders'], number(f['scenarios']['deposit_each_if_agreed_day_0']))
        reduced = cash_schedule(f, f['scenarios']['reduced_orders'], Decimal(0))
        self.assertEqual(baseline, [('opening', 3000), ('day_0', -1800), ('day_14', -2600), ('day_30', -3200), ('day_45', 4800)])
        self.assertEqual(conditional, [('opening', 3000), ('day_0', 1900), ('day_14', 1100), ('day_30', 500), ('day_45', 4800)])
        self.assertEqual(reduced, [('opening', 3000), ('day_0', 600), ('day_14', 200), ('day_30', -400), ('day_45', 3600)])
        self.assertEqual(min(x[1] for x in conditional), number(f['observations']['cash_floor']))
        self.assertEqual(baseline[-1][1], conditional[-1][1])
        self.assertEqual(f, before)

    def test_invalid_missing_and_nonfinite_numbers(self):
        for value in (None, True, 20, 3.2, '', 'NaN', '-Infinity', 'not a number'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                number(value)
        self.assertEqual(number('-40'), Decimal(-40))

    def test_zero_denominator_is_not_zero_performance(self):
        self.assertEqual(ratio(Decimal(0), Decimal(0)), {'state': 'UNDEFINED', 'count': Decimal(0), 'reason': 'zero denominator'})
        self.assertEqual(ratio(Decimal(2), Decimal(10)), {'state': 'DEFINED', 'value': Decimal('0.2')})


class SubjectIntegrityControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        corpus = json.loads((ROOT / 'docs/research-logs/2026-09-12-stage-17-case-contracts.json').read_text())
        cls.accepted = corpus['primary_cases'][0]
        cls.prompt = cls.accepted['exact_prompt']
        cls.facts = facts_from_prompt(cls.prompt)

    def test_appended_oracle_is_detected(self):
        contaminated = self.prompt + '\nReference findings: ' + self.accepted['reference_findings']
        self.assertFalse(subject_matches(contaminated, self.facts, self.accepted))

    def test_changed_business_fact_is_detected(self):
        changed = deepcopy(self.facts)
        changed['scenarios']['fixed_fee'] = '200'
        self.assertFalse(subject_matches(self.prompt, changed, self.accepted))

    def test_missing_or_duplicate_facts_are_rejected(self):
        for prompt in ('Task: invent a price', self.prompt + '\nFacts (JSON): {}', self.prompt.split('Task:', 1)[0]):
            with self.subTest(prompt=prompt[:40]), self.assertRaises(ValueError):
                facts_from_prompt(prompt)

    def test_complete_input_has_no_extra_fact_dependency(self):
        for case in json.loads((ROOT / 'docs/research-logs/2026-09-12-stage-17-case-contracts.json').read_text())['primary_cases']:
            with self.subTest(case=case['id']):
                directory = ROOT / f'examples/level-{case["level"]:02d}' / case['id']
                self.assertTrue(subject_matches((directory/'prompt.txt').read_text(), json.loads((directory/'input.json').read_text()), case))


if __name__ == '__main__':
    unittest.main()
