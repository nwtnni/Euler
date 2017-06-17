'''
007: 10001st Prime

Newton Ni
'''

from sys import argv
from primes_util import probable_prime

n, i = int(argv[1]) - 1, 1

while (n > 0):
    i += 2
    if (probable_prime(i)):
        n -= 1
print i

