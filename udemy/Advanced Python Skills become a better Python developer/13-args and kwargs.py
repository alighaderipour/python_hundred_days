"""
Special Symbols Used for passing arguments in Python:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
Note: “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function.”

"""

"""
The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 

The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
"""


def my_print_funtion(*args):
    for arg in args:
        print(arg)


my_print_funtion("hello", "I", "am", 15)


def my_print_function_extra(arg1, *args):
    print(f"args1 is : ", arg1)
    for arg in args:
        print(arg)


my_print_function_extra(12, "years", "to be", "free")


"""
What is Python **kwargs?
The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
Example 1: 

Python program to illustrate *kwargs for a variable number of keyword arguments. Here **kwargs accept keyworded variable-length argument passed by the function call. for first=’Geeks’ first is key and ‘Geeks’ is a value. in simple words, what we assign is value, and to whom we assign is key. 
"""


def funkwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


funkwargs(first="ali", mid="ghaderi", last="pour")


def process_item(item_type, **kwargs):
    print(f"Processing a {item_type}...")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("Item processed!\n")


# Processing different items
process_item("Book", title="Python Programming", author="John Doe", price=29.99)
process_item(
    "Electronics",
    name="Smartphone",
    brand="TechBrand",
    price=399.99,
    warranty="2 years",
)
process_item("Clothing", name="T-Shirt", size="M", color="Blue", price=19.99)
