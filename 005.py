'''
005: Smallest Multiple

Newton Ni
'''

import sys
from util import probablePrime

# Increment by the LCM of primes
inc = 3
for i in range(4, int(sys.argv[1])):
    if probablePrime(i, 10):
        inc *= i

n = 0
while (True):
    n += inc
    for i in range(int(sys.argv[1]), 1, -1):
        if (n % i != 0):
            break
    else:
        print n
        break
