from typing import List, NamedTuple

from parsing import parse
from equations import sums


class Result(NamedTuple):
    N: int
    missing: int


def find_missing(fname: str) -> List[Result]:
    '''
    find_missing scans through a text file containing pairs of lines of alternating:
    1) annotations of a number N which states the quantity of numbers (save for one missing) in the sequence which follows
    2) the sequence of numbers, randomly ordered, potentially broken across multiple lines. One number is missing.

    The missing number is found by first calculating the sum of all numbers [1..N]
    and then successively subtracting each existing number in the sequence, leaving
    only the remainder which is equal to the missing number.

    This algorithm is optimized for memory and processing efficiency. It assumes that the sequences
    can approach the gigabyte range, so reads the text file line by line and does not persist any further data
    to memory, performing the operation in O(N) time where N is the number of lines in text file.

    It makes a further assumption that there is only a single number missing from the sequence set 
    and that no numbers are repeated.
    '''

    N = -1
    accumulator = 0
    results = []

    with open(fname, 'r') as f:
        for line_data in parse.sequences(f):
            if line_data.new_start:
                if N != -1:
                    results.append(Result(N=N, missing=accumulator))
                N = line_data.N
                accumulator = sums.nums_to(N)
            else:
                for n in line_data.sequence:
                    accumulator -= n

    return results