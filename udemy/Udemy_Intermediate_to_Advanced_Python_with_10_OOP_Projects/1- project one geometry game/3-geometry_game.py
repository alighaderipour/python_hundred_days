"""
1- Writing down the objects on a paper.
2- Writing a class for each object.
3- Writing methods for each class.
4- Calling the classes and methods.

"""

import ipaddress
import turtle

from classppoint import PPoint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pint1 = Point(10, 20)
pint2 = Point(11, 21)
pint3 = Point(12, 22)
pint4 = Point(13, 23)
print(type(pint1))  # <class '__main__.Point'> this main means that
# __main__. means current file the main file


point5 = PPoint(100, 200)
print(type(point5))  # <class 'classppoint.PPoint'>
# if you import from another file the __.main__ will change to the name of the file you are importing from


print(turtle.__file__)


myip = ipaddress.IPv4Address("1.1.1.1")
print(ipaddress.__file__)


num1 = 22452
print(pint1)  # <__main__.Point object at 0x000001B194B7E5D0>
print(num1)
