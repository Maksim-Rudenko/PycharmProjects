from sys import stdin

import numpy as np


def maximum_gold(capacity, weights):
    '''Заполнить рюкзак как можно больше без повторений!!!'''

    # Двумерный массив для каждого сочетания предметов (их веса)


    n = len(weights)

    value = np.zeros((n + 1, capacity + 1), dtype=int)

    for i in range(1, n + 1):
        element = weights[i - 1]
        for w in range(1, capacity + 1):
            value[i, w] = value[i - 1, w]
            if element <= w:
                val = value[i - 1, w - element] + element
                if value[i, w] < val:
                    value[i, w] = val

    return value[n, capacity]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))


'''Input:
10 3
1 4 8

Your output:
[1, 4, 8]

Correct output:
9'''