import random

print('''
Heads 

or 

Tails
''')
choice = input("Please choice one: \n")

random_int = random.randint(0,1)

if choice.capitalize() == "Heads" or choice.capitalize() == "Tails":
    if random_int == 1:
        if choice.capitalize() == "Heads":
            print("YOU WIN!!! - you picked 'Heads'")
            print(f"random_int is: {random_int}")
        else: 
            print("YOU LOSE!! - you picked 'Tails'")
            print(f"random_int is: {random_int}")
    elif random_int == 0:
        if choice.capitalize() == "Tails":
            print("YOU WIN!!! - you picked 'Tails'")
            print(f"random_int is: {random_int}")
        else:
            print("YOU LOSE!! - you picked 'Heads'")
            print(f"random_int is: {random_int}")
else:
    print("You typed an invalid word. Try again - Please type 'Heads' or 'Tails'")
