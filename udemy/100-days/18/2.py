from turtle import Turtle, Screen

turtlex = Turtle()
turtlex.shape("turtle")
turtlex.speed(0)


# draw a circle
for i in range(540):
    turtlex.forward(1)
    turtlex.right(1)


screen = Screen()
screen.exitonclick()
