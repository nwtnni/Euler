'''
007: 10001st Prime

Newton Ni
'''

from sys import argv
from util import probablePrime

n, i = int(argv[1]) - 1, 1

while (n > 0):
    i += 2
    if (probablePrime(i, 5)):
        n -= 1
print i

