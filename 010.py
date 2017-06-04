'''
010: Summation of Primes

Newton Ni
'''

from util import probablePrime

TARGET = 2000000

if __name__ == "__main__":

    sum = 2

    for i in range(3, TARGET, 2):
        if probablePrime(i, 5):
            sum += i

    print sum
