"""
1- a set is a collection which is unordered and un-indexed.
2- it is iterable, mutable and has no duplicate elements.
3- python's set class represents the mathematical notion of a set.
4- the major advantage of using a set, as opposed to a list, is that it has highly optimized method for checking
whether a specific element is contained in a set.

"""

import random
from collections import Counter

nums = [random.randint(1, 10) for x in range(1, 20)]
print(f"nums : {nums}")
p = Counter(nums)
print(f"occurrence : {p}")
nums_set = set(nums)
print(f"set : {nums_set}")
