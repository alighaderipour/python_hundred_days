import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if min(lowleft[0], upright[0]) < self.x < max(lowleft[0], upright[0]) and min(
            lowleft[1], upright[1]
        ) < self.y < max(lowleft[1], upright[1]):
            return True
        else:
            return False

    def distance_to(self, other):
        return math.sqrt(
            math.pow((self.x - other.x), 2) + math.pow((self.y - other.y), 2)
        )


class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right


point1 = Point(2, 3)
print(point1)
print(point1.x, point1.y)

print(point1.falls_in_rectangle((2, -3), (-5, 5)))

point2 = Point(3, 4)
print(point1.distance_to(point2))

rectangle1 = Rectangle(Point(2, 0), Point(4, 2))
