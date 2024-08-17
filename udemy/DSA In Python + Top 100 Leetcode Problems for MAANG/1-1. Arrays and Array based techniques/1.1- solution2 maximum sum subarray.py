from faker import Faker

faker = Faker()

# int_num = [faker.pyint(-10, 10) for _ in range(10)]
int_num = [8, -1, 9, -5, 1, 0, 6, -7, 1, 5]
print(int_num)


def maxSubArray(int_num):
    max_sofar = int_num[0]
    current_sum = int_num[0]
    for item in range(len(int_num)):
        if current_sum < 0:
            current_sum = 0
        current_sum += int_num[item]
        if current_sum > max_sofar:
            max_sofar = current_sum
    return max_sofar


print(maxSubArray(int_num))
