num_int = [8, -1, 9, -5, 1, 0, 6, -7, 1, 5]


def test(num_int):
    for i in range(0, len(num_int)):
        max_sofar = num_int[i]
        max_list = num_int[i]
        if num_int < 0:
            max_sofar = 0
        max_sofar += num_int[i]
        if max_sofar > max_list:
            max_list = max_sofar
        return max_list
