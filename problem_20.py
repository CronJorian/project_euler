def factorialSum(num):
    prod = 1
    sum = 0
    for i in range(1, num + 1):
        prod *= i
    while prod > 0:
        sum += prod % 10
        prod = prod // 10
    return sum


print(factorialSum(100))
