"""
Python primarily organizes variable scope into four categories, often remembered as the LEGB Rule:

Local (L): Variables defined within a function or a block are considered local to that function/block.

They are accessible only within that function.
Created when the function starts and destroyed when the function ends.

"""

print("-----------------------------Local-----------------------------------")


def my_function():
    local_var = 10  # Local scope
    print(local_var)


my_function()
# print(local_var)  # This would raise an error.

print("-----------------------------Enclosing-----------------------------------")
"""
Enclosing (E): Variables in the enclosing function's scope. This applies to nested functions.

If a function is defined inside another function, the inner function can access variables from the outer (enclosing) function.
"""


def outer_function():
    enclosing_var = "I'm in the enclosing scope"

    def inner_function():
        print(enclosing_var)

    inner_function()


outer_function()
print("-----------------------------Global-----------------------------------")
"""
Variables defined at the top level of a module or declared using the global keyword.

These variables are accessible throughout the module, including inside functions (if explicitly declared as global)."""

global_var = "I'm global"


def my_function():
    print(global_var)


my_function()

print("-----------------------------Built-In-----------------------------------")
"""
Python’s reserved names and built-in functions (e.g., len, print, etc.).

These are always available unless shadowed by local variables."""
print(len("hello"))  # 'len' is a built-in function.


print(
    "-----------------------------Variable Shadowing-----------------------------------"
)
"""
A local variable can "shadow" a variable with the same name in an enclosing or global scope:
"""
x = 10


def my_function():
    x = 5  # Shadows the global x
    print(x)  # Prints 5


my_function()
print(x)  # Prints 10 (global x is unaffected)
