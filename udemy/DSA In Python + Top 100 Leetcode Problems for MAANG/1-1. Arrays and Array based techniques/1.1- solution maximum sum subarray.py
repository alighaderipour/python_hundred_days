from faker import Faker

faker = Faker()

# int_num = [faker.pyint(-10, 10) for _ in range(10)]
int_num = [8, -1, 9, -5, 1, 0, 6, -7, 1, 5]
max_list = []
current_max = 0
for item in range(len(int_num)):
    if len(max_list) == 0:
        if int_num[item] < 0:
            continue
        else:
            max_list.append(int_num[item])
            current_max = int_num[item]
    else:
        temp = current_max
        current_max += int_num[item]
        if current_max < temp:
            current_max = 0
            continue
        else:
            max_list.append(current_max)

print(max(max_list))
