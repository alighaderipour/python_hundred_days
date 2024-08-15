class Car:
    def __init__(self, seats, year_model):
        self.seat = seats
        self.year_model = year_model

    def race_mode(self):
        self.seat = 2

    def normal_mode(self):
        self.seat = 5


# ? a function attached to an object is called a method
# ? we use self in method so the attributes knows which object is called it

toyota = Car(5, 1989)


next_id = 1


class User:
    def __init__(self, name, family):
        global next_id
        self.id = next_id
        next_id += 1
        self.name = name
        self.family = family
        self.follower = 0
        self.following = 0

    def follow(self):
        self.following += 1
        self.following += 1


user1 = User("Ali", "Ghaderi Pour")
user2 = User("Reza", "Ahmadi")


print(user1.id)  # Output: 1
print(user2.id)  # Output: 2
