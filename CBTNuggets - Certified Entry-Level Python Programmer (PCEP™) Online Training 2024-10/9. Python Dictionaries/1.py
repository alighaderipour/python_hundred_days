car_stock = {"Toyota": 10, "Nissan": 13, "Peugeot": 12}
Toyota_val = car_stock["Toyota"]
Nissan_val = car_stock.get("Nissan")
print(Toyota_val, " , ", Nissan_val)

car_stock.update({"Volvo": 25})
print(car_stock)

# when you want to create a dict out of a tuple with a single value for all keys
club_names = ("Perspolis", "Mes", "Nassaji", "Zobahan")
intial_value = 0
club_val = dict.fromkeys(club_names, intial_value)
print(club_val)
