import random

# This program is a password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# User Input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
easy_pass = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    easy_pass += random_char
    print(easy_pass)

for char in range(1, nr_symbols + 1):
    easy_pass += random.choice(symbols)
    print(easy_pass)

for char in range(1, nr_numbers + 1):
    easy_pass += random.choice(numbers)
    print(easy_pass)

print(easy_pass)

# Hard Level
hard_pass = []

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    # You can add to a list using the '+=' operator
    hard_pass += random_char
    print(hard_pass)

for char in range(1, nr_symbols + 1):
    # or add to a listusing the 'append' method
    hard_pass.append(random.choice(symbols))
    print(hard_pass)

for char in range(1, nr_numbers + 1):
    hard_pass.append(random.choice(numbers))
    print(hard_pass)

# the 'shuffle' method that randomizes a list
random.shuffle(hard_pass)
print(hard_pass)

# convert back to a string
password = ""

for char in hard_pass:
    password += char

print(f'Your new password is: {password}')
