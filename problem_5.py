"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def serie_multiplos(N, mult):
  max_mult = int(N / mult)
  serie = []
  i = 1
  while i * mult < N:
    serie.append(i * mult)
    i = i + 1
  return serie

multiplos = []
for i in range(1, 21):
  a = serie_multiplos(21, i)
  multiplos = list(set(a+multiplos))
  
  
       
  
