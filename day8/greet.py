# Learning Functions

def greet():
    print("Hello")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today!")

greet()
print()

def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do {name}?")
    print("Hope the weather is nice!")

greet_with_name("Robert")
print()


def greet_with(name, location):
    print(f'Hi {name},')
    print(f'Thanks for joining us all the way from {location}')

# using positinal arguements
greet_with('Rob', 'Washington D.C')
print()

# using keyword arguments
greet_with(name='Biggie Smalls', location='Brooklyn, New York')
