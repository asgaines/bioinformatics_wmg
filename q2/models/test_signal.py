from ast import Add
from re import M
import unittest

from decimal import Decimal
from models.specdata import Adduct, Metabolite, Signal


class TestSignalCalcNoise(unittest.TestCase):

    def test_edge_case_where_float_fails(self):
        # Using floats for holding data can lead to precision edge cases
        # e.g.: 0.3 - 0.2 - 0.1 == -2.7755575615628914e-17
        # when it should lead to 0.0
        # Using Decimal calculations circumvents this precision error
        expected = Decimal('0')

        signal = Signal(idx=1, data=Decimal('0.3'))
        metabolite = Metabolite(idx=1, data=Decimal('0.2'))
        adduct = Adduct(idx=1, data=Decimal('0.1'))

        got = signal.calc_noise(metabolite, adduct)

        self.assertEqual(expected, got)