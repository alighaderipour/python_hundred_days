from turtle import Turtle, Screen

turtlex = Turtle()
turtlex.shape("turtle")

# draw some stars

while True:
    print(turtlex.pos(), abs(turtlex.pos()))
    turtlex.speed("fastest")
    turtlex.forward(200)
    turtlex.left(170)

    if abs(turtlex.pos()) < 0.00005:
        break

screen = Screen()
screen.exitonclick()
