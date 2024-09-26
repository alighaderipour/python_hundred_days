# print(4 + 3)
# print("4" + "3")
# # why? same + but they act differently


class Test1:
    def __init__(self, name, family):
        self.person = name + family

    def __str__(self):
        return f"{self.person} is the best"


class Test2:
    def __init__(self, name, family):
        self.person = name + family

    def __str__(self):
        return f"{self.person} is the best"


a1 = Test1("Karim", "Bagheri")
a2 = Test2("Reza", "Javadi")
print(a1)
print(a2)
