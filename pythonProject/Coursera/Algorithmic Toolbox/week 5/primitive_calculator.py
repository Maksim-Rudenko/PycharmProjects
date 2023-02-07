#def compute_operations(n):
   # Дается значение. Операции калькулятора: +1, *2, *3. Вывести минимальное необходимое
   # число операций для получения заданного числа и массив чисел, которые получаются по ходу расчета


def optimal_sequence(n):
    '''
    Possible operation types:
    1 - multiply by 2
    2 - multiply by 3
    3 - add 1
    '''

    # n elements as we calculate number of operations starting from 1
    # elements [1, n]
    min_num_operations = [n] * n
    min_num_operations[0] = 0

    # operations array - write only last operation
    # sequence would be restored by this operations
    ops = [-1] * n

    # types of operations
    op_types = (1, 2, 3)

    # iterate from 0 till n-1
    for i in range(n-1):
        # iterate through operations
        for op_type in op_types:
            n_i = i + 1
            # multiply by 2
            if op_type == 1:
                n_new = n_i * 2
            # multiply by 3
            elif op_type == 2:
                n_new = n_i * 3
            # add 1
            elif op_type == 3:
                n_new = n_i + 1
            else:
                raise ValueError("New operation type {}".format(op_type))

            num_operations = min_num_operations[i] + 1
            i_new = n_new - 1

            # check if number of operations is less then the previous number
            if n_new <= n and num_operations < min_num_operations[i_new]:
                min_num_operations[i_new] = num_operations
                ops[i_new] = op_type

    seq = get_sequence(n, ops)

    return seq


def get_sequence(n, ops):
    '''
    Get number n from 1 in reversed order (from n to 1)
    '''
    n_seq = n
    seq = [n]
    while n_seq != 1:
        i = n_seq - 1
        op_type = ops[i]
        # multiply by 2
        if op_type == 1:
            n_seq = n_seq // 2
        # multiply by 3
        elif op_type == 2:
            n_seq = n_seq // 3
        # add 1
        elif op_type == 3:
            n_seq = n_seq - 1
        else:
            raise ValueError("New operation type {}".format(op_type))
        seq.append(n_seq)
    return seq[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = optimal_sequence(input_n)#compute_operations(input_n)
    print(len(output_sequence) - 1) # выводит число операций
    print(*output_sequence) # выводит массив чисел, получаемых по ходу расчетов от 1 до заданного