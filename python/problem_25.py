def getIndexOfFibonacciWithNDigits(n):
    a, b, i = 0, 1, 1

    while len(str(b)) < n:
        i += 1
        a, b = b, a + b
    return i


print(getIndexOfFibonacciWithNDigits(1000))
