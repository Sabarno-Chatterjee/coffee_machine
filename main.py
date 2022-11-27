from menu import MENU
from menu import resources


# import art
# # #
# # # def report():
# # #
# # def take_order():
# #     order = input("What would you like? (espresso/latte/cappuccino):\n").lower()
# # # #     if order == "report":
# # # #
# # # #     return order
# # # #
# # # #

#
#
# # order = take_order()
# # change = money(order)
# # print(f"\nHere's your change ${change}")
# # print("Have a nice day!")
#
# print(menu.MENU["latte"]["ingredients"])
#
# for ingredient in menu.MENU["latte"]["ingredients"]:
#
#     print(f"{ingredient} : {menu.MENU['latte']['ingredients'][ingredient]} ")
#     item_quantity = ({menu.MENU['latte']['ingredients'][ingredient]})
#     print(type(item_quantity))


def take_order():
    """To receive the order as input and return it."""
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        global machine_on
        machine_on = False

    elif order == "report":
        report()
    return order


def report():
    """Generates report that shows
the current resource values"""
    for resource in resources:
        print(f"{resource.title()} : {resources[resource]}")
    print(f"Money : $0 ")


def check_resources(order):
    """Checks for sufficient_resources."""
    global sufficient_resources
    for resource in resources:
        if (resources[resource]) < (MENU[order]["ingredients"][resource]):
            sufficient_resources = False
            return f"Insufficient {resource}, please wait for refill."
    else:
        return f"Here's your {order}"


def money(order):
    print("\nPlease insert the coins.\n")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total_money_received = quarters + dimes + nickles + pennies
    return round(total_money_received - float(MENU[order]["cost"]), 2)


machine_on = True

while machine_on:
    sufficient_resources = True
    new_order = take_order()
    if new_order == "off" or new_order == "report":
        continue
    else:
        print(check_resources(new_order))

    if sufficient_resources:
        print(money(new_order))

# order = "latte"
# print(check_resources(order))
