# A program that does a factorial calculation
# Not part of the 100 day of python course, just wanted to test my knowlege after the first
# capeston project.
import art

print(art.factorial_logo)
print()

def factorial(num):
    """takes number and recurivley return the answer"""
    if num == 1:
        num = num * 1
    else:
        num = num * factorial(num - 1)
    return num

number = int(input("Please enter a factoral number: "))
fac = factorial(number)
print(fac)
