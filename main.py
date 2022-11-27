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
    "milk": 200,
    "coffee": 100,
}


def take_order():
    """To receive the order as input and return it."""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


machine_on = True

while machine_on:

    order = take_order()
    if order == "off":
        machine_on = False
