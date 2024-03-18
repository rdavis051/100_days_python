from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available_drink = Menu()
machine = CoffeeMaker()
payment = MoneyMachine()

next_order = True
drink_options = available_drink.get_items()
while next_order:
    choice = input(f"Available drinks are: '{drink_options}: ").lower()
    if choice == "off":
        print("GoodBye!!")
        next_order = False
    elif choice == "report":
        machine.report()
        payment.report()
    else:
        drink = available_drink.find_drink(choice)
        enough_ingredients = machine.is_resource_sufficient(drink)
        print(f"enough ingredients: {enough_ingredients}")
        if enough_ingredients:
            print(f"That drink costs: ${drink.cost}")
            if payment.make_payment(drink.cost):
                machine.make_coffee(drink)