def fibonacci_last_digit(n):
    '''Вместо того, чтобы считать число Фибоначчи полностью, считаем только последнюю цифру'''
    fib_1 = 0
    fib_2 = 1
    for i in range(2, n + 1):
        fib_1, fib_2 = fib_2 % 10, (fib_1 + fib_2) % 10

    return fib_2 if n > 0 else fib_1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
