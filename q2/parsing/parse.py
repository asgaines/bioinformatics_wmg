from decimal import Decimal
from typing import Generator, List, TextIO

from models.specdata import Metabolite, Adduct, Signal, MassSpecData, Run


def mass_spec_data(fobj: TextIO) -> Generator[MassSpecData, None, None]:
    num_cases = int(fobj.readline().rstrip())
    
    for i in range(num_cases):
        # M = number of metabolites
        # K = number of adducts
        # N = number of signals
        M, K, N = (int(n) for n in fobj.readline().rstrip().split(' '))

        metabolites = read_data_line(fobj.readline(), Metabolite)
        adducts = read_data_line(fobj.readline(), Adduct)
        signals = read_data_line(fobj.readline(), Signal)

        assert M == len(metabolites), 'M is not equal to the size of the metabolites database'
        assert K == len(adducts), 'K is not equal to the size of the adducts database'
        assert N == len(signals), 'N is not equal to the size of the signals database'

        yield MassSpecData(
            metabolites=metabolites,
            adducts=adducts,
            signals=signals,
            run=Run(n=i+1, total=num_cases),
        )


def read_data_line(line: str, cls: Metabolite | Adduct | Signal) -> List[Metabolite | Adduct | Signal]:
    return [cls(idx=i+1, data=Decimal(val)) for i, val in enumerate(line.rstrip().split(' '))]