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
profit = 0
order_again = True


def check_resource(drink):
    for item, value in MENU[drink]["ingredients"].items():
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calc_coins():
    quarters = int(input("how many quarters ? "))
    dimes = int(input("how many dimes ?"))
    nickles = int(input("how many nickles ?"))
    pennies = int(input("how many pennies ?"))
    calculation = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return calculation


while order_again:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        order_again = False
        print("Thank You for visit! 👍")
    elif choice == "report":
        print(f"water  : {resources['water']}")
        print(f"milk   : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
        print(f"profit : {profit}")

    else:
        if check_resource(choice):
            total = calc_coins()
            if total < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                for item, value in resources.copy().items():
                    print(item, value, "before")
                    print(MENU[choice]["ingredients"][item])
                    resources[item] -= MENU[choice]["ingredients"][item]
                    print(item, value, "after")
