def isPandigital(num, limit = 9):
  digits = [int(digit) for digit in str(num)]
  unique_digits = set(digits)
  consecutive_digits = range(1, limit + 1)
  
  if len(digits) != len(unique_digits) or unique_digits.difference(consecutive_digits):
    return False
  return True

def getMaxPandigital():
  max = 0
  
  for n in range(2, 10):
    for i in range(100000):
      num_string = ''.join([str(i * j) for j in range(1, n + 1)])
      if len(num_string) == 9:
        num = int(num_string)
        if isPandigital(num): 
          print(n, i, num)
          if num > max:
            max = num
  return max


print(getMaxPandigital())