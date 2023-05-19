from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_machine = True

while coffee_machine:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        print("Thank you for using the coffee machine.")
        coffee_machine = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): #this is the class.attribute.
              coffee_maker.make_coffee(drink)
    else:
        print("I'm sorry, I don't recognize that input. Please try again.")