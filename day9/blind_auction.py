#########################
# Blind Auction Program #
#########################

# to clear screen. use os module system method with either 'clear' or 'cls' parameter. Ex: os.system('cls') or os.system('clear')
import os
from art import logo

bids = {}
winner_name = ''
winning_bid = 0
more_bidders = True

print(logo)
print()

# While loop to get name and bid
while more_bidders == True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bids[name] = price
    if next_bidder == 'yes':
        os.system('clear')
    else:
        more_bidders = False

print(bids)

for key in bids:
    if bids[key] > winning_bid:
        winner_name = key
        winning_bid = bids.get(key)

print()
print(f'{winner_name} is the winner of the auction, with a wining bid of ${winning_bid}!!')

# For loop to determine the highest bidder
