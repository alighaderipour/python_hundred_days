import random
from turtle import Turtle, Screen

import colorgram

# Extract colors from the image
rgb_colors = []
colors = colorgram.extract("image.jpg", 500)

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# Initialize the turtle and screen
turtle = Turtle()
turtle.shape("arrow")
turtle.speed(0)
turtle.hideturtle()

screen = Screen()
screen.colormode(255)

# Define the colors
colors = rgb_colors

# Get screen dimensions
screen_width = screen.window_width()
screen_height = screen.window_height()

# Starting positions and center of the screen is (0,0)
# In order to go in bottom left side of the screen we negative the screen_width //2
"""(Double Slash or Floor Division): This operator performs division and returns the largest integer that is less than or equal to the division 
result."""

start_x = -screen_width // 2 + 20
start_y = -screen_height // 2 + 20


# Function to draw a dot with a given dot_color
def draw_dot(x, y, dot_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(20, dot_color)


# Set the spacing between dots
dot_spacing = 30

# Draw dots across the screen
x = start_x
while x < screen_width // 2 - 20:
    y = start_y
    while y < screen_height // 2 - 20:
        color = random.choice(colors)
        draw_dot(x, y, color)
        y += dot_spacing
    x += dot_spacing

# Close the screen on click
screen.exitonclick()

# First x is constant, and we go up by increasing y value
# Then after we are close to  screen_height // 2 - 20 we go right by add x  with dot_spacing and again we go up
