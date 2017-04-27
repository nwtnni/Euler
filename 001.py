'''
001: Multiples of 3 and 5

Newton Ni
'''

import sys

sum = 0;
for i in range(int(sys.argv[1])):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print sum
