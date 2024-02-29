import sys

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

def add_money(prev_funds):
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarters_amt = round(quarters * .25, 2)
    #print(quarters_amt)
    dimes_amt = round(dimes * .10, 2)
    #print(dimes_amt)
    nickles_amt = round(nickles * .05, 2)
    #print(nickles_amt)
    pennies_amt = pennies * .01
    #print(pennies_amt)
    total = round(quarters_amt + dimes_amt + nickles_amt + pennies_amt, 2)
    return total + prev_funds


# TODO: 1. Check resources sufficient to make drink order
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
            return  False
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
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 2. check if money added is enough to by drink, if not return funds.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    continue_ordering = True
    while continue_ordering:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            print_report()
        elif choice == 'espresso':
            print("In Espresso")
            if money < MENU['espresso']['cost']:
                money = add_money(money)
                if money < MENU['espresso']['cost']:
                    print("Sorry that's not enough money. Money refunded.")
                    sys.exit()
            ingredients = enough_ingredients('espresso')
            if ingredients:
                print(f"money is now: {money}")
                money = round(money - MENU['espresso']['cost'], 2)
                print(f"Here is ${money} in change.")
                print(f"Here is your expresso - Enjoy!")
            else:
                print("There isn't enough ingredients for that drink!")
                print(f"Returning funds - returning ${money}")
        elif choice == 'latte':
            print("In Latte")
            if money < MENU['latte']['cost']:
                money = add_money(money)
                if money < MENU['latte']['cost']:
                    print("Sorry that's not enough money. Money refunded.")
                    sys.exit()
            ingredients = enough_ingredients('latte')
            if ingredients:
                print(f"money is now: {money}")
                money = round(money - MENU['latte']['cost'], 2)
                print(f"Here is ${money} in change.")
                print(f"Here is your latte - Enjoy!")
            else:
                print("There isn't enough ingredients for that drink!")
                print(f"Returning funds - returning ${money}")
        elif choice == 'cappuccino':
            print("In Cappuccino")
            if money < MENU['cappuccino']['cost']:
                money = add_money(money)
                if money < MENU['cappuccino']['cost']:
                    print("Sorry that's not enough money. Money refunded")
                    sys.exit()
            ingredients = enough_ingredients('cappuccino')
            if ingredients:
                money = round(money - MENU['cappuccino']['cost'], 2)
                print(f"money is now: {money}")
                print(f"Her is ${money} in change.")
                print(f"Here is your cappuccino - Enjoy!")
            else:
                print("There isn't enough ingredients for that drink!")
                print(f"Returning funds - returning ${money}")
        elif choice == 'off':
            continue_ordering = False
        else:
            print("You chose an invalid option! - Try again")



