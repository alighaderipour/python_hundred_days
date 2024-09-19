"""


"""


def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


def number(stops):
    return sum(i - o for i, o in stops)


def number(arr):
    people_in = 0
    people_out = 0
    for stops in arr:
        people_in += stops[0]
        people_out += stops[1]
    return people_in - people_out
