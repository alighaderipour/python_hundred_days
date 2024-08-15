import math
import random


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
        print(
            f" rectangle coordination: ({lower_left.x},{lower_left.y}) , ({upper_right.x}{upper_right.y})"
        )


rectangle1 = Rectangle(
    Point(random.randint(0, 9), random.randint(0, 9)),
    Point(random.randint(0, 9), random.randint(0, 9)),
)

guessed_x = int(input("guess x   : "))
guessed_y = int(input("guess y   : "))
point_guessd = Point(guessed_x, guessed_y)

print(point_guessd.falls_in_rectangle)
