from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drinks = Menu()
available = drinks.get_items()


machine_on = True

while machine_on:
    drink = input(f"What would you like to drink {available} .")
    if drink == "off":
        print("Sorry, machine down for maintenance.")
        machine_on = False
