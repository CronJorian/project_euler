def bruteForce():
  Tn = lambda n: n*(n + 1)/2
  Pn = lambda n: n*(3*n - 1)/2
  Hn = lambda n: n*(2*n - 1)

  Tcounter = 1
  Pcounter = 1
  Hcounter = 144

  while True:
    H = Hn(Hcounter)
    while Tn(Tcounter) < H:
      Tcounter += 1
    while Pn(Pcounter) < H:
      Pcounter += 1
    
    if H == Pn(Pcounter) and H == Tn(Tcounter):
      return H

    Hcounter += 1

print(bruteForce())