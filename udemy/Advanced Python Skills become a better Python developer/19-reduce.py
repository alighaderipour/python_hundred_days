"""
The reduce function in Python is used to apply a function cumulatively to the items of an iterable (like a list), reducing the iterable to a single value. It is part of the functools module.

Basic Example: Summing a List of Numbers
Here's a simple example where reduce is used to sum up a list of numbers.

"""

"""map: Applies a function to each item in an iterable (like a list) and returns an iterable of the results. The output has the same number of 
elements as the input. reduce: Applies a function cumulatively to the items of an iterable, reducing the iterable to a single value."""

from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]


# Define a function that will be applied cumulatively
def add(x, y):
    return x + y


# Use reduce to apply the function to the list
result = reduce(add, numbers)

print(result)  # Output: 15

# ////////////////////////////////////////////////////////////////////////////////
print(
    "# ////////////////////////////////////////////////////////////////////////////////"
)


from functools import reduce

# Define a list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]


# Define a function that returns the maximum of two values
def max_value(x, y):
    return x if x > y else y


# Use reduce to find the maximum value
max_result = reduce(max_value, numbers)

print(max_result)  # Output: 9
