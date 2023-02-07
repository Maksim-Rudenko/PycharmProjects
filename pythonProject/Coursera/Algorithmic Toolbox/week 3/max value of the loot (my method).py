from sys import stdin
# все работает, но похоже для супер больших данных плохо...
# Failed case #8/13: time limit exceeded (Time used: 6.53/5.00, memory used: 11284480/2684354560.)
def optimal_value(capacity, weights, values):

    '''Задано несколько типов предметов (каждого свое количество weights) и их цены
    (каждого values за весь weights!!!)
    Определить максимальную выгоду (забирать сразу все дорогие, потом дешевле и т.д.
    пока есть место в кармане (capacity)'''

    value = 0
    while capacity > 0:
        if weights == []:
            break
        # Создаем список с ценами за 1 значение веса и находим максимальный элемент (его индекс)
        most_value_list = [v / w for v in values for w in weights if values.index(v) == weights.index(w)]
        most_value_index = most_value_list.index(max(most_value_list))


        if capacity >= weights[most_value_index]:
            # Если вместимость больше, чем есть, то забираем все самое дорогое
            capacity -= weights[most_value_index]
            value += values[most_value_index]
            weights.pop(most_value_index)
            values.pop(most_value_index)
            most_value_list.pop(most_value_index)
        else:
            # Если вместимость меньше, чем есть, то забираем сколько можем
            value += most_value_list[most_value_index] * capacity
            capacity = 0


    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))