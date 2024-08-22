import random

fruits = {"apple": 60, "orange": 23, "watermelon": 91, "banana": 39}
print(fruits.get("apple"))
fruits.setdefault("kiwi", 0)


students = ["ali", "reza", "karim"]

quantize = dict()
for stu in students:
    quantize[stu] = quantize.setdefault(stu, random.randint(1, 101))
print(quantize)
