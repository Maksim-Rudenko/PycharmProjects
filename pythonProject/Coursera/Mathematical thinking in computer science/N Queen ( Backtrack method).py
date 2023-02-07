def can_be_extended_to_solution(perm):
    '''Проверка по диагонали. Задается массив последнего частичного решения и проверяется'''
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    '''Постепенно создается массив решения perm '''
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

extend(perm = [], n = 20)
'''Суть в том чтобы ставить королеву сразу КУДА-ТО на 1 строку(столбец), потом на 2-ю
и проверять не на одной диагонали ли они и т.д. Если решение не выходит, то удаляем последнюю королеву
и ставим ее на другое место в этой же строке (столбце). Таким образов составляется древо всех решений
до момента пока не найдется 1 правильное'''