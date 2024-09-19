class Person:
    print("class body only executed once")

    def __init__(self, name, eye_color, hair_color, age):
        self.name = name
        self.eyeColor = eye_color
        self.hairColor = hair_color
        self.age = age

        print("creating instance of Person class")

    def greet(self, other_name):
        print(f"hello {other_name} , my name is {self.name}")


person1 = Person(name="ali", age=21, eye_color="brown", hair_color="black")
person1.greet("zari")
