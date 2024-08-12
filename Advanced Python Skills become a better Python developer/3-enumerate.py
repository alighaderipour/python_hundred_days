"""
1- adds a counter to an iterable (lists, dictionaries, tuples, sets, strings) and returns is as an enumerate object
2- the enumerate object is usually used in for loops.
"""

fruits = ["apple", "banana", "cherry", "lemon"]
enumerated_fruits = enumerate(fruits)
print(enumerated_fruits)

for item in enumerated_fruits:
    print(item)

players = ["Ronaldo", "Ronaldo", "Larsen"]
enumerated_players = enumerate(players, start=10)
# set a start for enumerating the list
for item in enumerated_players:
    print(item)

files = ["Videos", "Pictures", "Documents"]
for index, item in enumerate(files, start=1):
    print(f"file{index}: {item}.jpg")

items = (("apple", 3), ("banana", 2), ("orange", 5))

for index, (fruit, quantity) in enumerate(items):
    print(f"{index} - we have {quantity} {fruit}s")

from faker import Faker

faker = Faker()

students = [faker.name() for _ in range(5)]
grades = [faker.pyfloat(2, 2, True, 0.01, 20) for _ in range(5)]
for index, (student, grade) in enumerate(zip(students, grades)):
    print(f"{index} - {student}: {grade}")
