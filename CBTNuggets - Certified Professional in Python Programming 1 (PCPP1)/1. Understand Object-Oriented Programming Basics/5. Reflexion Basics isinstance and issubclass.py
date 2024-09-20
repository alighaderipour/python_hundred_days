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


class Developer(Person):
    pass


person1 = Person(name="ali", age=21, eye_color="brown", hair_color="black")
person1.greet("zari")


def print_person_details(person):
    # check whether an object is i  nstance of a specific class or not
    if isinstance(person, Person):
        print(f"{person.name}")
    else:
        print("not instance of Person")


print_person_details(person1)
print_person_details(1)

print(f"is Developer a subclass of Person? ", issubclass(Developer, Person))
