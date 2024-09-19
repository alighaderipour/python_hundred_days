class Person:
    def __init__(self, name, eye_color, hair_color, age):
        self.name = name
        self.eyeColor = eye_color
        self.hairColor = hair_color
        self.age = age

    def greet(self):
        print(
            f"Greetings {self.name}, you are {self.age} and you have {self.eyeColor} eyes!"
        )


class Developer(Person):
    def __init__(self, name, eye_color, hair_color, age, programming_language):
        # Call the constructor of the parent class (Person)
        super().__init__(name, eye_color, hair_color, age)
        self.programming_language = programming_language

    def introduce(self):
        print(f"{self.name} codes in {self.programming_language}.")


developer1 = Developer(
    name="Ali",
    eye_color="brown",
    hair_color="black",
    age=33,
    programming_language="python",
)
developer1.greet()
developer1.introduce()
