"""
sort vs sorted
1- The Sort method only works with lists.
2- The sorted function works with any iterable.
3- You can specify the parameter reverse in both of them.
4- And you can also specify a key.
5- Sort() returns "None" and modifies the original list in-place.
sorted() returns a new sorted list and does not modify the original.

"""

fruits = ["apple", "watermelon", "banana", "potato"]
fruits.sort()
print(fruits)


best_player = "Maradona is the best player in history"
print(sorted(best_player, reverse=True))

students_grade = {"Ali": 20, "Mahmood": 19, "Hadi": 21}
print(students_grade.values())
print(sorted(students_grade.values()))
print(students_grade.keys())
print(sorted(students_grade.keys()))


def get_quantity(grade):
    return students_grade[grade]


print(sorted(students_grade, key=get_quantity))

it_supply = {"Moniotors": 120, "CPU": 12, "Mouse": 98}
print(sorted(it_supply, key=lambda supply: it_supply[supply]))
