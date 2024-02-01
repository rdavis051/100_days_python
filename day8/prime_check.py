# write your code below this line.

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'Yes! {number} is prime!!')
    else:
        print("No, that's not a prime number")

# Do not change any of the code below
n = int(input("Enter number to check: "))
prime_checker(number=n)
