print('''Hello! This is a program to find out what day of the week you were born on.
''')
# This program works for any date after 1900 unless it is in Jan or Feb of a leap year.

print('What month were you born in? Jan, Feb, Mar, ect.')


while True:
    in_month = input()
    if (in_month == 'Jan') or (in_month == 'jan') or (in_month == 'JAN') or (in_month == 'january') or (in_month == 'January') or (in_month == 'JANUARY') or (in_month == '1'):
        month_value = 6
        break
    elif (in_month == 'Feb') or (in_month == 'feb') or (in_month == 'FEB') or (in_month == 'February') or (in_month == 'february') or (in_month == 'FEBRUARY') or (in_month == '2') :
        month_value = 2
        break
    elif (in_month == 'Mar') or (in_month == 'mar') or (in_month == 'MAR') or (in_month == 'March') or (in_month == 'march') or (in_month == 'MARCH') or (in_month == '3') :
        month_value = 2
        break
    elif (in_month == 'Apr') or (in_month == 'apr') or (in_month == 'APR') or (in_month == 'April') or (in_month == 'april') or (in_month == 'APRIL') or (in_month == '4') :
        month_value = 5
        break
    elif (in_month == 'May') or (in_month == 'may') or (in_month == 'MAY') or (in_month == '5') :
        month_value = 0
        break
    elif (in_month == 'Jun') or (in_month == 'jun') or (in_month == 'JUN') or (in_month == 'June') or (in_month == 'june') or (in_month == 'JUNE') or (in_month == '6') :
        month_value = 3
        break
    elif (in_month == 'Jul') or (in_month == 'jul') or (in_month == 'JUL') or (in_month == 'July') or (in_month == 'july') or (in_month == 'JULY') or (in_month == '7') :
        month_value = 5
        break
    elif (in_month == 'Aug') or (in_month == 'aug') or (in_month == 'AUG') or (in_month == 'August') or (in_month == 'august') or (in_month == 'AUGUST') or (in_month == '8') :
        month_value = 1
        break
    elif (in_month == 'Sep') or (in_month == 'sep') or (in_month == 'SEP') or (in_month == 'September') or (in_month == 'september') or (in_month == 'SEPTEMBER') or (in_month == '9') :
        month_value = 4
        break
    elif (in_month == 'Oct') or (in_month == 'oct') or (in_month == 'OCT') or (in_month == 'October') or (in_month == 'october') or (in_month == 'OCTOBER') or (in_month == '10') :
        month_value = 6
        break
    elif (in_month == 'Nov') or(in_month == 'nov') or (in_month == 'NOV') or (in_month == 'November') or (in_month == 'november') or (in_month == 'NOVEMBER') or (in_month == '11') :
        month_value = 2
        break
    elif (in_month == 'Dec') or (in_month == 'dec') or (in_month == 'DEC') or (in_month == 'December') or (in_month == 'december') or (in_month == 'DECEMBER') or (in_month == '12') :
        month_value = 4
        break
    print('Please enter a valid month.')

print('What day of the month were you born on? 1-31')
# If you type a word "invalid literal for int() with base 10" How do I get it to only accept an int?


while True :
    while True : 
        try :
            in_day = int(input())
            break
        except :
            print('Please enter the day of the month 1-31')
    if (in_day <= 31) and (in_day >= 1) :
        break
    else : 
        print('Please enter the day of the month 1-31')
month_plus_day = month_value + in_day

print('What decade were you born in? 1900,1910,1920, ect.')
while True:
    in_decade = input()

    if in_decade == '1900' :
        decade_value = 1
        break
    elif in_decade == '1910' :
        decade_value = 6
        break
    elif in_decade == '1920' :
        decade_value = 5
        break
    elif in_decade == '1930' :
        decade_value = 3
        break
    elif in_decade == '1940' :
        decade_value = 2
        break
    elif in_decade == '1950' :
        decade_value = 0
        break
    elif in_decade == '1960' :
        decade_value = 6
        break
    elif in_decade == '1970' :
        decade_value = 4
        break
    elif in_decade == '1980' :
        decade_value = 3
        break
    elif in_decade == '1990' :
        decade_value = 1
        break
    elif in_decade == '2000' :
        decade_value = 0
        break
    elif in_decade == '2010' :
        decade_value = 5
        break
    else :
        print('Please enter the year as 4 digits ending with a 0.')

month_day_dec = month_plus_day + decade_value

print('What year in that decade were you born in? 0,1,2,3, ect.')

if (in_decade == '1900') or (in_decade == '1920') or (in_decade == '1940') or (in_decade == '1960') or (in_decade == '1980') or (in_decade == '2000') :
    while True:
        in_year = input()

        if in_year == '0' :
            year_value = 0
            break
        if in_year == '1' :
            year_value = 0
            break
        if in_year == '2' :
            year_value = 0
            break
        if in_year == '3' :
            year_value = 0
            break
        if in_year == '4' :
            year_value = 1
            break
        if in_year == '5' :
            year_value = 1
            break
        if in_year == '6' :
            year_value = 1
            break
        if in_year == '7' :
            year_value = 1
            break
        if in_year == '8' :
            year_value = 2
            break
        if in_year == '9' :
            year_value = 2
            break
        else :
            print('Please enter a digit 0-9.')
if (in_decade == '1910') or (in_decade == '1930') or (in_decade == '1950') or (in_decade == '1970') or (in_decade == '1990') or (in_decade == '2010') :
    while True:
        in_year = input()

        if in_year == '0' :
            year_value = 0
            break
        if in_year == '1' :
            year_value = 0
            break
        if in_year == '2' :
            year_value = 1
            break
        if in_year == '3' :
            year_value = 1
            break
        if in_year == '4' :
            year_value = 1
            break
        if in_year == '5' :
            year_value = 1
            break
        if in_year == '6' :
            year_value = 2
            break
        if in_year == '7' :
            year_value = 2
            break
        if in_year == '8' :
            year_value = 2
            break
        if in_year == '9' :
            year_value = 2
            break
        else :
            print('Please enter a digit 0-9.')

final_sum = month_day_dec + year_value + int(in_year)

final_remainder = final_sum % 7

space = ' '
conclusion = (in_month + space + str(in_day) + space + str(int(in_year) + int(in_decade)))

if final_remainder == 0 :
    print(conclusion , 'was a Sunday.')
elif final_remainder == 1 :
    print(conclusion , 'was a Monday.')
elif final_remainder == 2 :
    print(conclusion , 'was a Tuesday.')
elif final_remainder == 3 :
    print(conclusion , 'was a Wednesday.')
elif final_remainder == 4 :
    print(conclusion , 'was a Thursday.')
elif final_remainder == 5 :
    print(conclusion , 'was a Friday.')
elif final_remainder == 6 :
    print(conclusion , 'was a Saturday')
else : 
    print('ERROR: Please try again')