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


def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


is_even_list = [lambda x=x: x * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())


Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))


List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)
