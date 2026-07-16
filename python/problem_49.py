def getPrimes(limit=10000):
  primes = []
  for i in range(2, limit):
    isPrime = True
    for p in primes:
      if i % p == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(i)
  return primes

def bruteForce():
  sequences = []
  primes = getPrimes()
  for i, prime1 in enumerate(primes):
    for j, prime2 in enumerate(primes[i+1:]):
      if len(set(str(prime1)).symmetric_difference(str(prime2))) != 0:
        continue
      increase = prime2 - prime1
      if increase < 1000 or increase > 9999:
        continue
      if (prime3 := prime2 + increase) not in primes:
        continue
      if len(set(str(prime2)).symmetric_difference(str(prime3))) != 0:
        continue
      sequence = str(prime1) + str(prime2) + str(prime3)
      if len(sequence) == 12:
        sequences.append(sequence)
  return sequences

print(bruteForce())