from sys import stdin

def min_refills(distance, tank, stops):
    '''Задано расстояние, емкость бака (сколько можно проехать на 1 баке), расстояния заправок (stops)
        Определить сколько минимально заправок нужно, чтобы проехать заданное расстояние'''
    num_refill, curr_refill, limit = 0, 0, tank
    while limit < distance:  # While the destination cannot be reached with current fuel
        if curr_refill >= len(stops) or stops[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < len(stops) - 1 and stops[curr_refill + 1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = stops[curr_refill] + tank  # Fill up the tank
        curr_refill += 1
    return num_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))


'''Input:
500
100
4
100 200 300 400'''
