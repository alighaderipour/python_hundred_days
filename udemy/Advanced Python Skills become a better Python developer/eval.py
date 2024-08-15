x = 1
print(eval("x + 1"))  # Output: 2

expression = "3 * (4 + 5)"
result = eval(expression)  # Output: 27


def calculate_area(length):
    return length * length


area_expression = "calculate_area(5)"
print(eval(area_expression))  # Output: 25


def square(n):
    return n * n


# Define a restricted environment
restricted_globals = {"square": square}
restricted_locals = {}

# User input for the number to square
number = 4
expression = "square(number)"

# Evaluate the expression in a restricted environment
output = eval(expression, restricted_globals, {"number": number})
print(output)  # Output: 16
