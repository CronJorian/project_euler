import math
def getPrimes(limit=1_000_000):
  primes = []
  for i in range(2, limit):
    isPrime = True
    for p in primes:
      if p > i**0.5 + 1:
        break
      if i % p == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(i)
  return primes

def bruteForce():
  maxTarget = (0, None)

  primes = getPrimes()
  i = 0
  ts = 0
  while ts < 1000000:
    ts += primes[i]
    i += 1
  termLimit = i
  
  for t, targetPrime in enumerate(reversed(primes)):
    if termLimit < maxTarget[0]:
      return maxTarget
    if sum(primes[:termLimit]) > targetPrime:
      termLimit -= 1

    l = 0
    u = maxTarget[0] + 1
    
    while l < u and u < targetPrime:
      s = sum(primes[l:u+1])
      if s < targetPrime:
        u += 1
      elif s > targetPrime:
        l += 1
      elif s == targetPrime and maxTarget[0] < u - l + 1:
        maxTarget = (u - l + 1, targetPrime)
        print(f"new max {targetPrime} length {u-l + 1} from {primes[l]} to {primes[u]}")
      else:
        u += 1
  return maxTarget

print(bruteForce())