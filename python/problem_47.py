def getDistinctPrimeFactors(n, primes):
  factors = set()
  i = 0
  while n != 1:
    if len(primes) == i:
      return set([n])

    prime = primes[i]
    if n % prime == 0:
      factors.add(prime)
      n //= prime
      i = 0
    else:
      i += 1

  return factors


def getConsecutiveDistinctPrimeFactors(sequence = 2):
  primes = []
  first = None
  i = 2
  while True:
    factors = getDistinctPrimeFactors(i, primes)
    if len(factors) == 1:
      prime = list(factors)[0]
      primes.append(prime)
    if len(factors) != sequence:
      first = None
    elif first == None:
        first = i
    elif first + sequence - 1 == i:
      return first
    i += 1

print(getConsecutiveDistinctPrimeFactors(4))
