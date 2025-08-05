def fillMultiplier(
    digits={"1", "2", "3", "4", "5", "6", "7", "8", "9"}, multiplicant="", multiplier=""
):
    products = set()
    for digit in digits:
        remainingDigits = digits.copy()
        remainingDigits.remove(digit)
        multiplier += digit
        product = str(int(multiplicant) * int(multiplier))
        if (
            "0" not in product
            and len(product + multiplicant + multiplier) == 9
            and len(set([*list(multiplicant), *list(multiplier), *list(product)])) == 9
        ):
            print(multiplier, multiplicant, product)
            products.add(int(product))
        products.update(fillMultiplier(remainingDigits, multiplicant, multiplier))
        multiplier = multiplier[:-1]
    return products


def fillMultiplicant(
    digits={"1", "2", "3", "4", "5", "6", "7", "8", "9"}, multiplicant=""
):
    products = set()
    for digit in digits:
        remainingDigits = digits.copy()
        remainingDigits.remove(digit)
        multiplicant += digit
        products.update(fillMultiplier(remainingDigits, multiplicant))
        products.update(fillMultiplicant(remainingDigits, multiplicant))
        multiplicant = multiplicant[:-1]
    return products


# products = fillMultiplicant()
# print(products)
# print(sum(products))


def bruteForce():
    mem = set()
    for i in range(1, 3333):
        for j in range(i, 3333):
            if i * j in mem:
                continue
            digits = set()
            digits.update(str(i), str(j), str(i * j))
            if (
                len(digits) == 9
                and "0" not in digits
                and len(str(i) + str(j) + str(i * j)) == 9
            ):
                mem.add(i * j)
    return mem


products = bruteForce()
print(products)
print(sum(products))
