# this is a number guessing game
import sys
from random import randint
import art

print(art.logo)
print()

def another_guess(number):
    if number > 0:
        return True
    else:
        return False

def play_game(attempts):
    """start guessing game with specfic number of attempts"""
    selected_number = randint(1, 100)
    attempts_counter = attempts
    continue_guessing = True
    while continue_guessing:
        print(f"You have {attempts_counter} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > selected_number:
            print("Too High.")
            print("Guess again")
            attempts_counter -= 1
            continue_guessing = another_guess(attempts_counter)
        elif guess < selected_number:
            print("Too Low.")
            print("Guess again.")
            attempts_counter -= 1
            continue_guessing = another_guess(attempts_counter)
        elif guess == selected_number:
            print("You Win - You guessed correctly")
            print(f"The randomly generated number was: {selected_number}")
            continue_guessing = False
    if attempts_counter == 0:
        print(f"You are out of guesses - the random generated number was: {selected_number}")
        print("You Lose!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5
else:
    print("You typed an incorrect option - try again!")
    sys.exit()
# start game
play_game(guesses)
