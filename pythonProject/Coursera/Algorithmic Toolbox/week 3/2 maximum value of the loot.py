from sys import stdin

def optimal_value(capacity, weights, values):

    unitValues_list = []

    # Создаем список цен за 1 единицу веса unitValues_list
    for i in range(len(weights)):
        unitValue = (values[i]/weights[i])
        unitValues_list.append(unitValue)

    # intake - сколько веса в сумке
    intake = 0
    max_value = 0
    factor = True

    while factor:
        max_index = unitValues_list.index(max(unitValues_list, default=0))
        # Индекс элемента с максимальной стоимостью

        if weights[max_index] <= capacity:
            # Если вмещается весь элемент, то берем его
            intake = weights[max_index]
            capacity -= weights[max_index]
            max_value += values[max_index]
        else:
            # Если все не помещается
            fraction = capacity / weights[max_index] # Доля от всего веса
            max_value += values[max_index] * fraction # Сколько получиаем за эту долю
            capacity = int(capacity - (weights[max_index] * fraction))

        weights.pop(max_index)
        values.pop(max_index)
        unitValues_list.pop(max_index)

        factor = ((len(weights) != 0) if ((capacity != 0) if True else False) else False)

    return max_value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))