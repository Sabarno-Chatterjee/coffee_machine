from menu import MENU
from menu import resources
from menu import add_on
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
    print(f"Sugar : {add_on['sugar']}")


def sufficient_resources(order):
    """Checks for sufficient_resources."""
    for resource in resources:
        if resource != "money":
            if (resources[resource]) < (MENU[order]["ingredients"][resource]):
                print(f"Insufficient {resource}, please wait for refill.")
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
    if total < MENU[order]["cost"]:
        print(f"Sorry that's not enough money, ${total} refunded.")
        return False
    else:
        resources["money"] += MENU[order]["cost"]
        return_money = round(total - float(MENU[order]["cost"]), 2)
        print(f"Here's your change ${return_money}, Have a nice day!")
        return True


def make_coffee(order):
    """Take's the order as an argument and prepares the coffee by deducting the resources."""
    for resource in resources:
        if resource != "money":
            resources[resource] = resources[resource] - MENU[order]["ingredients"][resource]
    print(coffee)
    print(f"\nHere's your simmering cup of {order}, enjoy!")


def refill():
    """Refills the coffee machine"""

    # for resource in resources:
    #     if resource != "money" and resources[resource] == 0:
    #         resources[resource] = resources[resource] + 200
    def refill_coffee():
        """Refills coffee"""
        resources["coffee"] += 100

    def refill_milk():
        """Refills milk"""
        resources["milk"] += 200

    def refill_water():
        """Refills water"""
        resources["water"] += 300

    for resource in resources:
        for drink in MENU:

            if resource != "money" and resources[resource] < (MENU[drink]["ingredients"][resource]):
                if resource == "coffee":
                    refill_coffee()
                elif resource == "milk":
                    refill_milk()
                elif resource == "water":
                    refill_water()


machine_on = True

while machine_on:
    new_order = take_order()
    if new_order == "off" or new_order == "report" or new_order == "refill":
        continue
    if sufficient_resources(new_order):
        if (input("Would you like to add sugar?\n")).lower() == "y":
            add_on["sugar"] -= 10
        else:
            pass
        if sufficient_money(new_order):
            make_coffee(new_order)
