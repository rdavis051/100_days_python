import os
import random
from art import logo, vs
from game_data import data

def compare_followers(a_followers_cnt, b_followers_cnt):
    """ Compare IG account followers - return the account with the most followers"""
    if a_followers_cnt > b_followers_cnt:
        return "a"
    elif a_followers_cnt < b_followers_cnt:
        return "b"
    else:
        return "draw"

def start_game():
    correct_guess_cnt = 0
    total_guess_cnt = 0
    draws = 0
    #while loop the keep going until the user guesses wrong
    user_correct = True
    # set intial B account
    account_b = random.choice(data)

    while user_correct:
        os.system('clear')
        # generate random account
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        print(logo)
        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")
        more_followers = compare_followers(account_a['follower_count'], account_b['follower_count'])
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a':
            if more_followers == 'a':
                correct_guess_cnt += 1
            elif more_followers == 'draw':
                print("There was a draw - moving to new IG profiles!")
                draws += 1
            else:
                user_correct = False
        elif guess == 'b':
            if more_followers == 'b':
                correct_guess_cnt += 1
            elif more_followers == 'draw':
                print("There was a draw - moving to new IG profiles!")
                draws += 1
            else:
                user_correct = False
        else:
            print("You choose and invalid option - 'A' and 'B' only accepted - TRY AGAIN!")

        if user_correct == False and draws > 0:
            print(f"Sorry, that's wrong. Final score: {correct_guess_cnt} - Draws were: {draws}")
        elif user_correct == False:
            print(f"Sorry, that's wrong. Final score: {correct_guess_cnt}")
        
start_game()
