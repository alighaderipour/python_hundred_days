# ----------------------------- Definition -----------------------------
"""
1- Takes iterables (lists, dictionaries, tuples, sets, strings ) abd "zip" them into "tuples
2- Is used for parallel iteration
3- Returns a Zip Object, which is an iterator of tuples
"""

# ---------------------------------- LIST ----------------------------------

countries = ["Iran", "Spain", "Italy", "France", "Portugal", "England"]
clubs = ["Perspolis", "Real Madrid", "Inter", "P.S.G", "Porto", "Arsenal"]
players = ["Ali Parvin", "Zidane", "Zanetti", "Navas", "Pepe"]
zipped = zip(countries, clubs, players)
print(zipped)  # England is not going to get zipped

# print(zipped.__next__())

for country, club, player in zipped:
    print(country, club, player)

# ---------------------------------- DICTIONARIES ----------------------------------
products = {"apple": 0.5, "pineapple": 0.7}
tech = {"iPhone": 1000, "windows": 600}
products_tech = zip(products, tech)
for item in products_tech:
    print(item)
products_tech_values = zip(products.values(), tech.values())
for item in products_tech_values:
    print(item)

# ---------------------------------- Tuples ----------------------------------
countries_tuple = ("Iran", "Spain", "Italy", "France", "Portugal", "England")
clubs_tuple = ("Perspolis", "Real Madrid", "Inter", "P.S.G", "Porto", "Arsenal")
players_tuple = ("Ali Parvin", "Zidane", "Zanetti", "Navas", "Pepe")
zipped_tuple = zip(countries_tuple, clubs_tuple, players_tuple)
for item in zipped_tuple:
    print(item)

# ---------------------------------- Strings ----------------------------------
name = "ali"
family = "ghaderi pour"
zipped_string = zip(name, family)
for item in zipped_string:
    print(item)

## ---------------------------------- zip_lonest ----------------------------------

from itertools import zip_longest

name_longest = "ali"
family_longest = "ghaderi pour"
zipped_string_longest = zip_longest(name, family)
zipped_string_longest_fill_value = zip_longest(name, family, fillvalue="test")
for item in zipped_string_longest_fill_value:
    print(item)
