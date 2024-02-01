#  This is the encode/decode program.
#  It takes user input and either encrypts/decrypts the text entered.
#  It was how Caesar decryped/encrypted messages by know how far to shift the letters.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# combinin encrypt/decrypt functions
def caesar(user_text, shift_number, user_dir):
    end_text = ''
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            if user_dir == 'encode':
                new_position = position + shift_number
                if new_position > len(alphabet) - 1:
                    new_position = new_position - len(alphabet)
            elif user_dir == 'decode':
                new_position = position - shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {user_dir}d text is: {end_text}')

# checks that the shift number is not too large (greater than 25)
def shift_check(shift_number):
    ask_again = True
    while ask_again == True:
        new_shift = int(input("Please Enter an shift number between 0 - 25: \n"))
        if new_shift > 25 or new_shift < -25:
            ask_again = True
            print("You entered an invalid number: Try Again! \n")
        else:
            ask_again = False
            return new_shift

# User Input
print(logo)
print()
print()
cont = True
while cont == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    if shift > 25 or shift < -25:
        shift = shift_check(shift)
    caesar(text, shift, direction)
    result = input('Do you want to go again? (Y/n) ').lower()
    if result == 'y' or result == 'yes':
        cont = True
    else:
        cont = False
print("GoodBye!")
