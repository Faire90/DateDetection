import re

day = 0
month = 0
year = 0

def CheckDateValidity(day, month, year):
    months30days = [4, 6, 9, 11]
    if month in months30days:
        if day <= 30:
            return True
        else:
            return False
    elif month == 2:
        if day > 29:
            return False
        elif day <= 28:
            return True
        elif day == 29:
            if year%4 == 0:
                if year%100 != 0:
                    return True
                elif year%400 == 0:
                    return True
                else:
                    return False
            else:
                return False
    elif month not in months30days:
        if month <= 12:
            if day <= 31:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

dateDetectionRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
print('Input string with date in the form DD/MM/YYYY:')
while True:
    searchString = input()
    date = dateDetectionRegex.search(searchString)
    if date != None:
        day = (int(date.group(1)))
        month = (int(date.group(2)))
        year = (int(date.group(3)))
        break
    else:
        print('Please enter a string with a date in the form DD/MM/YYYY:')
valid = CheckDateValidity(day, month, year)
if valid == True:
    print('The date entered is a valid date.')
elif valid == False:
    print('The date entered is not a valid date.')
else:
    print('There was an error processing the date.')

