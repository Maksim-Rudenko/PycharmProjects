def change(money):
    '''Нужно разменять заданное количество денег номиналами монет 1, 4, 3'''

    money_list = [0] * money
    coins_list = [0] * money
    for i in range(money):
        if i == 2:
            money_list[i] = 3
            coins_list[i] = 1

        elif i == 3:
            money_list[i] = 4
            coins_list[i] = 1

        elif (i + 1) - 4 in money_list and ((i + 1) % 3 != 0 or
                                            (i + 1) / 4 < (i + 1) / 3 and i % 2 == 1 and (i + 1) % 4 == 0):
            # если есть число на 4 меньше и рассматриваемое не
            # кратно 3, то прибавляем 4 и получаем число ( + 1 монета)
            money_list[i] = money_list[i - 4] + 4
            coins_list[i] = coins_list[i - 4] + 1

        elif (i + 1) - 3 in money_list:
            # если есть число на 3 меньше, то прибавляем 3 и получаем число ( + 1 монета)
            money_list[i] = money_list[i - 3] + 3
            coins_list[i] = coins_list[i - 3] + 1

        else:
            money_list[i] = money_list[i - 1] + 1
            coins_list[i] = coins_list[i - 1] + 1
    #print(money_list)
    #print(coins_list)

    return coins_list[money - 1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))