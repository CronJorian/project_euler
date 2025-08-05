def useCoin(amount=200, coins=[200, 100, 50, 20, 10, 5, 2, 1]):
    combinations = 0
    for coin in coins:
        if amount - coin == 0:
            combinations += 1
        elif amount - coin > 0:
            combinations += useCoin(amount - coin, [c for c in coins if c <= coin])
    return combinations


print(useCoin())
