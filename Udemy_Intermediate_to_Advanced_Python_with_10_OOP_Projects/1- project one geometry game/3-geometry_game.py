import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


x, y , z, r = random.randint(-10, 9)
first_point = Point(x, y)
second_point = Point(y,z)
