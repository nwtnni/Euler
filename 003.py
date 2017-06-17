'''
003: Largest Prime Factor

Newton Ni
'''

import sys
from math import sqrt
from primes_util import probable_prime

LIMIT = 600851475143

if __name__ == "__main__":
    
    for i in range(int(sqrt(LIMIT)), 0, -1):
        if (LIMIT % i == 0) and probable_prime(i):
            print i
            break
