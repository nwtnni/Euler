'''
044: Pentagon Numbers

Newton Ni
'''

from math import sqrt
from sys import exit

def pentagonal(n): return (n * (3 * n - 1)) / 2
def is_pentagonal(n): return (sqrt(24 * n + 1) + 1) % 6 == 0

if __name__ == "__main__":

    min = 9999999999

    for a in xrange(1, 100000):
        for b in xrange(a, 0, -1):

            x = pentagonal(a)
            y = pentagonal(b)

            if is_pentagonal(x + y) and is_pentagonal(x - y):
                print abs(x - y)
                exit(0)
