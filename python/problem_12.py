def triangle_divisors(limit):
    triangle_number = 1
    next_delta = 2
    while True:
        divisors = set()
        for i in range(1, int(next_delta + 1) // 2 + 1):
            if triangle_number % i == 0:
                divisors.add(i)
        if len(divisors) * 2 >= limit:
            print(divisors)
            print(triangle_number)
            return
        triangle_number += next_delta
        next_delta += 1


triangle_divisors(500)

