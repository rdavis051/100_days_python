# tip_calculatr.py
# day 2 of 100 days of python
# program gets the total from a bill, people, percent and how much each person owes

if __name__=='__main__':
    print('Welcome to the tip calculator.')
    bill = input('What was the total bill? $')
    people = input('How many people to split the bill? ')
    percent = input('What percentage tip would you like to give? 10, 12, or 15? ')
    tip = float(bill) * (int(percent)/100)
    bill = float(bill) + float(tip)
    amount_owed = round(bill/int(people), 2)
    amount_owed = "{:.2f}".format(amount_owed)
    print(f"Each person should pay: ${amount_owed}")

