# Calculator
import sys
from art import logo

print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply 
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1 , n2):
    return n1 / n2

operations  = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        # opertation symbol check
        if operation_symbol not in ("+", "-", "*", "/"):
            print(f"'{operation_symbol}' is not a valid option - please try again!")
            print("Exiting Program!!")
            sys.exit()  
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        keep_result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start with a new calculation, or 'q' to quit: ").lower()
        if keep_result == 'y' or keep_result == 'yes':
            num1 = answer
        elif keep_result == 'n' or keep_result == 'no':
            should_continue = False
            calculator()
        else:
            print("Exiting Calculator Progam - Have A Good Day!!")
            sys.exit()

calculator()
