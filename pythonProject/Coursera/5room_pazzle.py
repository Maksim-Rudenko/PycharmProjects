import random

# 5 комнат объединены дверями (списки номеров дверей)
room_1 = [1, 2, 5, 6, 7]
room_2 = [3, 4, 6, 8, 9]
room_3 = [5, 10, 11, 14]
room_4 = [7, 8, 11, 12, 15]
room_5 = [9, 12, 13, 16]
apartament = [room_1, room_2, room_3, room_4, room_5]

out_apart_check = [[1, 2], [3, 4], [13, 16], [10, 14]]
in_apart_check = [[1, 10], [14, 15], [15, 16], [4, 13], [2, 3]]

# двери, ведущие наружу
out_doors = [1, 2, 3, 4, 10, 13, 14, 15, 16]
out_doors_check = [1, 2, 3, 4, 10, 13, 14, 15, 16]
# результат - последовательность выбора дверей (прохода через двери)
result = []


def find_next_room(door, start_room):
    '''Находит следующую комнату, в которую идем'''
    for room in apartament:
        if door in room and room != start_room:
            return room
    else:
        return []


def find_enter_room(enter_door):
    '''Находит комнату, в которую заходят по двери'''
    for room in apartament:
        if enter_door in room:
            return room
    else:
        return []


def out_apartment_check(first, second, third):
    check = 0
    for out in out_apart_check:
        if out == [second, third] or out == [third, second]:
            check += 1
    if first in out_doors_check:
        check += 1
    # если 2, то мы снаружи
    return check == 2


def delete_door(door):
    '''Удаляет (закрыавем) дверь в комнате'''
    for room_num in apartament:
        # удаляем дверь, через которую прошли, из комнат, где она есть
        if door in room_num:
            room_num.remove(door)

    if door in out_doors:
        # удаляем дверь из списка внешних, чтобы потом не войти в нее
        out_doors.remove(door)




def go_out_the_room():
    random_start = random.randint(0, 1)
    start_out_enter = False
    if random_start == 0:
        # начинаем движение находясь изначально в комнате
        next_room = apartament[random.randint(0, len(apartament) - 1)]
        print('start room:', next_room)
        next_door = next_room[random.randint(0, len(next_room) - 1)]
        print('start door:', next_door)
    else:
        start_out_enter = True
        # начинаем снаружи (заходим в дверь, закрываем ее, определяем комнату и входим)
        next_door = out_doors[random.randint(0, len(out_doors) - 1)]
        print('start enter door:', next_door)
        next_room = find_enter_room(next_door)
        result.append(next_door)
        delete_door(next_door)
        next_door = next_room[random.randint(0, len(next_room) - 1)]
        print('start room:', next_room)
        print('start door:', next_door)

    while len(room_5) + len(room_4) + len(room_3) + len(room_2) + len(room_1) > 0:

        # записываем дверь, через которую прошли в результат (путь)
        result.append(next_door)

        if next_door not in out_doors_check:
            # если дверь ведет во внутрь
            next_room = find_next_room(next_door, next_room)
            #print('1next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            #print('1next door:', next_door)
            continue

        if next_door in out_doors_check and len(result) == 2 and \
                result[-2] in out_doors_check and start_out_enter == True:
            # если вышли наружу
            # выбираем рандомную дверь, чтобы войти
            delete_door(next_door)
            if len(out_doors) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = out_doors[random.randint(0, len(out_doors) - 1)]
            # print('4enter door:', next_door)
            # находим комнату, в которую ведет это дверь
            result.append(next_door)
            next_room = find_enter_room(next_door)
            # print('4next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            # print('4next door:', next_door)
            continue

        if next_door in out_doors_check and len(result) == 2 and \
                result[-2] in out_doors_check and start_out_enter == False:
            # если снаружи входим во внутрь
            next_room = find_next_room(next_door, next_room)
            #print('3next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            #print('3next door:', next_door)
            continue

        if next_door in out_doors_check and len(result) > 2 and \
                result[-2] in out_doors_check and out_apartment_check(result[-3], result[-2], result[-1]):
            # если вышли наружу
            # выбираем рандомную дверь, чтобы войти
            delete_door(next_door)
            if len(out_doors) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = out_doors[random.randint(0, len(out_doors) - 1)]
            # print('4enter door:', next_door)
            # находим комнату, в которую ведет это дверь
            result.append(next_door)
            next_room = find_enter_room(next_door)
            # print('4next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            # print('4next door:', next_door)
            continue

        if next_door in out_doors_check and len(result) > 1 and \
                result[-2] in out_doors_check and not out_apartment_check(result[-3], result[-2], result[-1]):
            # если снаружи входим во внутрь
            next_room = find_next_room(next_door, next_room)
            #print('5next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            #print('5next door:', next_door)
            continue

        if (len(result) == 1 and next_door in out_doors_check) or \
                (len(result) > 1 and next_door in out_doors_check and result[-2] not in out_doors_check):
            # если вышли наружу
            # выбираем рандомную дверь, чтобы войти
            delete_door(next_door)
            if len(out_doors) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = out_doors[random.randint(0, len(out_doors) - 1)]
            #print('6enter door:', next_door)
            # находим комнату, в которую ведет это дверь
            result.append(next_door)
            next_room = find_enter_room(next_door)
            #print('6next room:', next_room)
            delete_door(next_door)
            if len(next_room) == 0 and len(result) != 16:
                print('тупик...', len(result), 'из 16')
                return result
            next_door = next_room[random.randint(0, len(next_room) - 1)]
            #print('6next door:', next_door)
            continue

    print('Успех!')
    return result


if __name__ == "__main__":
    print(go_out_the_room())
