letters = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


def getFacultyBelow(number):
    prod = 1
    i = 1
    while prod * i < number:
        prod *= i
        i += 1
    return prod


def fac(number):
    prod = 1
    for i in range(1, number + 1):
        prod *= i
    return prod


def nthLexicographicPermutation(index, letters=letters):
    output = ""
    if index <= 0:
        return "".join(sorted(letters))
    elif index >= fac(len(letters)) - 1:
        return "".join(reversed(sorted(letters)))

    remainingLetters = letters
    position = index
    while len(remainingLetters):
        nextLetter = remainingLetters.pop(position // getFacultyBelow(position))
        output += nextLetter
        position = position % getFacultyBelow(position)
    return output


print(nthLexicographicPermutation(999999))
