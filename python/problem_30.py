def fifthPowerSum(numbers):
    return sum([number**5 for number in numbers])


def bruteForce():
    sum = 0

    for i in range(10, 1_000_000):
        if i == fifthPowerSum([int(n) for n in list(str(i))]):
            print(i)
            sum += i
    return sum


print(bruteForce())
