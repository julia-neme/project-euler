"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(min, max):
  import numpy as np
  serie = np.arange(min, max+1, 1)
  sum_of_sq = np.sum(serie**2)
  return sum_of_sq
  
def square_of_sum(min, max):
  import numpy as np
  serie = np.arange(min, max+1, 1)
  sq_of_sum = np.sum(serie)**2
  return sq_of_sum
  
ans = sum_of_squares(1, 100) - square_of_sum(1, 100)
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {0}".format(ans))
