'''
039: Integer Right Triangles

Newton Ni
'''

from math import sqrt
from collections import Counter

if __name__ == "__main__":

    counter = Counter()

    for a in range(1, 1001):
        for b in range(1, 1001):
            c = sqrt(a**2 + b**2)
            p = a + b + int(c)
            counter[p] += 1 if c == int(c) and p <= 1000 else 0
    print counter.most_common(1)
