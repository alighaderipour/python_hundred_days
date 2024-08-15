"""
Dictionary comprehension is a syntactic construct that allows you to create dictionaries in a single line of code.
It provides a more readable and compact way to create dictionaries compared to traditional methods.
Syntax
The basic syntax for dictionary comprehension is:
python
{key_expression: value_expression for item in iterable}
key_expression: This defines how the keys of the dictionary will be generated.
value_expression: This defines how the values of the dictionary will be generated.
iterable: This is the collection (like a list or a tuple) that you are iterating over.
"""

from faker import Faker

fake = Faker()

students = [fake.name() for _ in range(5)]
grades = [fake.pyfloat(2, 2, True, 0.01, 20) for _ in range(5)]

new_dict = {stu: gra for stu, gra in zip(students, grades)}
print(new_dict)

for st, gr in zip(students, grades):
    print(f"student {st} has grade: {gr}")
