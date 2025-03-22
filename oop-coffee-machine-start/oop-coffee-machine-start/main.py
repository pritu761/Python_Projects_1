from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
a=True
while a:
    choice = menu.get_items()
    options = input(f"Enter options:{choice}")
    if options == "off":
        a = False
        print("Turning off coffee maker")
        continue
    elif options == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(options)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


