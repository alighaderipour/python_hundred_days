listo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 222, 11, 12, 13, 14]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


filtered_list = list(filter(lambda x: x % 2 == 0, listo))

print(filtered_list)
