import unittest

from decimal import Decimal
from typing import List, NamedTuple

from models.specdata import Adduct, MassSpecData, Metabolite, Run, Signal
from search import find


class TestFindOptimalMatches(unittest.TestCase):

    def test_single_metabolite_and_adduct_only_possible_result(self):
        expected = [
            find.Result(
                noise=Decimal('1.0'),
                met_idx=1,
                adc_idx=1,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('1.0')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('0.5')
                ),
            ],
            signals=[
                Signal(
                    idx=1,
                    data=Decimal('2.5'),
                ),
            ],
            run=Run(1, 1),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)

    def test_toy_results_set_1(self):
        expected = [
            find.Result(
                noise=Decimal('0.000001'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000001'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.499998'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.500001'),
                met_idx=1,
                adc_idx=2,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('1.000002')
                ),
                Metabolite(
                    idx=2,
                    data=Decimal('0.000002')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('0.500000')
                ),
                Adduct(
                    idx=2,
                    data=Decimal('-0.500000')
                ),
            ],
            signals=[
                Signal(
                    idx=1,
                    data=Decimal('0.500001'),
                ),
                Signal(
                    idx=2,
                    data=Decimal('0.500002'),
                ),
                Signal(
                    idx=3,
                    data=Decimal('0.500003'),
                ),
                Signal(
                    idx=4,
                    data=Decimal('1.000000'),
                ),
                Signal(
                    idx=5,
                    data=Decimal('0.000001'),
                ),
            ],
            run=Run(1, 3),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)

    def test_toy_results_set_2(self):
        expected = [
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=2,
                adc_idx=1,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000001'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.499998'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.500000'),
                met_idx=2,
                adc_idx=1,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('1.000002')
                ),
                Metabolite(
                    idx=2,
                    data=Decimal('0.000001')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('0.500000')
                ),
                Adduct(
                    idx=2,
                    data=Decimal('-0.500000')
                ),
            ],
            signals=[
                Signal(
                    idx=1,
                    data=Decimal('0.500001'),
                ),
                Signal(
                    idx=2,
                    data=Decimal('0.500002'),
                ),
                Signal(
                    idx=3,
                    data=Decimal('0.500003'),
                ),
                Signal(
                    idx=4,
                    data=Decimal('1.000000'),
                ),
                Signal(
                    idx=5,
                    data=Decimal('0.000001'),
                ),
            ],
            run=Run(2, 3),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)

    def test_toy_results_set_3(self):
        expected = [
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=2,
                adc_idx=4,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=3,
            ),
            find.Result(
                noise=Decimal('0.000085'),
                met_idx=5,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=1,
            ),
            find.Result(
                noise=Decimal('0.000005'),
                met_idx=5,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000001'),
                met_idx=1,
                adc_idx=2,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=1,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('0.000001')
                ),
                Metabolite(
                    idx=2,
                    data=Decimal('0.000002')
                ),
                Metabolite(
                    idx=3,
                    data=Decimal('0.000003')
                ),
                Metabolite(
                    idx=4,
                    data=Decimal('0.000004')
                ),
                Metabolite(
                    idx=5,
                    data=Decimal('0.000005')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('0.000002')
                ),
                Adduct(
                    idx=2,
                    data=Decimal('0.000010')
                ),
                Adduct(
                    idx=3,
                    data=Decimal('0.000001')
                ),
                Adduct(
                    idx=4,
                    data=Decimal('-0.000001')
                ),
            ],
            signals=[
                Signal(
                    idx=1,
                    data=Decimal('0.000001'),
                ),
                Signal(
                    idx=2,
                    data=Decimal('0.000002'),
                ),
                Signal(
                    idx=3,
                    data=Decimal('0.000100'),
                ),
                Signal(
                    idx=4,
                    data=Decimal('0.000005'),
                ),
                Signal(
                    idx=5,
                    data=Decimal('0.000020'),
                ),
                Signal(
                    idx=6,
                    data=Decimal('0.000010'),
                ),
                Signal(
                    idx=7,
                    data=Decimal('0.000003'),
                ),
            ],
            run=Run(3, 3),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)

    def test_deduplicated_values_and_cache_hit(self):
        expected = [
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=1,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=1,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=1,
                adc_idx=1,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=4,
                adc_idx=4,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('1.500000')
                ),
                Metabolite(
                    idx=2,
                    data=Decimal('1.500000')  # Duplicate of above
                ),
                Metabolite(
                    idx=3,
                    data=Decimal('1.500000')  # Second duplicate of above
                ),
                Metabolite(
                    idx=4,
                    data=Decimal('10.500000')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('-0.500000')
                ),
                Adduct(
                    idx=2,
                    data=Decimal('-0.500000')  # Duplicate of above
                ),
                Adduct(
                    idx=3,
                    data=Decimal('-0.500000')  # Second duplicate of above
                ),
                Adduct(
                    idx=4,
                    data=Decimal('0.500000')
                ),
            ],
            signals=[
                Signal(
                    idx=1,
                    data=Decimal('1.000000'),
                ),
                Signal(
                    idx=2,
                    data=Decimal('1.000000'),  # Duplicate of above: cache hit
                ),
                Signal(
                    idx=3,
                    data=Decimal('1.000000'),  # Second duplicate of above: cache hit
                ),
                Signal(
                    idx=4,
                    data=Decimal('11.000000'),
                ),
            ],
            run=Run(1, 1),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)

    def test_signal_cache_hits(self):
        expected = [
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=3,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=3,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=3,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=3,
            ),
            find.Result(
                noise=Decimal('0.000000'),
                met_idx=3,
                adc_idx=3,
            ),
        ]

        data = MassSpecData(
            metabolites=[
                Metabolite(
                    idx=1,
                    data=Decimal('0.500000')
                ),
                Metabolite(
                    idx=2,
                    data=Decimal('0.200000')
                ),
                Metabolite(
                    idx=3,
                    data=Decimal('25.000000')
                ),
            ],
            adducts=[
                Adduct(
                    idx=1,
                    data=Decimal('-0.500000')
                ),
                Adduct(
                    idx=2,
                    data=Decimal('0.500000')
                ),
                Adduct(
                    idx=3,
                    data=Decimal('-5.000000')
                ),
            ],
            signals=[
                # This first signal processed will trigger a calculation, the following ones
                # should all result in a cache hit since they have the same signal value
                Signal(
                    idx=1,
                    data=Decimal('20.000000'),
                ),
                Signal(
                    idx=2,
                    data=Decimal('20.000000'),
                ),
                Signal(
                    idx=3,
                    data=Decimal('20.000000'),
                ),
                Signal(
                    idx=4,
                    data=Decimal('20.000000'),
                ),
                Signal(
                    idx=5,
                    data=Decimal('20.000000'),
                ),
            ],
            run=Run(1, 1),
        )

        got = find.optimal_matches(data)

        self.assertEqual(expected, got)


class TestFindDeduplicate(unittest.TestCase):

    def test_nothing_to_deduplicate(self):
        class Case(NamedTuple):
            database: List[Metabolite] | List[Adduct]
            expected: List[Metabolite] | List[Adduct]


        cases = [
            Case(
                database=[
                    Metabolite(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                ],
                expected=[
                    Metabolite(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                ],
            ),
            Case(
                database=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                ],
                expected=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                ],
            ),
            Case(
                database=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                    Adduct(
                        idx=2,
                        data=Decimal('0.000002'),
                    ),
                ],
                expected=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                    Adduct(
                        idx=2,
                        data=Decimal('0.000002'),
                    ),
                ],
            ),
        ]

        for c in cases:
            got = find.deduplicate(c.database)
            self.assertEqual(got, c.expected)

    def test_duplicates_removed_based_on_data_value(self):
        class Case(NamedTuple):
            database: List[Metabolite] | List[Adduct]
            expected: List[Metabolite] | List[Adduct]


        cases = [
            Case(
                database=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                    Adduct(
                        idx=2,
                        data=Decimal('0.000001'),
                    ),
                ],
                expected=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                ],
            ),
            Case(
                database=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                    Adduct(
                        idx=1, # Same index as above. Not valid, but demonstrates dedupe on data
                        data=Decimal('0.000002'),
                    ),
                ],
                expected=[
                    Adduct(
                        idx=1,
                        data=Decimal('0.000001'),
                    ),
                    Adduct(
                        idx=1,
                        data=Decimal('0.000002'),
                    ),
                ],
            ),
        ]

        for c in cases:
            got = find.deduplicate(c.database)
            self.assertEqual(got, c.expected)