"""

Write a function that takes a single non-empty string of only lowercase and
uppercase ascii letters (word) as its argument, and returns an ordered list
containing the indices of all capital (uppercase) letters in the string."""


def capitals(word):
    return [x for x in range(len(word)) if word[x].isupper()]


print(capitals("CodEWarS"))
