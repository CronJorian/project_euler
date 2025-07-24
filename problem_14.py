def collatz_max(limit):
    memory = {}
    max_val = 0
    max_key = 0
    for i in range(1, limit + 1):
        j = i
        steps = 1
        while True:
            if j == 1:
                memory[i] = steps
                if memory[i] > max_val:
                    max_key = i
                    max_val = memory[i]
                break

            if j in memory:
                memory[i] = memory[j] + steps - 1
                if memory[i] > max_val:
                    max_key = i
                    max_val = memory[i]
                break

            if j % 2 == 0:
                j //= 2
            else:
                j = 3 * j + 1
            steps += 1
    print(max_key, max_val)


collatz_max(1_000_000_0)

