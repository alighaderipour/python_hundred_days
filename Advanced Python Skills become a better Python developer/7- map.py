"""
1- The map() function in Python is used to apply a function of one argument to each item of a list or other iterable, and returns a map object (an
iterator) of the results.
map(function, iterable, ...)
2- Returns a map object which is interior.
3- Use it instead of loops whenever you can.
"""

import math

numbers = [23, 345, 64, 2, 534, 64, 5, 756456, 2345, 234]


def plus_two(num):
    return num + 2


print(list(map(plus_two, numbers)))

random_num1 = [34, 52, 31]
random_num2 = [134, 9, 16]


def custom_add(num1, num2):
    return num1 + num2


print(list(map(custom_add, random_num1, random_num2)))

# Example : Capitalize all items in a list
country_name = ["iran", "sudan", "china"]
print(map(lambda name: name.capitilze(), country_name))
print(list(map(lambda name: name.capitalize(), country_name)))


men_age = [11, 24, 35, 32, 2, 54, 12, 43]
print(list(map(lambda x: int(math.pow(x, 3)), men_age)))


fruits = ["apple", "potatos", "tomato", "watermelons"]


def fruit_change(fruit):
    fruit_result = fruit.capitalize()
    if fruit.endswith("s"):
        fruit_result += " are great"
    else:
        fruit_result += " is great"
    return fruit_result


print(list(map(fruit_change, fruits)))


print(
    list(
        map(
            lambda fruit: (
                fruit.capitalize() + " are great"
                if fruit.endswith("s")
                else fruit.capitalize() + " is great"
            ),
            fruits,
        )
    )
)
print(
    list(
        map(
            lambda fruit: (
                fruit.capitalize() + " are great"
                if fruit.endswith("s")
                else +" is great"
            )
        ),
        fruits,
    )
)
