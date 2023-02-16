import numpy as np

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    # Глобальные данные, чтобы использовать в других методах
    global m, M, op

    # Списки чисел и знаков соответсвенно
    d = []
    op = []
    i = 0
    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while i < len(dataset):
        s = ''
        if dataset[i] in integers:
            while i < len(dataset) and dataset[i] in integers:
                s += dataset[i]
                i += 1
            d.append(int(s))
        else:
            op.append(dataset[i])
            i += 1

    n = len(d)
    # n - количество чисел в выражении
    # 2 таблицы: минимальных и максимальных значений
    m = np.zeros((n, n), dtype=int)
    M = np.zeros((n, n), dtype=int)

    # Основной цикл, который заполняет таблицу данных (макс и миним значений)
    for i in range(n):
        m[i, i] = d[i]
        M[i, i] = d[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i, j], M[i, j] = min_and_max(i, j)

    return M[0, n - 1]


def min_and_max(i, j):

    min_value = 99999999
    max_value = -99999999

    for k in range(i, j):

        a = evaluate(M[i, k], M[k + 1, j], op[k])
        b = evaluate(M[i, k], m[k + 1, j], op[k])
        c = evaluate(m[i, k], M[k + 1, j], op[k])
        d = evaluate(m[i, k], m[k + 1, j], op[k])

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return (min_value, max_value)



if __name__ == "__main__":
    print(maximum_value(input()))

