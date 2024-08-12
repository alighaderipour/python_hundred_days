"""
The `zip()` function in Python is used to combine corresponding elements from multiple iterable objects and return an iterator of tuples. Each tuple contains the corresponding elements from all the given iterables.
"""

lst1 = ["ali", "ahad"]
lst2 = [1, 2]

for item in zip(lst1, lst2):
    print(item)
