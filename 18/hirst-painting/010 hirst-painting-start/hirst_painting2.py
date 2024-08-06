import random
from turtle import Turtle, Screen
import colorgram

turtle = Turtle()

turtle.setheading(255)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100
screen = Screen()
screen.colormode(255)


# Extract colors from the image
rgb_colors = []
colors = colorgram.extract("image.jpg", 500)

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
colors = rgb_colors

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
