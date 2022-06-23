from typing import Generator, List, NamedTuple, TextIO


class LineData(NamedTuple):
    N: int
    sequence: List[int]
    new_start: bool


def sequences(fobj: TextIO) -> Generator[LineData, None, None]:
    '''
    sequences takes a file-like object and reads data line by line to keep memory footprint small.
    It providing a generator that yields:
    1) annotation integer (N), an integer parsed from the `>{N}` annotation lines
    2) the sequence of integers corresponding to the N
    3) a boolean denoting when a new sequence is beginning:
        - True if a new N's sequences will follow
        - False if the sequence being sent over is a continuation of the previously communicated N
    '''

    for line in fobj:
        line = line.rstrip('\n')
        if line[0] == '>':
            N = int(line[1:])
            yield LineData(N=N, sequence=[], new_start=True)
        else:
            sequence = [int(i) for i in line.split(' ')]
            yield LineData(N=-1, sequence=sequence, new_start=False)

    yield LineData(N=0, sequence=[], new_start=True)