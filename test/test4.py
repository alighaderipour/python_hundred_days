listo = [1, 4, 3, 63, 621]
num = next((item for item in listo if item == 3), None)
print(num)
