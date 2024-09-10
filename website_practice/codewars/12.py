"""
if win 3 point
if draw 1 point
loss 0 point

"""


def points(games):
    score = 0
    for item in range(len(games)):
        if games[item][0] > games[item][2]:
            score += 3
        elif games[item][0] == games[item][2]:
            score += 1
        else:
            score += 0
    return score


def points2(games):
    return sum((x >= y) + 2 * (x > y) for x, y in (item.split(":") for item in games))


print(points(["1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"]))
print(points2(["1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"]))


"""
points = (x >= y) + 2 * (x > y)
if win 1 + 2*1 = 3
if draw 1 + 2*0 = 1
if loss 0 + 2*0 = 0
"""
