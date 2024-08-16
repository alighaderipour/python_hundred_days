from faker import Faker

faker = Faker()

int_num = [faker.pyint(-10, 10) for _ in range(3333)]
print(int_num)

max_list = []
x = float("-inf")
max_list.append(x)
for item in range(len(int_num)):
    temp_sum = 0
    for item2 in range(item, len(int_num)):
        temp_sum += int_num[item2]
        if temp_sum >= max(max_list):
            max_list.append(temp_sum)


print(max_list)
print(max(max_list))
