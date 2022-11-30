from menu import MENU
from menu import resources
from art import coffee


def take_order():
    """To receive the order as input and return it."""
    order = input("\n\nWhat would you like? (espresso/latte/cappuccino): ").lower()
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
    for resource in resources:
        print(f"{resource.title()} : {resources[resource]}")


def check_resources(order):
    """Checks for sufficient_resources."""
    global sufficient_resources
    for resource in resources:
        if resource != "money":
            if (resources[resource]) < (MENU[order]["ingredients"][resource]):
                sufficient_resources = False
                return f"Insufficient {resource}, please wait for refill."
    else:
        return f"{order.title()}, is an excellent choice. "


def money(order):
    """Receives money and returns the change."""
    global sufficient_money
    print("\nPlease insert the coins.\n")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    total += round((float(input("How many pennies?: ")) * 0.01),2)
    if total < MENU[order]["cost"]:
        sufficient_money = False
        return f"Sorry that's not enough money, ${total} refunded."
    else:
        resources["money"] += MENU[order]["cost"]
        return_money = round(total - float(MENU[order]["cost"]), 2)
        return f"Here's your change ${return_money}, Have a nice day!"


def make_coffee(order):
    """Take's the order as an argument and prepares the coffee by deducting the resources."""
    for resource in resources:
        if resource != "money":
            resources[resource] = resources[resource] - MENU[order]["ingredients"][resource]
    print(coffee)
    return f"\nHere's your simmering cup of {order}, enjoy!"


def refill():
    """Refills the coffee machine"""
    for resource in resources:
        if resource != "money":
            resources[resource] = resources[resource] + 50


machine_on = True

while machine_on:
    sufficient_resources = True
    sufficient_money = True
    new_order = take_order()
    if new_order == "off" or new_order == "report" or new_order == "refill":
        continue
    else:
        print(check_resources(new_order))

    if sufficient_resources:
        print(money(new_order))
    if sufficient_money and sufficient_resources:
        print(make_coffee(new_order))
