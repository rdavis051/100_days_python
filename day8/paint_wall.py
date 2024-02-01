import math

banner = """
#######################################
Welcome to the paint calculator Program
#######################################
"""

print()
height = int(input("What is the height of the wall? "))
width = int(input("What is the width of the wall? "))
coverage = 5

def paint_calc(height, width, coverage):
        number_of_cans = (height * width) / coverage
        print(f'The actually calculation is: {number_of_cans}')
        print(f"You'll need {math.ceil(number_of_cans)} cans of paint")

paint_calc(height, width, coverage)

