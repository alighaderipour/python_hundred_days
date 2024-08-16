# We have a hidden issue in our Rectangle class:

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
# We have named the points of the rectangle lowleft and upright. However, because the points are generated randomly, not always is lowleft the
# lower-left corner and upright the upper-right corner. The randomly generated coordinates of upright could be smaller than lowleft making upright the actual lower-left point. We can easily fix this issue by renaming lowleft and upright to point1 and point2: in the Rectangle class:

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
# That means point1 could be to the right of point2 and vice-versa and the Rectangle class would still make sense.



# You can find the complete code with the fix implemented below:

from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


# Create rectangle object
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)