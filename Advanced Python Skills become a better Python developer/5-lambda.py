"""
1- also called anonymous functions because they are unnamed.
2- it's syntax is : lambada argument: expression.
3- they can take any number of parameters.

"""

add = lambda x: x + 2
print(add(5))

first_number = 5
multiple = lambda x: x * first_number
print(multiple(4))


lambda_function = [lambda x: x + j for j in range(15)]
first_lambda_function = lambda_function[0]
print(first_lambda_function(7))
