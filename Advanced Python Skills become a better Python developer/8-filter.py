"""

1- The filter() function in Python is a built-in utility that allows you to filter elements from an iterable (like lists, tuples, or sets) based on a
specified condition defined by a function. This function tests each element in the iterable and returns an iterator containing only those elements
for which the function returns True.
filter(function, iterable)
function: This is a function that tests whether each element of the iterable is true or not. If None is passed instead of a function, all elements that are considered false (like 0, None, False, etc.) will be filtered out.
iterable: This is the iterable (like a list, tuple, or set) that you want to filter.
2- Constructs an iterator that filters elements from an iterable (like lists, tuples, or sets) for which a function returns True.
3- In other words, it filters an iterable based on a condition given by a function,.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda number: number % 2 == 0, numbers)))


fruits = ["apple", "banana", "cherry", "watermelon", "cucumber"]
print(list(filter(lambda fruit: fruit.startswith("a"), fruits)))


def is_positive(num):
    return num > 0


numbers = [1, -2, 3, 4, -5, 6, 7, -8, 9]
print(list(filter(is_positive, numbers)))


it_supply = {"monitor": 30, "keyboard": 40, "mouse": 34, "printer": 5}
print(list(filter(lambda supply: supply[1] > 34, it_supply.items())))


filtered_supplies = filter(lambda item: item[1] > 34, it_supply.items())
result = dict(filtered_supplies)
print(result)
