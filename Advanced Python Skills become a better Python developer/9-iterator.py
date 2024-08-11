"""
1- An iterable is a representation of a series of elements, which can be iterated over. It does not have any iteration state such as a "current
element", but every iterable can be converted to an iterator by using iter(). typically, an iterable should be able to produce any number of valid
iterators.
2- An iterator is the object with iteration state. it lets you check if it has more element using the next() or __next__() and move to the next
element ( if any).
3- In Python, an iterator is an object that allows you to traverse through all the values in a collection, such as lists, tuples, or dictionaries.
It implements the iterator protocol, which consists of two special methods: __iter__() and __next__().
Key Concepts
Iterator Protocol
__iter__(): This method returns the iterator object itself. It is called when an iterator is initialized.
__next__(): This method returns the next value from the iterator. When there are no more items to return, it raises a StopIteration exception to signal that the
 iteration is complete.
"""


# You can create your own iterator by defining a class that implements these two methods. Here's a simple example:
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration


# Using the iterator
iterator = MyIterator(5)
for number in iterator:
    print(number)

my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# next(iterator) would raise StopIteration
