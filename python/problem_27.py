def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def bruteForce():
    primes = set()
    maxStreak = 0
    maxA, maxB = None, None

    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            streak = 0
            while True:
                result = n**2 + a * n + b
                if result in primes:
                    n += 1
                    streak += 1
                elif isPrime(result):
                    n += 1
                    streak += 1
                    primes.add(result)
                else:
                    if streak >= maxStreak:
                        maxStreak = streak
                        maxA, maxB = a, b
                    break
    return maxA * maxB


print(bruteForce())
