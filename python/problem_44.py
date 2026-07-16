def isPentagonal(pn):
  n = (1/6) + ((1 + 24*pn)**0.5) / 6
  if n % 1 == 0:
    return True
  return False

def bruteForce():
  ds = {}
  memory = set()
  n = 1
  while len(ds) < 20:
    pn = int(n*(3*n - 1) / 2)
    for pj in memory:
      sum_pn = pn + pj
      diff_pn = abs(pn - pj)
      if isPentagonal(sum_pn) and isPentagonal(diff_pn):
        ds[diff_pn] = (pn, pj)
        print(diff_pn, pn, pj)
    memory.add(pn)
    n += 1
  

print(bruteForce())
