def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = 1  # Start with 1, as it is a divisor of all numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n


def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers


# Example usage:
start = 1
end = 1000000
print(
    f"Perfect numbers between {start} and {end} are: {perfect_numbers_in_range(start, end)}"
)
