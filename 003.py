'''
003: Largest Prime Factor

Newton Ni
'''

import sys
from math import sqrt
from primes_util import probable_prime

n = int(sys.argv[1])
for i in range(int(sqrt(n)), 0, -1):
    if (n % i == 0):
        if (probable_prime(i, 10)):
            print i
            break
