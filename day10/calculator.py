# Calculator

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

# Get first number
num1 = int(input("What's the first number?: "))
# print optional sybols
for symbol in operations:
    print(symbol)
# get operation user wants to use
operator = input("Please select an operator from the list above: ")
# Get second number
num2 = int(input("What's the second number?: "))
#print(f"you chose to {operator} the two inputs of {num1} & {num2}")

function = operations[operator]
result = function(num1, num2)
print(f"Result: {num1} {operator} {num2} =  {result}")
print()
answer = input("Do you want to continue? (Y/n): ").lower()
if answer == 'y':
    continue_operations = True
else:
    continue_operations = False

while continue_operations:
    num = int(input("Please enter an new number: "))
    operator = input("Please enter a new operator: ")
    function = operations[operator]
    new_result = function(result, num)
    print(f'{result} {operator} {num} = {new_result}')
    result = new_result
    answer = input("Do you want to continue? (Y/n): ").lower()
    if answer == 'y':
        continue_operations = True
    else:
        continue_operations = False