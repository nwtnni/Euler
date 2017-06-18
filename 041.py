'''
041: Pandigital Prime

Newton Ni
'''

from primes_util import probable_prime
from itertools import permutations

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

if __name__ == "__main__":
    
    max = 0
    while len(DIGITS) > 4:
        for n in permutations(DIGITS):
            n = int(reduce(lambda a, b: str(a) + str(b), n))
            if probable_prime(n):
                max = n if n > max else max
        DIGITS.pop(-1)
    print max

