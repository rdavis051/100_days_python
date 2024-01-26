import random

names_string = input("Please type the list of names of people at dinner: ")
print(names_string)

names = names_string.split(", ")
for x in names:
    print(x)

names_length = len(names)
print(names_length)

random_int = random.randint(0, names_length - 1)
print(random_int)

payer = names[random_int]

print(f"{payer} is going to pay for the meal today!")

