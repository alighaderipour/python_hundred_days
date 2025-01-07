from faker import Faker

fake = Faker()
fake_list = [fake.pyint(min_value=10, max_value=20) for i in range(200)]

print(fake_list)

counter = {i: fake_list.count(i) for i in set(fake_list)}
print(counter)
# -------------------------------------------------------
from faker import Faker

fake = Faker()
fake_list = [fake.pyint(min_value=10, max_value=20) for i in range(200)]

print(fake_list)

counter = {i: fake_list.count(i) for i in set(fake_list)}
print(counter)
