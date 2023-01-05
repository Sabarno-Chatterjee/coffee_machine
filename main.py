# Using OOPs concepts
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
available = order.get_items()

machine_on = True
money = MoneyMachine()
resources = CoffeeMaker()
while machine_on:

    gootorder = Menu()
    available = order.get_items()
    order_name = input(f"What would you like to drink {available}.\n ")
    if order_name == "off":
        print("Sorry, machine down for maintenance.")
        machine_on = False
        continue
    elif order_name == "report":
        report = resources.report(), money.report()
        continue
    available = order.find_drink(order_name)
    cost_of_drink = available.cost
    drink = order.find_drink(order_name)

    resources_sufficient = resources.is_resource_sufficient(drink)
    if resources_sufficient:
        print(f"{order_name.capitalize()} is an excellent choice.")
        insert_coins = money.make_payment(cost_of_drink)
        if insert_coins:
            coffee = resources.make_coffee(drink)
