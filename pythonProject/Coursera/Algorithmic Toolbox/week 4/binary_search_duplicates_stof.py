def find_first_index(A, low, high, key):
    if A[low] == key:
        return low
    if low == high:
        return -1
    mid = low + (high - low) // 2
    if A[mid] >= key:
        return find_first_index(A, low, mid, key)
    return find_first_index(A, mid + 1, high, key)


def binary_search(keys, number):
    return find_first_index(keys, 0, len(keys) - 1, number)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')