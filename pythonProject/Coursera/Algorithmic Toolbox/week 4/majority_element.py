def majority_element_naive(elements):
    '''majority element - это элемент количество вхождений которого больше половины длины массива'''

    # разделяй и властвуй - разделить массив на 2 и посмотреть там маржинальный элемент
    # Вот как нужно сделать
    '''https://www.youtube.com/watch?v=28D-VLSXBt0&ab_channel=DeepCoding'''


    return divine_majority_elements(elements, 0, len(elements) - 1)

def divine_majority_elements(arr, low, high):
    if len(arr) == 1:
        return 1
    mid = int((high + low) / 2)

def get_majority_element(a, left, right):
    # check array on zero elements
    if left == right:
        return -1

    # check array on only one element
    if left + 1 == right:
        return a[left]

    # sort the array to get n*log(n) complexity
    a.sort()

    # initialize counters
    cur_elem = a[0]
    cur_cnt = 1
    max_elem = a[0]
    max_cnt = 1

    # iterate through sorted array
    for i in range(1, right):
        if a[i] == cur_elem:
            cur_cnt += 1
        else:
            if cur_cnt > max_cnt:
                max_elem = cur_elem
                max_cnt = cur_cnt
            cur_elem = a[i]
            cur_cnt = 1

    # last element check
    if cur_cnt > max_cnt:
        max_elem = cur_elem
        max_cnt = cur_cnt

    # print('fast:', max_elem, max_cnt, right/2)

    # check for majority
    if max_cnt > right/2:
        return max_elem

    # return -1 if no majority element
    return -1

def get_majority_element_divandconq(a, left, right):
    # last tree level
    if (right - left) == 1:
        return 1
    else:
        # split point
        mid = (left + right) // 2

        left_maj_elem = get_majority_element(a, left, mid)
        right_maj_elem = get_majority_element(a, mid+1, right)

        # define whether there is a majority element for the part of the array
        # majority elements, exclude -1
        maj_elems = (a for a in (left_maj_elem, right_maj_elem) if a != -1)
        for maj_elem in maj_elems:
            cnt = 0
            for i in range(left, right):
                if a[i] == maj_elem:
                    cnt += 1
            if cnt > (right - left) / 2:
                return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    #print(majority_element_naive(input_elements))
    print(get_majority_element_divandconq(input_elements, 0, len(input_elements)))
