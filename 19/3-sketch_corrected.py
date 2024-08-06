from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.setheading(90)
    turtle.forward(10)


def move_down():
    turtle.setheading(270)
    turtle.forward(10)


def move_left():
    turtle.setheading(180)
    turtle.forward(10)


def move_right():
    turtle.setheading(0)
    turtle.forward(10)


screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_right, key="d")
screen.onkey(move_down, key="s")
screen.onkey(move_left, key="a")

screen.exitonclick()
