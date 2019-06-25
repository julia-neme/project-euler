"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def serie_multiplos(N, mult):
  max_mult = int(N / mult)
  serie = []
  i = 1
  while i * mult < N:
    serie.append(i * mult)
    i = i + 1
  return serie

import numpy as np
serie_multiplos3 = serie_multiplos(1000, 3)
serie_multiplos5 = serie_multiplos(1000, 5)
serie_multiplos3_5 = set(serie_multiplos3 + serie_multiplos5)
suma = np.sum(np.array(list(serie_multiplos3_5)))
print("La suma de todos los números múltiplos de 3 o 5 menores a 1000 es {0}".format(suma))

