# Leap year progam - determins if a year is a leap year.

def is_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    year = input('What year do you want to check? ')
    check_year = is_leapyear(int(year))
    if check_year == True:
        print(f'YES! {year} is a leap year.')
    else:
        print('No! that is not a leap year')
