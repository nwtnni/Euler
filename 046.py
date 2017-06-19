'''
046: Goldbach's Other Conjecture

Newton Ni
'''

from math import sqrt
from primes_util import probable_prime

if __name__ == "__main__":
     
    n = 33
    while True:
        n += 2
        if probable_prime(n): continue
        for m in range(1, n + 1):
            if probable_prime(n - 2*(m**2)):
                break
        else:
            print n
            break
