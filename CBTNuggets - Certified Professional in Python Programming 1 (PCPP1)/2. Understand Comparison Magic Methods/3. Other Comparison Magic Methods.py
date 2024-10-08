import functools


@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


ali = Person("ali", 18)
reza = Person("reza", 19)
hasan = Person("hasan", 22)
karim = Person("karim", 22)

print(reza > ali)
print(ali < hasan)
print(hasan == karim)

# you don't need to implement lower than dunder method, as python knows what to do when you implement __gt__
