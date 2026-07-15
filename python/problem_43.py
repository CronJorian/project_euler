def hasInterestingProperty(s):
  divisors = {2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 13, 8: 17}
  if all([int(s[i-1:i+2]) % div == 0 for i, div in divisors.items()]):
    return s
  return "0"

def getPermutations(n = "", digits = ["1","2","3","4","5","6","7","8","9","0"]):
  if len(digits) == 0:
    return [n]
  
  perms = []  
  for i in digits:
    if len(n) == 0 and i == "0":
      continue
    perms.extend(getPermutations(n + i, [digit for digit in digits if i != digit]))
  return perms

def bruteForce():
  perms = getPermutations()
  return sum([int(hasInterestingProperty(n)) for n in perms])

print(bruteForce())
