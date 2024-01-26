# The point of this game is iterate from 1 to 100.
# For any number that is divisable by 3 print 'Fizz'.
# For any number that is divisable by 5 print 'Buzz'.
# For any number that is divisable by 3 and 5 print 'FizzBuzz'.

#** Note: (This is a question that is asked often on job interviews)**

target = 100
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

