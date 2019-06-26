"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
""" 

def largest_palindrome(nro_limit):
  nro = str(nro_limit)
  L = len(nro)
  c = int(L/2)
  while nro[:c] != nro[c:][::-1]:
    nro = str(int(nro) - 1)
    L = len(nro)
    c = int(L/2)
  return int(nro)
      
def find_divisors(nro, digits):
  div = int('9'*digits)
  divisors = False
  while len(str(div)) == digits:
    if nro % div == 0:
      if len(str(int(nro/div))) == digits:
        divisors = [div, int(nro/div)]
        break
      else:
        div -= 1
    else:
      div -= 1
  return divisors
 
ans = False
limite = 999*999
while ans == False:
  pal = largest_palindrome(limite)
  ans = find_divisors(pal, 3)
  limite = pal - 1
  
print("El mayor palíndromo formado por el producto de dos nros. de 3 cifras es {0} = {1} + {2}".format(pal, ans[0], ans[1]))
  
