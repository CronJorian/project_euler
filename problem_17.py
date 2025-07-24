import re

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def getWord(number):
    s = ""
    if number == 1000:
        return "one thousand"
    elif number // 100 > 0:
        s += numbers[number // 100] + " " + numbers[100]
        number %= 100
        if number != 0:
            s += " and "
    if number in numbers:
        s += numbers[number]
    elif ((number // 10) * 10) in numbers:
        s += numbers[((number // 10) * 10)] + "-" + numbers[number % 10]
    return s


def countLetters(word):
    return len(re.sub("[ -]+", "", word))


def getWordNumberLength(number):
    return countLetters(getWord(number))


cnt = 0
for i in range(1, 1001):
    cnt += getWordNumberLength(i)
print(cnt)
