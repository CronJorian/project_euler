def getProperDivisors(number):
    divisors = [1]
    for i in range(2, int(number**0.5 + 1)):
        if number % i == 0:
            divisors.append(i)
            if number // i != i:
                divisors.append(number // i)
    return divisors


def isPerfect(number):
    return sum(getProperDivisors(number)) == number


def isAbundant(number):
    return sum(getProperDivisors(number)) > number


def isDeficient(number):
    return sum(getProperDivisors(number)) < number


def getNumberState(number):
    a = sum(getProperDivisors(number))
    b = number
    return 0 if a == b else -1 if a < b else 1


def bruteForce(limit):
    abundantSums = set(range(limit))
    abundantNumbers = []

    for i in range(1, limit + 1):
        if isAbundant(i):
            for a in abundantNumbers:
                abundantSums.discard(a + i)
            abundantSums.discard(i + i)
            abundantNumbers.append(i)
    return sum(abundantSums)


print(bruteForce(28123))
