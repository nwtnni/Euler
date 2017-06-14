'''
019: Counting Sundays

Newton Ni
'''

month_to_day = {
    0: 31, 1: 28, 2: 31,
    3: 30, 4: 31, 5: 30,
    6: 31, 7: 31, 8: 30,
    9: 31, 10: 30, 11: 31
    }

if __name__ == "__main__":

    year = 1

    month = 0
    weekday = 2

    sundays = 0

    while year < 100:

        # Check Sunday
        if weekday == 0:
            sundays += 1

        # Next month
        weekday = (weekday + month_to_day[month]) % 7
        month += 1

        if (month == 1 and year % 4 == 0):
            if year % 100 == 0:
                if year % 400 == 0:
                    weekday = (weekday + 1) % 7
            else:
                weekday = (weekday + 1) % 7

        # Next year
        if month >= 12:
            year += 1
            month = 0
    
    print sundays
     
