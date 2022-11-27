import menu
import art


def take_order():
    return input("What would you like? (espresso/latte/cappuccino):\n")


def money(order):
    print("\nPlease insert the coins.\n")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total_money_received = quarters + dimes + nickles + pennies
    return total_money_received - float(menu.MENU[order]["cost"])


order = take_order()
change = money(order)
print(f"\nHere's your change ${change}")
print("Have a nice day!")
