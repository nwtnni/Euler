'''
012: Highly Divisible Triangular Number

Newton Ni
'''

from math import sqrt
from sys import argv

def count_divisors(n):

    count = 0
    for i in range(1, int(sqrt(n))):
        if (n % i == 0): 
            count += 2

    if (sqrt(n) == int(sqrt(n))):
        count += 1

    return count

if __name__ == "__main__":

    n = 1
    triangle = 1
    while (count_divisors(triangle) < int(argv[1])):
        n += 1
        triangle += n

    print triangle
