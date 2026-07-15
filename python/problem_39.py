def get_triples(p):
  triples = []
  for a in range(1,p // 2):
    r = p - a
    for b in range(1,r // 2):
      c = r - b
      if ((a**2 + b**2) == c**2):
        triples.append((a,b,c))
  return len(triples)

def brute_force():
  max = (0,0)
  for p in range(0, 1001):
    num_triples = get_triples(p)
    if num_triples > max[1]:
      max = (p, num_triples)
  return max

print(brute_force())