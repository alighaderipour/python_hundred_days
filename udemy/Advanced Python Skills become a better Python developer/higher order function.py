"""
A function is called

Higher Order Function

if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as a parameter or returns a function as a result. Python too supports the concepts of higher order functions.

Properties of higher-order functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
Functions as objects
In Python, a function can be assigned to a variable. This assignment does not call the function, instead a reference to that function is created. Consider the below example, for better understanding.
"""


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout("Hello"))

# Assigning function to a variable
yell = shout

print(yell("task"))
"""
In the above example, a function object referenced by shout and creates a second name pointing to it, yell.

Passing Function as an argument to other function
Functions are like objects in Python, therefore, they can be passed as argument to other functions. Consider the below example, where we have created a function greet which takes a function as an argument.
"""


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)
"""
Returning function
As functions are objects, we can also return a function from another function. In the below example, the create_adder function returns adder function.

Example:
"""


# Python program to illustrate functions
# Functions can return another function


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


"""Decorators
Decorators are the most common use of higher-order functions in Python. It allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


Syntax:

@gfg_decorator
def hello_decorator(): 
    .
    .
    .

    
In the above code,

gfg_decorator

is a callable function, will add some code on the top of some another callable function,

hello_decorator

function and return the wrapper function
"""


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
