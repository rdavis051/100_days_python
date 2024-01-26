import random
from hangman_art import banner, stages
from hangman_words import word_list

cnt = 0
#for word in stages:
#    stages[cnt].replace('\n', '')
#    print(stages[cnt])
#    cnt += 1

print(banner)

# parameters
still_guessing = True
#word_list = ["ardvark", "baboon", "camel"]
len_list = len(word_list)
chosen_word = random.choice(word_list)

print("")
# create blanks
display = []
for blank in chosen_word:
    display.append('_')
print(display)
print("")

incorrect_ans_cnt = 6
while still_guessing == True:
    match = False
    guess = input("Please guess a letter: ").lower()
    print()
    position = 0  # counter
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            match = True
        position += 1
    if match == False:
        print(stages[incorrect_ans_cnt])
        incorrect_ans_cnt -= 1
    #print(display)
    print(f"{' '.join(display)}")
    print()
    if '_' in display:
        still_guessing = True
    else:
        still_guessing = False
        print("You Win!!")
    if incorrect_ans_cnt < 0:
        still_guessing = False
        print("You Lose")
        print(f"Word is: {chosen_word}")
    print()
