import random
from turtle import Turtle, Screen

tin = Turtle()
tin.shape("arrow")
screen = Screen()
colors = [
    "#FFC67D",  # Coral
    "#ACFFAC",  # Mint Green
    "#4169E1",  # Royal Blue
    "#F7DC6F",  # Lemon Yellow
    "#FF69B4",  # Hot Pink
    "#228B22",  # Forest Green
    "#032B44",  # Cobalt Blue
    "#F5DEB3",  # Golden Brown
    "#C71585",  # Lavender
    "#1ABC9C",  # Turquoise
]

tin.speed(0)
for i in range(3, 10):
    tin.color(random.choice(colors))
    for item in range(i):

        tin.forward(100)
        tin.right(360 / i)


screen.exitonclick()
