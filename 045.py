'''
045: Triangular, Pentagonal, and Hexagonal

Newton Ni
'''

from math import sqrt

def triagonal(n): return (n * (n + 1)) / 2
def is_pentagonal(n): return (sqrt(24 * n + 1) + 1) % 6 == 0

if __name__ == "__main__":

    n = 1
    while True:
        if is_pentagonal(triagonal(n)) and n > 285:
            print triagonal(n)
            break
        n += 2 
