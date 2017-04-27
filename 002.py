import sys

'''
002: Even Fibonacci Numbers
'''

a, b, c, sum = 1, 2, 0, 2

while (a + b < int(sys.argv[1])):
    c = a + b
    if (c % 2 == 0):
        sum += c
    a, b = b, c

print sum


