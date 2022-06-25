from typing import Dict, List, NamedTuple
from decimal import Decimal
from progress.bar import Bar

from models.specdata import MassSpecData, Metabolite, Adduct, Signal
from models.tree import Tree


class Result(NamedTuple):
    noise: Decimal
    met_idx: int
    adc_idx: int


def optimal_matches(data: MassSpecData) -> List[Result]:
    results: List[Result] = []
    # Store results of calculations in case of duplicate identical signals
    signal_cache: Dict[Decimal, Result] = {}

    # Remove duplicates since any of matching metabolites/adducts are fair game
    metabolites = deduplicate(data.metabolites)
    adducts = deduplicate(data.adducts)

    tree: Tree
    smaller_db = []

    # Optimize choice of binary tree based on relative size of databases
    if len(metabolites) > len(adducts):
        tree = Tree(metabolites)
        smaller_db = adducts
    else:
        tree = Tree(adducts)
        smaller_db = metabolites
    
    bar = Bar(f'Processing ({data.run.n}/{data.run.total})', max=len(data.signals))

    for signal in data.signals:
        bar.next()

        cached_result = signal_cache.get(signal.data, None)
        if cached_result is not None:
            # Cache hit, return previously calculated result
            results.append(cached_result)
            continue

        result = find_lowest_noise(signal, smaller_db, tree)
        results.append(result)

        # Add result to cache for potential future hits
        signal_cache[signal.data] = result
    
    bar.finish()
    
    return results


def find_lowest_noise(signal: Signal, entries: List[Metabolite] | List[Adduct], tree: Tree) -> Result:
    lowest = Result(noise=Decimal('Inf'), met_idx=0, adc_idx=0)
    iter_metabolite = type(entries[0]) == Metabolite

    for entry in entries:
        target = signal.data - entry.data

        closest = tree.find(target)
        if closest.data + entry.data < 0:
            continue

        if closest.data == target:
            return Result(
                noise=Decimal('0.000000'),
                met_idx=entry.idx if iter_metabolite else closest.idx,
                adc_idx=closest.idx if iter_metabolite else entry.idx,
            )

        noise = signal.calc_noise(closest, entry)
        if noise < lowest.noise:
            lowest = Result(
                noise=noise,
                met_idx=entry.idx if iter_metabolite else closest.idx,
                adc_idx=closest.idx if iter_metabolite else entry.idx,
            )

    return lowest
        


def deduplicate(database: List[Metabolite] | List[Adduct]) -> List[Metabolite] | List[Adduct]:
    deduped: Dict[Decimal, Metabolite | Adduct] = {}

    for entry in database:
        if entry.data not in deduped:
            deduped[entry.data] = entry

    return list(deduped.values())