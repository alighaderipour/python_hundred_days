from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

timmy.forward(100)
timmy.left(90)
timmy.forward(100)

turtle_screen = Screen()
print(turtle_screen.canvheight)
print(turtle_screen.canvwidth)

turtle_screen.title("Tuuuuuuuuuuuuuuurtle")

turtle_screen.exitonclick()
