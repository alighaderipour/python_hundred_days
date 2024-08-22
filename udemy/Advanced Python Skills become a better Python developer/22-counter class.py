"""
1- A Counter is a dict subclass for counting hashtable objects. it is a collection where elements are stored as dictionary keys and their counts are
stored as dictionary values.
2- Counters are allowed to be any integer value including zero or negative counts. the Counter class is similar to bags or multilists in other
languages.
3- Elements are counted from an iterable or initialized from another mapping(or counter)
"""

import random
from collections import Counter

nums = [random.randint(1, 100) for _ in range(100)]
print(nums)
c = Counter(nums)
print(c)
