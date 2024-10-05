class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.age = age

    def __eq__(self, object):
        return self.name == object.name
        # and self.age == object.age)

    def __gt__(self, object):
        return self.age > object.age


p1 = Person("ali", "ghaderi", 34)
p2 = Person("ali", "rezaie", 32)
print(p1 == p2)
print(p1 > p2)
# we redefined == function
# == is a magic method
