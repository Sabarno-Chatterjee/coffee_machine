from art import coffee
from art import tea
import menu
# from menu import tea


def take_order():
    """To receive the order as input and return it."""
    order = input("\n\nWhat would you like? (espresso/latte/cappuccino/masala chai): ").lower()
    if order == "off":
        global machine_on
        print("\nMachine down for maintenance.\n")
        machine_on = False

    elif order == "report":
        report()
    elif order == "refill":
        refill()
    return order


def report():
    """Generates report that shows
the current resource values"""
    for resource in menu.resources:
        print(f"{resource.title()} : {menu.resources[resource]}")
    print(f"Sugar : {menu.add_on['sugar']}")
    print(f"Tea premix : {menu.tea['tea_premix']}")


def sufficient_resources(order):
    """Checks for sufficient_resources."""
    for resource in menu.resources:
        if order == "masala chai" and resource != "money":
            if menu.tea["tea_premix"] < menu.MENU[order]["ingredients"][resource]:
                print(f"Insufficient {resource}, please wait for refill.")
                return False
            else:
                print(f"{order.title()}, is an excellent choice.")
                return True

        if resource != "money":
            if (menu.resources[resource]) < (menu.MENU[order]["ingredients"][resource]):
                print(f"Insufficient {resource}, please wait for refill.")
                return False
            elif menu.add_on["sugar"] <= 10:
                print(f"Insufficient sugar, please wait for refill.")
                return False
    else:
        print(f"{order.title()}, is an excellent choice.")
        return True


def sufficient_money(order):
    """Receives money and returns the change."""
    print("\nPlease insert the coins.\n")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    total += round((float(input("How many pennies?: ")) * 0.01), 2)
    if total < menu.MENU[order]["cost"]:
        print(f"Sorry that's not enough money, ${total} refunded.")
        return False
    else:
        menu.resources["money"] += menu.MENU[order]["cost"]
        return_money = round(total - float(menu.MENU[order]["cost"]), 2)
        print(f"Here's your change ${return_money}, Have a nice day!")
        return True


def make_coffee(order):
    """Take's the order as an argument and prepares the coffee by deducting the resources."""


    # print(tea)
    # print(f"\nHere's your simmering cup of {order}, enjoy!")
    # return ()

    for resource in menu.resources:
        if order == "masala chai" and resource != "money":
            menu.tea["tea_premix"] -= 30
        if resource != "money":
            menu.resources[resource] = menu.resources[resource] - menu.MENU[order]["igit push ngredients"][resource]
    print(coffee)
    print(f"\nHere's your simmering cup of {order}, enjoy!")


def refill():
    """Refills the coffee machine"""

    for resource in menu.resources:
        for drink in menu.MENU:

            if resource != "money" and menu.resources[resource] < (menu.MENU[drink]["ingredients"][resource]):
                if resource == "coffee":
                    menu.resources["coffee"] += 100
                elif resource == "milk":
                    menu.resources["milk"] += 200
                elif resource == "water":
                    menu.resources["water"] += 300
    if menu.add_on["sugar"] <= 10:
        menu.add_on["sugar"] += 90
    elif menu.tea["tea_premix"] <= 30:
        menu.tea["tea_premix"] += 70


machine_on = True

while machine_on:
    new_order = take_order()
    if new_order == "off" or new_order == "report" or new_order == "refill":
        continue
    if sufficient_resources(new_order):
        if (input("Would you like to add sugar?\n")).lower() == "y":
            menu.add_on["sugar"] -= 10
        else:
            pass
        if sufficient_money(new_order):
            make_coffee(new_order)
