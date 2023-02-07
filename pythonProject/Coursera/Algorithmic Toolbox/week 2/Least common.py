def lcm(a, b):
    '''НОК'''
    # Если числа делятся, то возвращаем наибольшее
    if max(a, b) % min(a, b) == 0:
        return max(a, b)
    l = 0
    # Если числа не делятся, то суммируем меньшее до НОК
    while l < a * b:
        if (l % a == 0 and l % b == 0) and l > max(a, b):
            break
        l += min(a, b)
    return l


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
