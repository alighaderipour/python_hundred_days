class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class NewPoint:
    def __init__(my_object, x, y):
        my_object.x = x
        my_object.y = y
        print("my_object : ", my_object)
