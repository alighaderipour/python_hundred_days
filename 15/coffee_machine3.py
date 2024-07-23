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
    "water": 2000,
    "milk": 2000,
    "coffee": 1000,
}
# variables
money = 0
serveAgain = True


# methods:
def resource_efficient(drink):
    for item, value in MENU[drink]["ingredients"].items():
        if value > resources.get(item, 0):
            print(f"sorry there is not enough {item}")
            return False
            # the get() method returns value of a key of a dictionary, 0 if no value for key found

    return True


def take_coins():
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


while serveAgain:
    choice = input("What would you like? (espresso/latte/cappuccino? ")
    choice_list = [
        "espresso",
        "latte",
        "cappuccino",
        "off",
        "report",
        "profit",
        "resource",
    ]
    if choice.lower() not in choice_list:
        print(
            f"you picked a drink which is not in the {choice_list}, please choose try again!"
        )
        continue
    elif choice == "off":
        serveAgain = False
        print("thank you for your purchase")
    elif choice == "report":
        print(f'water  : {resources["water"]} ml')
        print(f'milk   : {resources["milk"]} ml')
        print(f'coffee : {resources["coffee"]} g')
        print(f"{money}")
    elif choice == "profit":
        print(money)
    elif choice == "resource":
        print(resources)
    else:
        if resource_efficient(choice):
            received_money = take_coins()
            if received_money >= MENU[choice]["cost"]:
                for item, value in MENU[choice]["ingredients"].items():
                    resources[item] -= value
                extra_money = received_money - MENU[choice]["cost"]
                print(
                    f"you paid {round(received_money,2)}$, money refunded is {round(extra_money,2)}"
                )
                money += MENU[choice]["cost"]
                print(f"machine profit is {money}$")
                print(f"remained resources is : {resources}")
                print("what else you would like to purchase? ")
            else:
                print(
                    f"your money is not enough to make your item, money received is {received_money} but your drink cost is {MENU[choice]["cost"]}$"
                )

        else:
            pass
