def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True;

def createPrimePermutations(n, digits):
  if len(digits) == 0:
    if isPrime(n):
      return n

  for i in digits:
    if prime := createPrimePermutations(n * 10 + i, [digit for digit in digits if digit != i]):
      return prime


def createPrimePandigital(limit = 9):
  primes = []
  for i in range(limit, 0, -1):
    if prime := createPrimePermutations(0, list(range(i, 0, -1))):
      return prime

print(createPrimePandigital())