'''
006: Sum Square Difference

Newton Ni
'''

import sys

n, squaresum = int(sys.argv[1]), 0
for i in range(n + 1):
    squaresum += i * i
sumsquare = ((n * (n + 1)) / 2)
print(sumsquare * sumsquare - squaresum)
