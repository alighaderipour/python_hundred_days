from turtle import Turtle, Screen
import random

# Create the first turtle
turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("red")

# Create the second turtle
turtle2 = Turtle()
turtle2.shape("turtle")
turtle2.color("green")


finish_line = Turtle()
finish_line.color("black")

# Set the size of the screen
manual_width = 800
manual_height = 600
screen = Screen()
screen.setup(width=manual_width, height=manual_height)  # Set the screen size

# Calculate the starting position for both turtles
start_x = -manual_width / 2 + 20  # X-coordinate for left middle
start_y1 = +20  # Y-coordinate for turtle1
start_y2 = -20  # Y-coordinate for turtle2 (slightly below turtle1)

# Move turtle1 to the starting position without drawing
turtle1.penup()  # Lift the pen to avoid drawing
turtle1.setposition(start_x, start_y1)  # Set position
turtle1.pendown()  # Put the pen down if you want to draw later

# Move turtle2 to the starting position without drawing
turtle2.penup()  # Lift the pen to avoid drawing
turtle2.setposition(start_x, start_y2)  # Set position
turtle2.pendown()  # Put the pen down if you want to draw later


end_of_race = 0


def turtle_pos(turtle):
    turtle_x, turtle_y = turtle.pos()
    return turtle_x, turtle_y


finish_line.penup()
finish_line.pendown()
finish_line.hideturtle()
finish_line.setposition(0, +135)
finish_line.setheading(270)  # Point downwards
finish_line.forward(270)  # Draw a vertical line


while True:
    turtle1_distance = random.randint(1, 20)
    turtle2_distance = random.randint(1, 20)
    if turtle_pos(turtle1)[0] < 0 and turtle_pos(turtle2)[0] < 0:
        turtle1.forward(turtle1_distance)
        turtle2.forward(turtle2_distance)
    elif turtle_pos(turtle1)[0] >= 0 or turtle_pos(turtle2)[0] >= 0:
        if turtle_pos(turtle1)[0] >= 0 and turtle_pos(turtle2)[0] >= 0:
            print("both turtle wins")
            break
        elif turtle_pos(turtle1)[0] >= 0 and turtle_pos(turtle2)[0]:
            print("turtle1 wins")
            break
        elif turtle_pos(turtle1)[0] < 0 and turtle_pos(turtle2)[0] >= 0:
            print("turtle2 wins")
            break
        else:
            print("error")
            break
# Keep the window open until clicked
screen.exitonclick()
