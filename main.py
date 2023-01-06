# Using OOPs concepts
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_on = True

while machine_on:

    available = menu.get_items()
    order_name = input(f"What would you like to drink {available}.\n ")
    if order_name == "off":
        print("Sorry, machine down for maintenance.")
        machine_on = False
        continue
    elif order_name == "report":
        report = coffee_maker.report(), money_machine.report()
        continue
    available = menu.find_drink(order_name)
    cost_of_drink = available.cost
    drink = menu.find_drink(order_name)

    resources_sufficient = coffee_maker.is_resource_sufficient(drink)
    if resources_sufficient:
        print(f"{order_name.capitalize()} is an excellent choice.")
        insert_coins = money_machine.make_payment(cost_of_drink)
        if insert_coins:
            coffee = coffee_maker.make_coffee(drink)
