""" 
100 Days Of Python - Day 10
This program will determine the days of the month.
"""
def is_leap(year):
    """
    This function returns whether it is a leap year or not.
    """
    leap_year = ''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
                leap_year = True
                return leap_year
            else:
                print("Not leap year")
                leap_year = False
                return leap_year
        else:
            print("Leap Year")
            leap_year = True
            return leap_year
    else:
        print("Not leap year")
        leap_year = False
        return leap_year

def days_in_month(usr_year, usr_month):
    """
    Returns the number of days in a month.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    new_month = usr_month - 1
    is_leap_year = is_leap(usr_year)
    if is_leap_year and usr_month == 2:
        days = 29
        return days
    days = month_days[new_month]
    return days

year = int(input("Please type a year to check: "))
month = int(input("Please enter month: "))
days = days_in_month(year, month)
print(f'number of days in that month is {days}!')
