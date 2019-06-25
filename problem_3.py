"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime_factor(nro):
    i = 2
    while i * i < nro:
        while nro % i == 0:
            nro = nro / i
        i = i + 1
    return nro

anw = largest_prime_factor(600851475143)
print("El mayor número primo que divide a 600851475143 es {0}".format(anw))
