print(any([False, False, False, False]))
print(any([False, False, False, True]))
print(all([False, False, False, True]))
print(all([True, True, True, True]))


list1 = []
list2 = []
list3 = []
list4 = []


for i in range(1, 21):
    list1.append(4 * i - 3)


for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)

print("See whether all numbers in list1 are odd =>")
print(list2)
print(all(list2))

for i in range(1, 21):
    list3.append(3 * i + 7)

for i in range(0, 20):
    list4.append(list3[i] % 2 == 1)
print("See whether all numbers in list4 are odd =>")
print(list4)
print(all(list4))
