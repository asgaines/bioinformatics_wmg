import io
import unittest

from decimal import Decimal

from parsing import parse
from models.specdata import Adduct, MassSpecData, Metabolite, Signal, Run


class TestParseMassSpecData(unittest.TestCase):

    def test_zero_test_results_returns_nothing(self):
        expected = []

        with io.StringIO() as f:
            # Num test results
            f.write('0\n')
            f.seek(0)

            got = list(parse.mass_spec_data(f))

        self.assertEqual(expected, got)

    def test_incorrect_dataset_size_descriptor_violates_assertion(self):
        with io.StringIO() as f:
            # Num test results
            f.write('1\n')
            # M, K, N
            f.write('2 1 1\n')
            # Metabolites
            f.write('0.01\n') # Note there is only one element here, violating M = 2
            # Adducts
            f.write('0.04\n')
            # Signals
            f.write('0.07\n')

            f.seek(0)

            with self.assertRaises(AssertionError):
                list(parse.mass_spec_data(f))

    def test_single_small_test_result(self):
        expected = [
            MassSpecData(
                metabolites=[
                    Metabolite(idx=1, data=Decimal('0.01')),
                    Metabolite(idx=2, data=Decimal('0.02')),
                    Metabolite(idx=3, data=Decimal('0.03')),
                ],
                adducts=[
                    Adduct(idx=1, data=Decimal('0.04')),
                    Adduct(idx=2, data=Decimal('0.05')),
                    Adduct(idx=3, data=Decimal('0.06')),
                ],
                signals=[
                    Signal(idx=1, data=Decimal('0.07')),
                    Signal(idx=2, data=Decimal('0.08')),
                    Signal(idx=3, data=Decimal('0.09')),
                ],
                run=Run(1, 1),
            ),
        ]

        with io.StringIO() as f:
            # Num test results
            f.write('1\n')
            # M, K, N
            f.write('3 3 3\n')
            # Metabolites
            f.write('0.01 0.02 0.03\n')
            # Adducts
            f.write('0.04 0.05 0.06\n')
            # Signals
            f.write('0.07 0.08 0.09\n')

            f.seek(0)

            got = list(parse.mass_spec_data(f))

        self.assertEqual(expected, got)

    def test_two_small_test_results(self):
        expected = [
            MassSpecData(
                metabolites=[
                    Metabolite(idx=1, data=Decimal('0.01')),
                    Metabolite(idx=2, data=Decimal('0.02')),
                    Metabolite(idx=3, data=Decimal('0.03')),
                ],
                adducts=[
                    Adduct(idx=1, data=Decimal('0.04')),
                    Adduct(idx=2, data=Decimal('0.05')),
                    Adduct(idx=3, data=Decimal('0.06')),
                ],
                signals=[
                    Signal(idx=1, data=Decimal('0.07')),
                    Signal(idx=2, data=Decimal('0.08')),
                    Signal(idx=3, data=Decimal('0.09')),
                ],
                run=Run(1, 2),
            ),
            MassSpecData(
                metabolites=[
                    Metabolite(idx=1, data=Decimal('0.11')),
                ],
                adducts=[
                    Adduct(idx=1, data=Decimal('0.12')),
                    Adduct(idx=2, data=Decimal('0.13')),
                ],
                signals=[
                    Signal(idx=1, data=Decimal('0.14')),
                    Signal(idx=2, data=Decimal('0.15')),
                    Signal(idx=3, data=Decimal('0.16')),
                ],
                run=Run(2, 2),
            ),
        ]

        with io.StringIO() as f:
            # Num test results
            f.write('2\n')

            # M, K, N
            f.write('3 3 3\n')
            # Metabolites
            f.write('0.01 0.02 0.03\n')
            # Adducts
            f.write('0.04 0.05 0.06\n')
            # Signals
            f.write('0.07 0.08 0.09\n')

            # M, K, N
            f.write('1 2 3\n')
            # Metabolites
            f.write('0.11\n')
            # Adducts
            f.write('0.12 0.13\n')
            # Signals
            f.write('0.14 0.15 0.16\n')

            f.seek(0)

            got = list(parse.mass_spec_data(f))

        self.assertEqual(expected, got)