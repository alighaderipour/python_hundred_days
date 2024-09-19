class Person:
    def __init__(self, name, eyeColor, hairColor, age):
        self.name = name
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.age = age

    def greet(self):
        print(
            f"greetings {self.name}, you are {self.age} and you have {self.eyeColor} eyes!"
        )


person1 = Person(name="Ali", eyeColor="brown", hairColor="black", age=33)
person1.greet()

person2 = Person(name="Mahmood", eyeColor="black", hairColor="black", age=37)
person2.greet()
