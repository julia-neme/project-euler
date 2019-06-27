"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def get_largest_mult(serie):
  serie_ord = list(set(serie))
  mult = []
  mult.append(serie_ord[-1])
  i = -2
  while abs(i) < len(serie_ord):
    is_mult = True
    for m in mult:
      if m % serie_ord[i] == 0:
        is_mult = False

    if is_mult:
      mult.append(serie_ord[i])
    i -= 1
  return mult
  
  
       
  
