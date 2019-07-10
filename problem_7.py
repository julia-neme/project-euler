"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(N):
  i = 2
  ans = True
  while i*i <= N:
    if N % i == 0:
      ans = False
      break
    else:
      i += 1
  return ans

def get_largest_exp(N_max, N):
  import numpy as np
  max_exp = int(np.log(N_max)/np.log(N))
  return max_exp

def eratosthenes_sieve(N_max):
  import numpy as np
  serie = np.arange(1, N_max + 1, 1)
  sieve = [True] * len(serie)
  i = 1
  while i < len(serie):
    if sieve[i]:
      if is_prime(serie[i]):
        max_exp = get_largest_exp(np.max(serie), serie[i])
        j = 2
        while j <= max_exp:
          sieve[serie[i]**j - 1] = False
          j += 1
      else:
        sieve[i] = False
    i += 1
  return serie[1:][sieve[1:]]
