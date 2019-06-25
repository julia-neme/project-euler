"""
El ejercicio pide calcular la suma de todos los números múltiplos de 3 o 5 menores a 1000.
"""

def es_multiplo(nro):
  x = False
  for i in [3, 5]:
    if nro % i == 0:
      x = True 
      break
  return x

multiplos = []
for i in range(1, 1000):
  x = es_multiplo(i)
  if x:
    multiplos.append(i)

import numpy as np

suma = np.sum(np.array(multiplos))
print("La suma de todos los números múltiplos de 3 o 5 menores a 1000 es {0}".format(suma))

"""
Pruebo un enfoque más eficiente
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

