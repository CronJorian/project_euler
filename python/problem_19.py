daysOfMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def bruteForce():
    day = 1
    month = 1
    year = 1900
    dayOfWeek = 1
    firstOfMonthSunday = 0

    while year < 2001:
        if day == 1 and dayOfWeek == 7 and year >= 1901:
            firstOfMonthSunday += 1
        if isLeapYear(year):
            daysOfMonth[2] = 29
        else:
            daysOfMonth[2] = 28
        day += 1
        dayOfWeek += 1
        if dayOfWeek > 7:
            dayOfWeek = 1
        if day > daysOfMonth[month]:
            day = 1
            month += 1
        if month > 12:
            month = 1
            year += 1
    return firstOfMonthSunday

print(bruteForce())
