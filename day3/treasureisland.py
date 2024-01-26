print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("**** Begin Game ****\n")

# takes user info do decide which way to go
direction = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"? \n')
# decision tree
if direction.lower() == "left":
    swim_wait = input('You\'ve come to the lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accoss. \n')
    if swim_wait.lower() == "wait":
        color = input("You have successfully arrived at the island. There is a house with 3 doors. One red, one yellow , one blue. Choose a color (red, blue, yellow)? \n")
        if color.lower() == "blue":
            print("You entered a room full of Monsters... GAME OVER!!")
        elif color.lower() == "yellow":
            print("Congrats - You found the treasure.. YOU WIN!!!")
        elif color.lower() == "red":
            print("You enter a room full of fire.. GAME OVER!!")
        else:
            print("You chose door that doesn't exist.. GAME OVER!!") 
    else:
        print("You got attacked by a Shark.. GAME OVER!!")
else:
    print("Wrong Way... GAME OVER!!")
