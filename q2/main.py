import argparse

from typing import List

from parsing import parse
from search import find


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Determine metabolite and adduct from mass spectrometry signal data')
    parser.add_argument('fnamein', type=str, help='Path to file with mass spectrometry data')
    parser.add_argument('fnameout', type=str, help='Path to file to write results to')
    args = parser.parse_args()

    results: List[find.Result] = []

    with open(args.fnamein, 'r') as f:
        for data in parse.mass_spec_data(f):
            matches = find.optimal_matches(data)
            results.extend(matches)

    with open(args.fnameout, 'w') as f:
        for result in results:
            f.write(f'{result.met_idx} {result.adc_idx}\n')