def diagonalSum(length):
    sum = 1
    for i in range(3, length + 1, 2):
        lastDiag = (i - 2) ** 2
        step = i - 1
        diags = 4 * (lastDiag + step) + 6 * step
        sum += diags
    return sum


diagonalSum(1001)
