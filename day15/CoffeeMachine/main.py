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

# TODO: 1. change how money is assigned and what it's tracking (profit refers to machine money)
profit = 0
money = 0

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press ⌃R to execute it or replace it with your code.
########################
# Program Requirements #
########################
# 1. Print Report
# 2. Check Resources Sufficient?
# 3. Process Coins (1 cent, 5 cents, 10 cents, 25 cents)
# 4. Check Transaction Successful
# 5. Make Coffee

def add_money():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarters_amt = round(quarters * .25, 2)
    dimes_amt = round(dimes * .10, 2)
    nickles_amt = round(nickles * .05, 2)
    pennies_amt = pennies * .01
    total = round(quarters_amt + dimes_amt + nickles_amt + pennies_amt, 2)
    return total


# TODO: 2. Check resources sufficient to make drink order
def enough_ingredients(coffee_type):
    """Checks there is enough ingredients to make coffee"""
    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']
    latte_water = MENU['latte']['ingredients']['water']
    latte_milk = MENU['latte']['ingredients']['milk']
    latte_coffee = MENU['latte']['ingredients']['coffee']
    cappuccino_water = MENU['cappuccino']['ingredients']['water']
    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
    if coffee_type == "espresso":
        if resources['water'] >= espresso_water and resources['coffee'] >= espresso_coffee:
            resources['water'] -= espresso_water
            resources['coffee'] -= espresso_coffee
            return True
        elif resources['water'] < espresso_water:
            print("Insufficient water")
            return False
        elif resources['coffee'] < espresso_coffee:
            print("Insufficient coffee")
            return False
    elif coffee_type == 'latte':
        if resources['water'] >= latte_water and resources['milk'] >= latte_milk and resources['coffee'] >= latte_coffee:
            resources['water'] -= latte_water
            resources['milk'] -= latte_milk
            resources['coffee'] -= latte_coffee
            return True
        elif resources['water'] < latte_water:
            print("Insufficient water")
            return False
        elif resources['milk'] < latte_milk:
            print("Insufficient milk")
            return False
        elif resources['coffee'] < latte_coffee:
            print("Insufficient coffee")
            return False
    elif coffee_type == 'cappuccino':
        if resources['water'] >= cappuccino_water and resources['milk'] >= cappuccino_milk and resources['coffee'] >= cappuccino_coffee:
            resources['water'] -= cappuccino_water
            resources['milk'] -= cappuccino_milk
            resources['coffee'] -= cappuccino_coffee
            return True
        elif resources['water'] < cappuccino_water:
            print("Insufficient water")
            return False
        elif resources['milk'] < cappuccino_milk:
            print("Insufficient milk")
            return False
        elif resources['coffee'] < cappuccino_coffee:
            print("Insufficient coffee")
            return False

#def subtract_ingredients(coffee_type, money):
#    """ subtracts the ingredients from resources """
#    if coffee_type == "espresso":


def print_report():
    """ Use a breakpoint in the code line below to debug your script. """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO: 3. check if money added is enough to by drink, if not return funds.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    continue_ordering = True
    while continue_ordering:
        change = 0
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            continue_ordering = False
        elif choice == 'report':
            print_report()
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            money = add_money()
            if money < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                continue_ordering = False
            ingredients = enough_ingredients(choice)
            if ingredients:
                print(f"money is now: {money}")
                profit += MENU[choice]['cost']
                change = round(money - MENU[choice]['cost'], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your expresso - Enjoy!")
            else:
                print("There isn't enough ingredients for that drink!")
                print(f"Returning funds - returning ${money}")
        else:
            print("You chose an invalid option! - Try again")



