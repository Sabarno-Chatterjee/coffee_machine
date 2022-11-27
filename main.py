# import menu
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
# # def money(order):
# #     print("\nPlease insert the coins.\n")
# #     quarters = float(input("How many quarters?: ")) * 0.25
# #     dimes = float(input("How many dimes?: ")) * 0.1
# #     nickles = float(input("How many nickles?: ")) * 0.05
# #     pennies = float(input("How many pennies?: ")) * 0.01
# #     total_money_received = quarters + dimes + nickles + pennies
# #     return total_money_received - float(menu.MENU[order]["cost"])
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

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    }
}

resources = {
    "water": 300,
    "milk": 0,
    "coffee": 100,
}


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
    global sufficient_resources
    for resource in resources:
        if (resources[resource]) < (MENU[order]["ingredients"][resource]):
            sufficient_resources = False
            return f"Insufficient {resource}, please wait for refill."
    else:
        return "Here's your cafe"


machine_on = True
sufficient_resources = True

while machine_on:

    new_order = take_order()
    if new_order == "off" or new_order == "report":
        continue
    else:
        print(check_resources(new_order))

# order = "latte"
# print(check_resources(order))