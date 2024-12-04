print("-------------------create  dictionary--------------------------")
car_stock = {"Toyota": 10, "Nissan": 13, "Peugeot": 12}
print(car_stock)
print("-------------------get  dictionary value --------------------------")
Toyota_val = car_stock["Toyota"]
Nissan_val = car_stock.get("Nissan")
print("Toyota Inventory : ", Toyota_val, "Toyota Inventory", Nissan_val)

car_stock.update({"Volvo": 25})
print(car_stock)
print("-------------------all key,values --------------------------")
print(car_stock.keys())
print(car_stock.values())
print(car_stock.items())
print("----------------------fromkeys--------------------------------")
# when you want to create a dict out of a tuple with a single value for all keys
club_names = ("Perspolis", "Mes", "Nassaji", "Zobahan")
intial_value = 0
club_val = dict.fromkeys(club_names, intial_value)
print(club_val)
print("------------------------pop-----------------------------")
# dict.pop(key, default)
# key: The key to remove from the dictionary.
# default (optional): The value to return if the key is not found.
dict_names = {"Ali": 12, "Reza": 43, "Aria": 64, "Kourosh": 3, "Maryam": 26}
dict_names.pop("Alia", print("the name you tried to pop was not found"))
print("---------------------popitem-------------------------------")
# The popitem() method in Python is used with dictionaries to remove and return the last key-value pair as a tuple. It follows LIFO (Last In, First Out) order for removal.
from python_hundred_days.radnom_generators.random_dict import main

dict1 = main(5)
removed_item = dict1.popitem()
print(dict1)
print(removed_item)
print(
    "~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~~*~Advanced Topics ~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~~*~"
)
print("--------------------dictionary comprehension---------------------------")
# 1. Dictionary Comprehensions
# Dictionary comprehensions provide a concise way to create dictionaries.
dict_comp = {x: x**3 for x in [1, 2, 3, 4, 5]}
print(dict_comp)

# Swapping Keys and Values
original_dict = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original_dict.items()}
print(reversed_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}
# Creating Dictionaries from Two Lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print(combined_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# counting occurance
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {word: words.count(word) for word in set(words)}
print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# conditional assignment
numbers = range(6)
parity_dict = {num: ("even" if num % 2 == 0 else "odd") for num in numbers}
print(
    parity_dict
)  # Output: {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# filtering dict by values
original_dict = {"a": 5, "b": 15, "c": 10, "d": 20}
filtered_dict = {k: v for k, v in original_dict.items() if v > 10}
print(filtered_dict)  # Output: {'b': 15, 'd': 20}

print("--------------------Nested Dictionaries---------------------------")
# 2. Nested Dictionaries
# Dictionaries can hold other dictionaries as values.


nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}

# Accessing nested values
print(nested_dict["person1"]["name"])  # Output: Alice
print(
    "--------------------Handling Missing Keys with collections.defaultdict ---------------------------"
)
# 3. Handling Missing Keys with collections.defaultdict
# The defaultdict from the collections module provides a default value for missing keys.
