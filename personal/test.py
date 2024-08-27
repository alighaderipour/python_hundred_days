def pyramid(stones):
    seto = set(stones)
    top_three = sorted(seto)[-3:]
    for i in top_three:
        if i == 1:
            return None
    else:
        return 3 * top_three[0] + 2 * top_three[1] + top_three[2]


print(pyramid([7, 5, 3, 5, 3, 0, 0, -1, 0, 0, 3, 3, 3]))
