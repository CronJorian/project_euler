primes = set([2,3,5,7])
prime_digits = set([2,3,5,7])

def isPrimeWithMemory(num, primes):
  limit = int(num**0.5) + 1

  for i in filter(lambda prime: prime < limit, primes):
    if num % i == 0:
      return False
  return True

def brute_force():
  sum = 0
  counter = 0 # used to register all 11 target primes
  i = 10
  while counter < 11:
    if isPrimeWithMemory(i, primes):
      primes.add(i)
      if (int(str(i)[0]) not in prime_digits or int(str(i)[-1:]) not in prime_digits):
        i += 1
        continue
      left = i
      right = i
      isValid = True
      while left > 0 and isValid:
        if left not in primes:
          isValid = False
        left = left // 10
      while right > 0 and isValid:
        if right not in primes:
          isValid = False
        right = right % 10**(len(str(right)) - 1)
      if isValid:
        sum += i
        counter += 1
        print(counter, i)
    i += 1
  return sum

# print(brute_force())

def isPrime(num):
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True
  

def build_suffix():
  suffix_digits = [3,7]
  primes_infixes = []
  for suffix in suffix_digits:
    primes_infixes.extend(build_infix(suffix))
  
  right_side_primes = []
  for infix in [*suffix_digits, *primes_infixes]:
    right_side_primes.extend(build_prefix(infix))
  return right_side_primes


def build_infix(suffix):
  infix_digits = [1,3,7,9]
  primes = []

  for infix in infix_digits:
    number = infix * (10**len(str(suffix))) + suffix
    if isPrime(number):
      primes.append(number)
      primes.extend(build_infix(number))

  return primes


def build_prefix(infix):
  prefix_digits = [2,3,5,7]
  return [prefix * (10**len(str(infix))) + infix for prefix in prefix_digits if isPrime(prefix * (10**len(str(infix))) + infix)]

def build_primes():
  primes = []
  right_side_primes = build_suffix()
  for potential_prime in right_side_primes:
    left_side_prime = potential_prime // 10
    
    while left_side_prime // 10 > 0 and isPrime(left_side_prime):
      left_side_prime //= 10
    if left_side_prime // 10 == 0:
      primes.append(potential_prime)
  
  return primes

print(sum(build_primes()))
