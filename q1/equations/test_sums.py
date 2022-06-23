from typing import NamedTuple
import unittest

from equations import sums


class Case(NamedTuple):
    name: str
    in_N: int
    expected: int


class TestNumsTo(unittest.TestCase):

    def test_negative_number_causes_exception(self):
        with self.assertRaises(ValueError):
            sums.nums_to(-5)

    def test_natural_numbers(self):
        cases = [
            Case(
                name='Edge case zero value',
                in_N=0,
                expected=0,
            ),
            Case(
                name='Edge case 1',
                in_N=1,
                expected=1,
            ),
            Case(
                name='Normal case 2',
                in_N=2,
                expected=3,
            ),
            Case(
                name='Normal case 3',
                in_N=3,
                expected=6,
            ),
            Case(
                name='Normal case 10',
                in_N=10,
                expected=10+9+8+7+6+5+4+3+2+1,
            ),
            Case(
                name='Normal case large number',
                in_N=1000,
                expected=500500,
            ),
        ]

        for case in cases:
            got = sums.nums_to(case.in_N)
            self.assertEqual(got, case.expected, case.name)