class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


ali = Person("ali", 18)
reza = Person("reza", 19)
hasan = Person("hasan", 22)
karim = Person("karim", 22)


