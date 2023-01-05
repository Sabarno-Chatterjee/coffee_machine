# Using OOPs concepts
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
available = order.get_items()

machine_on = True

while machine_on:
    order = Menu()
    available = order.get_items()
    order_name = input(f"What would you like to drink {available}.\n ")
    # cost_of_drink = MenuItem(order_name)
    # cost = cost_of_drink.cost()
    available = order.find_drink(order_name)
    cost_of_drink = available.cost
    if order_name == "off":
        print("Sorry, machine down for maintenance.")
        machine_on = False
        continue
    elif order_name == "report":
        print_report = CoffeeMaker()
        report = print_report.report()
        continue
    drink = order.find_drink(order_name)
    resources = CoffeeMaker()
    resources_sufficient = resources.is_resource_sufficient(drink)
    if resources_sufficient:
        print(f"{order_name.capitalize()} is an excellent choice.")
        # cost_of_drink = MenuItem(drink)
        # cost_of_drink = cost_of_drink.cost
        money = MoneyMachine()
        insert_coins = money.make_payment(cost_of_drink)



