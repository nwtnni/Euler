import sys
from math import sqrt
from util import probablePrime

'''
003: Largest Prime Factor
'''

n = int(sys.argv[1])
for i in range(int(sqrt(n)), 0, -1):
    if (n % i == 0):
        if (probablePrime(i, 10)):
            print i
            break
