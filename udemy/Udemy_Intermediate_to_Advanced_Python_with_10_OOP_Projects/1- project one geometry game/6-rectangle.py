import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if min(rectangle.lower_left.x, rectangle.upper_right.x) < self.x < max(
            rectangle.lower_left.x, rectangle.upper_right.x
        ) and min(rectangle.lower_left.y, rectangle.upper_right.y) < self.y < max(
            rectangle.lower_left.y, rectangle.upper_right.y
        ):
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


rectangle1 = Rectangle(Point(2, 0), Point(4, 2))
pointx = Point(3, 1)

print(pointx.falls_in_rectangle(rectangle1))
