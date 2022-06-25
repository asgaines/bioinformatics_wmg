from typing import NamedTuple, List
from decimal import Decimal


class Metabolite(NamedTuple):
    # idx is the index of the metabolite in the M database, 1-indexed
    idx: int
    data: Decimal


class Adduct(NamedTuple):
    # idx is the index of the adduct in the K database, 1-indexed
    idx: int
    data: Decimal


class Signal(NamedTuple):
    # idx is the index of the signal in the N database, 1-indexed
    idx: int
    data: Decimal

    def calc_noise(self, metabolite: Metabolite, adduct: Adduct) -> Decimal:
        return abs(self.data - metabolite.data - adduct.data)


class Run(NamedTuple):
    n: int
    total: int


class MassSpecData(NamedTuple):
    metabolites: List[Metabolite]
    adducts: List[Adduct]
    signals: List[Signal]
    run: Run
