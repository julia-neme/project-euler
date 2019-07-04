"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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

primos = eratosthenes_sieve(10)
exp = []
for i in primos:
  exp.append(get_largest_exp(10, i))
primos_elevados = primos**exp
ans = 1
for x in primos_elevados:
  ans = ans*x

print("El menor nro. positivo multiplo de todos los nros. del 1 al 20 es {0}".format(ans))
      
  
  
  
       
  
