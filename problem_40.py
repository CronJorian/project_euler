def brute_force():
  fracs = ''.join([str(i) for i in range(1000000)])
  indices = [10 ** i for i in range(7)]
  
  prod = 1
  for i in [fracs[i] for i in indices]:
    print(i)
    prod *= int(i)
  return prod


def calculate_digit(index):
  digit_len = 1
  sum_len = 9 * 10**(digit_len - 1) * digit_len
  while index > sum_len:
    digit_len += 1
    index -= sum_len
    sum_len = 9 * 10**(digit_len - 1) * digit_len
  
  skip_nums = index // digit_len
  digit_index = index % digit_len - 1 

  target_num = 10**(digit_len - 1) + skip_nums
  target_digit = str(target_num)[digit_index]

  return int(target_digit)

def space_efficient_solution():
  product = 1
  for i in range(7):
    digit = calculate_digit(10**i)
    print(digit)
    product *= digit
  return product

print(calculate_digit(0))
print(calculate_digit(1))
print(calculate_digit(2))
print(calculate_digit(3))
print(calculate_digit(4))
print(calculate_digit(5))
print(calculate_digit(6))
print(calculate_digit(7))
print(calculate_digit(8))
print(calculate_digit(9))
print(calculate_digit(10))
print(calculate_digit(11))
print(calculate_digit(12))
print(calculate_digit(13))
print(calculate_digit(14))
print(calculate_digit(15))
print(calculate_digit(16))
# print(space_efficient_solution())
