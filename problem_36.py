# manual binary conversion if theres no bin function
def decToBin(dec):
  num = ""
  while dec > 0:
    rem = dec % 2
    num = str(rem) + num
    dec = dec // 2
  return "0b" + num

def isPalindrome(string):
  return string == string[::-1]

def getPalindromicSum(limit):
  sum = 0
  # Only odd numbers are relevant, as no leading zeroes are allowed
  for count in range(1, limit, 2):
    if isPalindrome(str(count)):
      binary = decToBin(count)[2:] # cutoff 0b prefix
      if isPalindrome(binary):
        sum += count
  return sum


print(getPalindromicSum(1000000))