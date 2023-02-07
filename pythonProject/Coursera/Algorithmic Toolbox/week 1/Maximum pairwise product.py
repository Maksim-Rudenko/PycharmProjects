'''Программа для нахождения максимального произведения 2-х чисел'''

'''def max_pairwise_product(numbers):
    Просматривает все пары произведений, сравнивает и возвращает максимум
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product'''

def max_pairwise_product_light(numbers):
    '''Ищет 2 максимальных числа из приведенных и возвращает их произведение'''
    n = len(numbers)
    max_number_1 = max(numbers)
    numbers.remove(max_number_1)
    max_number_2 = max(numbers)
    return max_number_1 * max_number_2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    #print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_light(input_numbers))