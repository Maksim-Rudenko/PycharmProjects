def binary_search(keys, query):
    '''Дано 2 массива keys - массив чисел где мы ищем (с дупликатами!!! для них правильный индекс -
    первое вхождение в массив); query - массив чисел, по
    порядку все из которых мы должны найти в массиве keys и вывести их индексы, если нет, то -1'''

    #Failed case  # 54/57: time limit exceeded (Time used: 10.00/5.00, memory used: 41381888/536870912.)
    '''Из-за этого использовал решение из stackoverflow'''

    # Предположим, что массив сортирован
    low = 0  # нижняя граница рассмативаемой части массива
    high = len(keys) - 1  # верхняя граница рассмативаемой части массива
    mid = int((low + high) / 2)  # средняя граница рассмативаемой части массива
    # print(mid)

    while low < high:
        if query > keys[high] or query < keys[low] or (low == mid and
                                                       (keys[low] != query and keys[high] != query)):
            # если искомое значение больше максимального или меньше минимального в массиве
            return -1
        elif query == keys[mid]:
            if mid > 0 and keys[mid] == keys[mid - 1]:
                mid -= 1
            else:
                return mid
        elif mid == low and query == keys[high]:
            return high
        else:
            if query < keys[mid]:
                high = mid
                mid = int((low + high) / 2)

            else:
                low = mid
                mid = int((low + high) / 2)




if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')



'''
input
7
2 4 4 7 7 7 7
4
9 4 5 2

correct out
6 1 -1 0
Your output:
6 3 -1 0
'''