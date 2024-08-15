"""Create a function that accepts a string and a single character,
and returns an integer of the count of occurrences the 2nd argument is found
in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0
"""


def str_count(strng, letter):
    counter = 0
    for i in range(len(strng)):
        if strng[i] == letter:
            counter += 1
    return counter


print(str_count("hello", "l"))


"""
def strCount(string, letter):
    return string.count(letter)
"""
