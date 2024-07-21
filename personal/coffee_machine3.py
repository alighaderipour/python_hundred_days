MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# variables
money = 0
serveAgain = True


# methods:
def resource_efficient(drink):
    print(MENU[drink]["cost"])


while serveAgain:
    choice = input("What would you like? (espresso/latte/cappuccino? ")
    if choice.lower() not in ["espresso", "latte", "cappuccino"]:
        print("you picked a drink which is not in the list, try again!")
        continue
    elif choice == "off":
        serveAgain = False
    elif choice == "report":
        print(f'water  : {resources["water"]} ml')
        print(f'milk   : {resources["milk"]} ml')
        print(f'coffee : {resources["coffee"]} g')
        print(f"{money}")
    else:
        resource_efficient(choice)
# Sorry there is not enough wate
