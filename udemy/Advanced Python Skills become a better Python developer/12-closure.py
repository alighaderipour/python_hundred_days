"""
In Python, a closure is a function that has access to its own scope and the scope of its surrounding environment.
 In other words, a closure is a function that "remembers" the
variables and functions of its surrounding scope, even when it's called outside of that scope.
A closure is created when a function is defined inside another function,
and the inner function uses variables from the outer function's scope.
The inner function "closes over" the variables of the outer function, hence the name "closure".
"""

"""
Closures are useful when you need to:

Encapsulate data: Hide internal implementation details and expose only a controlled interface.
Create higher-order functions: Functions that take other functions as arguments or return functions as output.
Implement decorators: Functions that modify or extend the behavior of other functions.
"""


def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3


# ////////////////////////////////////////////////////////////////////////////////////////////////
def double_decorator(func):
    def wrapper(x):
        return func(x) * 2

    return wrapper


@double_decorator
def add_one(x):
    return x + 1


result = add_one(5)
print(result)  # 12


# ////////////////////////////////////////////////////////////////////////////////////////////////


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
print(account.get_balance())  # 100
account.deposit(50)
print(account.get_balance())  # 150
