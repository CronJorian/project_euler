primes = []
def isPrime(n):
  if n == 1:
    return False
  for i in primes:
    if i > n ** 0.5:
      primes.append(n)
      return True
    if n % i == 0:
      return False
  primes.append(n)
  return True

def isComposable(n):
  f = lambda p,s: p + 2*(s**2)

  for p in primes:
    if p >= n:
      return False
    
    i = 0
    while (c := f(p, i)) <= n:
      if c == n: 
        return True
      i += 1
  return False


def bruteForce():  
  i = 2
  while True:
    if not isPrime(i) and i % 2 == 1:
      if not isComposable(i):
        return i
    i += 1
  
print("not composable: ", bruteForce())