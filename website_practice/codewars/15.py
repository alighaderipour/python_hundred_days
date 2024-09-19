"""

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


<<<<<<< HEAD
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
=======
def array_diff(a, b):

    for i in range(len(b)):
        for item in range(len(a)):
            if b[i] in a:
                a.remove(b[i])
    return a


def array_diff(a, b):
    return [x for x in a if x not in b]
>>>>>>> 910f4884b2b29cb87adf9bbdea418055300e3639
