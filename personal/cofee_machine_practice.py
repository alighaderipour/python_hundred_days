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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def order_efficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {ingredients[item]}.")
            return False
    return True


def take_coins():
    """returns total coins inserted"""
    # everytime your function returns something use docstrings
    print("please insert coins : ")
    total = 0
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickels : "))
    pennies = int(input("How many pennies : "))
    total += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


order_again = True
while order_again:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        order_again = False
        print("thank you")
    elif choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} g")
        print(f"money : {money} $")
    else:
        drink = MENU[choice]
        if order_efficient(drink["ingredients"]):
            money_received = take_coins()
            print(money_received)
            print(drink["cost"])
            if take_coins() >= drink["cost"]:
                # for item in resources:
                #     resources[item] -= drink["ingredients"][item]
                print("bigger")
        else:
            print("Sorry that's not enough money. Money refunded")
print(resources)
