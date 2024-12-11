import numpy as np

list_a = [1, 2, 3, 4]
print(list_a)
print(id(list_a))
list_a.append(5)
print(list_a)
print(id(list_a))

array_a = np.array([1, 2, 3, 4])
print(type(array_a))

print(id(array_a))

np.append(array_a, [5])
print("array_a", array_a)
print(id(array_a))
print(type(array_a))
