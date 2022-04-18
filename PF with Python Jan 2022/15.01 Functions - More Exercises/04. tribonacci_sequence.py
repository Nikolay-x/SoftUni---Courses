# 4.Tribonacci Sequence
# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. You will receive a positive integer number as input.
#
# Input
# 4
#
# Output
# 1 1 2 4

def tribonacci_sequence(n):
  num_list = []
  for i in range(1, n + 1):
    if i == 1 or i == 2:
      num_list.append(1)
    elif i == 3:
      num_list.append(2)
    else:
      num_list.append(num_list[-1] + num_list[-2] + num_list[-3])
  str_num_list = list(map(str, num_list))
  result = " ".join(str_num_list)
  return result

x = int(input())
print(tribonacci_sequence(x))
