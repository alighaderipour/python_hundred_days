from turtle import Turtle


class MyTur:
    def __init__(self, name, shape, color):
        self.name = Turtle()
        self.name.shape = shape
        self.name.color = color


turt = MyTur("my_turtle", "arrow", "red")
"""
turt.forward(100)
this code is invalid because turf is not instance of Turtle() class, it is instance of Mytur() class !
# ? if you want turf have to a forward method you have to implement it
    def move_forward(self, distance):
        self.name.forward(distance)  # Move the turtle forward
    useage >
    turt.move_forward(100)
"""
