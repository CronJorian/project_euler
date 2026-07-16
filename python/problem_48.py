print(str(sum([i**i for i in range(1,1001)]))[-10:])

s = 0
for i in range(1,1001):
  s += i**i
  s %= 10000000000
print(s)