from turtle import Turtle, Screen

turtlex = Turtle()
turtlex.shape("turtle")

# draw a squer
for i in range(4):
    turtlex.forward(100)
    turtlex.right(90)


screen = Screen()
screen.exitonclick()
