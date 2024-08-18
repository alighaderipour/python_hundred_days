from faker import Faker

fakerz = Faker()

numbs = [fakerz.pyint(1, 100) for i in range(10)]
print(numbs)
