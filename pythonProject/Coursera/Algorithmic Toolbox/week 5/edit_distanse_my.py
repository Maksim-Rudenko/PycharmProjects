def edit_distance(first_string, second_string):
    '''Сравниваются 2 строки. Возвращает число необходимых удалений символов (как рациональней),
    чтобы оставить общую часть (буквально по лекции)'''

    D = [[0 for i in range(len(second_string) + 1)] for i in range(len(first_string) + 1)]

    # заполняем верхнюю строку и левый столбец

    for i in range(len(second_string) + 1):
        D[0][i] = i
    for i in range(len(first_string) + 1):
        D[i][0] = i

    for j in range(1, len(second_string) + 1):
        for i in range(1, len(first_string) + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            mismatch = D[i - 1][j - 1] + 1
            match = D[i - 1][j - 1]

            if first_string[i - 1] == second_string[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))


