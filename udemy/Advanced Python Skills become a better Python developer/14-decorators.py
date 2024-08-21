"""

In Python, a decorator is a special type of function that can modify or extend the behavior of another function. A decorator is a small function that takes another function as an argument and returns a new function that "wraps" the original function. The new function produced by the decorator is then called instead of the original function when it's invoked.
"""


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@log_calls
def add(a, b):
    return a + b


result = add(2, 3)
# Output:
# add called with arguments: (2, 3) {}
# add returned: 5
print(result)  # 5
