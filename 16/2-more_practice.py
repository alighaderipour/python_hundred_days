import turtle

# Create a turtle named Timmy
timmy = turtle.Turtle()

# Set the shape of the turtle (default is classic arrow)
timmy.shape("turtle")

# Set the speed of the turtle
timmy.speed(2)


# Define a function to draw a square
def draw_square():
    for _ in range(4):
        timmy.forward(100)  # Move forward by 100 units
        timmy.right(90)  # Turn right by 90 degrees


# Draw the square
draw_square()

# Hide the turtle and display the window
timmy.hideturtle()
turtle.done()
