import random
import sys


rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"     Rock
'''

paper = '''
            ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       Paper
'''

scissor = '''
     .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/       Scissor
'''

choice_list = []
choice_list.append(rock)
choice_list.append(paper)
choice_list.append(scissor)

# get and print users choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n")
user_choice = int(user_choice)
if user_choice > 2 or user_choice < 0:
    print("Invalid number: YOU LOSE!")
    sys.exit(0)
print(choice_list[user_choice])

choice_length = len(choice_list)
#print(f"list length: {choice_length}")
random_int = random.randint(0, choice_length - 1)
print("")
#print(random_int)
print("Computer Chose: ")
print(choice_list[random_int])

loser = "You Lose :("
winner = "You WIN :)"

if user_choice == random_int:
    print("Tie")
    #sys.exit(0)
elif user_choice == 0:
    if random_int == 1:
        print(loser)
    elif random_int == 2:
        print(winner)
elif user_choice == 1:
    if random_int == 2:
        print(loser)
    elif random_int == 0:
        print(winner)
elif user_choice == 2:
    if random_int == 0:
        print(loser)
    elif random_int == 1:
        print(winner)
else:
    print("Something went wrong")

#if user_choice == 0 and random_int == 2:
#    print("You win!!")
#elif random_int > user_choice:
#    print("You lose")
#elif user_choice == random_int:
#    print("It's a draw")
#else:
#    print("You entered an invalid number")
