import time


def binary_search(keys, query):
    '''Дано 2 массива keys - массив чисел где мы ищем; query - массив чисел, по порядку все из которых
        мы должны найти в массиве keys и вывести их индексы, если нет, то -1'''
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
            return mid
        elif mid == low and query == keys[high]:
            return high
        else:
            if query < keys[mid]:
                high = mid
                mid = int((low + high) / 2)
                # print('mid', mid)
                # time.sleep(2)
            else:
                low = mid
                mid = int((low + high) / 2)
                #print('mid', mid, 'low', low, 'high', high)
                #time.sleep(2)



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        # Цикл по которому мы доджны найти число q из input_queries (query) в input_keys (keys)
        print(binary_search(input_keys, q), end=' ')


'''
5
1 5 8 12 13
5
8 1 23 1 11

7
1 5 8 10 12 13 14
1
1
'''