import random
from turtle import Turtle, Screen

tur = Turtle()
tur.shape("arrow")
tur.speed("fastest")
tur.color("green")

screen = Screen()
screen.colormode(255)


def choose_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def draww(size_of_gap):
    for item in range(int(360 / size_of_gap)):
        tur.color(choose_color())
        tur.circle(100)
        tur.setheading(tur.heading() + size_of_gap)


draww(10)
screen.exitonclick()
