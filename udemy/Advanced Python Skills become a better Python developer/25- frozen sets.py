"""
1- The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
2- Frozenset() method is just an immutable version of python set object. While elements of a set can be modifed at any time,
elements of the frozenset remains the same after creation
"""

empty_set = set()
empty_set.add({1, 2, 4})

# TypeError: unhashable type: 'set'


"""
The error TypeError: unhashable type: 'set' occurs because sets are mutable, and therefore cannot be used as elements in another set.

In Python, sets can only contain immutable elements, such as integers, strings, tuples, and frozensets. This is because sets use a hash table to store their elements, and mutable objects cannot be hashed.

When you try to add a set to another set, Python raises a TypeError because sets are mutable and cannot be hashed.

To fix this, you can use a frozenset instead of a set as an element. Frozensets are immutable, so they can be used as elements in a set:
"""


empty_dictionary = {{1, 2, 4}: 3}
print(empty_dictionary)
# TypeError: unhashable type: 'set'


frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # frozenset({1, 2, 3, 4})


empty_set2 = set()
empty_set2.add(frozen_set)
