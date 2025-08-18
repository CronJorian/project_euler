def getPrimes(limit):
    memory = []
    for i in range(2, limit):
        if isPrime(i, memory):
            memory.append(i)
    return set(memory)


def isPrime(number, memory):
    for prime in memory:
        if number % prime == 0 and number != prime:
            return False
        if prime > int((number**0.5) + 1):
            return True
    return True


def getCircularNumbers(number):
    numbers = [number]
    number = str(number)

    for _ in range(1, len(number)):
        letter = number[0]
        number = number[1::] + letter
        numbers.append(int(number))
    return numbers


def getCircularPrimes(primes):
    primes = sorted(primes)
    circularPrimes = set()
    for prime in primes:
        if prime not in circularPrimes:
            circularNumbers = getCircularNumbers(prime)
            if all(
                [isPrime(circularNumber, primes) for circularNumber in circularNumbers]
            ):
                circularPrimes.update(circularNumbers)
    return circularPrimes


primes = getPrimes(1000000)
circularPrimes = getCircularPrimes(primes)
print(circularPrimes)
print(len(circularPrimes))
