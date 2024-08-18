"""
1- They are a simple way of creating iterators. all the work we have done this is handled by generators.
2- They are easy to implement : we just have to create a function that returns elements with yield instead of return.
3- They can contain one or more yield statements.
4- When called, it returns an object (iterator) but does not start execution immediately.
5- Once the function Yields, the function is paused and the control is transferred to the caller.
6 -Local variables and their states are remembered between successive calls.
"""


class PowersOfTwo:
    def __init__(self, maximum=0):
        self.maximum = maximum

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.maximum:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration
