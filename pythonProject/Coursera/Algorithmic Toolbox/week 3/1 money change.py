def change(money):
    '''Задается количество денег, вывести минимальное количество монет номиналом 1, 5, 10,
    чтобы покрыть заданное количество денег'''
    coin_value_1 = 0
    coin_value_5 = 0
    coin_value_10 = 0
    while money != 0:
        if money >= 10:
            coin_value_10 += 1
            money -= 10
        elif money >= 5:
            coin_value_5 += 1
            money -= 5
        else:
            coin_value_1 += money
            money = 0

    return coin_value_1 + coin_value_5 + coin_value_10


if __name__ == '__main__':
    m = int(input())
    print(change(m))
