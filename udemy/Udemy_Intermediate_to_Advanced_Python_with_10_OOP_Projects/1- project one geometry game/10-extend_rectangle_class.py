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
            f" rectangle coordination: ({lower_left.x},{lower_left.y}) , ({upper_right.x},{upper_right.y})"
        )

    def area(self):
        return abs(self.lower_left.x - self.upper_right.x) * abs(
            self.lower_left.y - self.upper_right.y
        )


class GuiRectangle(Rectangle):
    def draw(self):
        from turtle import Turtle, Screen

        screen = Screen()
        screen.screensize(200, 200)
        my_turtle = Turtle()
        my_turtle.penup()
        my_turtle.goto(self.lower_left.x, self.lower_left.y)
        my_turtle.pendown()
        for _ in range(2):
            my_turtle.forward(abs(self.lower_left.x - self.upper_right.x))
            my_turtle.left(90)
            my_turtle.forward(abs(self.lower_left.y - self.upper_right.y))
            my_turtle.left(90)


rectangle1 = Rectangle(
    Point(random.randint(-200, 200), random.randint(-200, 200)),
    Point(random.randint(-200, 200), random.randint(-200, 200)),
)

# guessed_x = int(input("guess x   : "))
# guessed_y = int(input("guess y   : "))
point_guessd = Point(242, 343)


print(point_guessd.falls_in_rectangle(rectangle1))
print(f"the area of the rectangle is {rectangle1.area()}")


gui = GuiRectangle(
    Point(random.randint(-200, 200), random.randint(-200, 200)),
    Point(random.randint(-200, 200), random.randint(-200, 200)),
)
gui.draw()
