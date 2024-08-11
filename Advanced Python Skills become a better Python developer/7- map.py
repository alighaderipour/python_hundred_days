"""
1- The map() function in Python is used to apply a function of one argument to each item of a list or other iterable, and returns a map object (an
iterator) of the results.
map(function, iterable, ...)
2- Returns a map object which is interior.
3- Use it instead of loops whenever you can.
"""

# Example : Capitalize all items in a list
country_name = ["iran", "sudan", "china"]
print(map(lambda name: name.capitilze(), country_name))
print(list(map(lambda name: name.capitalize(), country_name)))
