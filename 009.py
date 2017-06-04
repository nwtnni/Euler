'''
009: Special Pythagorean Triplet

Newton Ni
'''

from math import pow, sqrt
from sys import exit

TARGET = 1000

if __name__ == '__main__':

    for a in range(1, TARGET):
        for b in range(1, TARGET):

            c = sqrt(float(pow(a, 2) + pow(b, 2)))

            if (a + b + c) == TARGET:
                print a*b*c
                exit()
