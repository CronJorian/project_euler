def properDivisors(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    divisors = list(sorted(divisors))
    return divisors


def amicableNumberRange(limit):
    memory = {}
    for i in range(1, limit + 1):
        if i in memory:
            continue
        sumDivisors = sum(properDivisors(i))
        amica = sum(properDivisors(sumDivisors))
        if sumDivisors != i and amica == i:
            memory[sumDivisors] = i
    print(memory)
    return sum(memory.keys()) + sum(memory.values())


print(amicableNumberRange(10000))
