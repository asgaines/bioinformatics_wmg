import argparse

from process import search


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find missing integer from sequential list')
    parser.add_argument('fname', type=str, help='Path to file with annotation/sequences of integers')
    args = parser.parse_args()

    results = search.find_missing(args.fname)
    
    for result in results:
        print(f'N={result.N} sequence missing value {result.missing}')