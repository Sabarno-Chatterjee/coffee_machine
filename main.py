import menu
import art


def take_order():
    return input("What would you like? (espresso/latte/cappuccino):\n")


def receive_money():
    print("\nPlease insert the coins.\n")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    def calc():


# print("\Here's your change.\n")


# def return_money():


# order = take_order()
# money()

print("\nPlease insert the coins.\n")
quarters = float(input("How many quarters?: ")) * 0.25
print(quarters)
calc = quarters - float(menu.MENU["latte"]["cost"])
print(calc)
print(menu.MENU["latte"]["cost"])

