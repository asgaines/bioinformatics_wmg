def nums_to(N: int) -> int:
    '''
    sum_nums_to returns the sum of all positive numbers from 1 to N, inclusive
    for example:
        N: 3
        returns 1 + 2 + 3 = 6
    N must be a positive number
    '''
    if N < 0:
        raise ValueError('N argument must be positive')

    return int(((N + 1) * N) / 2)