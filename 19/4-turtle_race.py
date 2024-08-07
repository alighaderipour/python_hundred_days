from turtle import Turtle, Screen

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
turtle1_x, turtle1_y = turtle1.pos()
turtle2_x, turtle2_y = turtle2.pos()
print(turtle1_x, turtle1_y)
print(turtle2_x, turtle2_y)

finish_line.penup()
finish_line.pendown()
finish_line.hideturtle()
finish_line.setposition(0, +135)
finish_line.setheading(270)  # Point downwards
finish_line.forward(270)  # Draw a vertical line

turtle1.forward(100)
turtle2.forward(70)


# Keep the window open until clicked
screen.exitonclick()
