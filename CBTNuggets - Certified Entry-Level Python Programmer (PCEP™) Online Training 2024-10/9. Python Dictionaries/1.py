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

print("--------------------dictionary comprehension---------------------------")
