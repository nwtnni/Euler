'''
015: Lattice Paths

Newton Ni
'''

from sys import argv

def factorial(n):
    return n*factorial(n - 1) if n > 1 else 1

if __name__ == "__main__":

    n = int(argv[1])
    k = int(argv[2])

    print factorial(n)/(factorial(k) * factorial(n - k))
    

