faculties = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
}


def bruteForce():
    numbers = []
    # limit is based on comments on the forum, my own limit was brute forced
    # limit is factorial of highest digit times the number of digits
    num_digits = 10
    fac_9 = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    limit = fac_9 * num_digits + 1
    for number in range(0, limit):
        digits = [int(letter) for letter in str(number)]
        if number == sum([faculties[digit] for digit in digits]):
            numbers.append(number)
    # remove the first two numbers as they are no sums
    numbers = numbers[2::]
    print(numbers)
    return sum(numbers)


print(bruteForce())
