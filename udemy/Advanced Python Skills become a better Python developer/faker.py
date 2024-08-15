from faker import Faker

faker = Faker()

students = [faker.name() for _ in range(5)]
grades = [faker.pyfloat(2, 2, True, 0.01, 20) for _ in range(5)]
for index, (student, grade) in enumerate(zip(students, grades)):
    print(f"{index} - {student}: {grade}")
