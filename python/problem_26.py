def recurringFractionCycle(dividend, divisor):
    i = 0
    divisors = {}

    while dividend != 0:
        if dividend % divisor == 0:
            return 0
        elif dividend // divisor == 0:
            dividend *= 10
        else:
            if dividend in divisors:
                return i - divisors.get(dividend)
            divisors[dividend] = i
            dividend %= divisor
            i += 1
    return 0


def findMaxRecurringCycle():
    maxNum = 0
    maxCycle = 0

    for i in range(2, 1000):
        if (cycle := recurringFractionCycle(1, i)) > maxCycle:
            maxNum = i
            maxCycle = cycle
    return maxNum, maxCycle


print(findMaxRecurringCycle())
