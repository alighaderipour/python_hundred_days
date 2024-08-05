# random walk

import random
from turtle import Turtle, Screen


tur = Turtle()
screen = Screen()

screen.colormode(255)

# tur.shape("arrow")
tur.color("black")
tur.pensize(15)
# screen.setup(width=1700, height=950)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_move():
    movement = [tur.right, tur.left]
    for i in range(100):
        tur.color(random_color())
        angel = random.randint(3, 90)
        distance = random.randint(15, 35)
        direction = random.choice(movement)
        direction(angel)
        tur.forward(distance)


def straight_move():
    movement = [tur.right, tur.left]
    for i in range(100):
        tur.color(random_color())
        distance = random.randint(15, 35)
        direction = random.choice(movement)
        direction(90)
        tur.forward(distance)


def snake_move():
    tur.speed(0)
    movement = [tur.right, tur.left]
    for i in range(10000):
        tur.color(random_color())
        angel = random.randint(3, 5)
        distance = random.randint(1, 2)
        direction = random.choice(movement)
        direction(angel)
        tur.forward(distance)


# ? choose one of these functions

# random_move()
# straight_move()
snake_move()

screen.exitonclick()
