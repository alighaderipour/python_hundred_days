from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.setheading(90)
    turtle.forward(10)


def move_down():
    turtle.setheading(90)
    turtle.forward(10)


def move_left():
    turtle.setheading(270)
    turtle.forward(10)


def move_right():
    turtle.setheading(90)
    turtle.forward(10)


screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_right, key="d")
screen.onkey(move_down, key="s")
screen.onkey(move_left, key="a")

screen.exitonclick()
"""
A function is called
Higher Order Function
if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as 
Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as 
a parameter or returns a function as a result. Python too supports the concepts of higher order functions."""
