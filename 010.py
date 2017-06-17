'''
010: Summation of Primes

Newton Ni
'''

from primes_util import probable_prime

TARGET = 2000000

if __name__ == "__main__":

    sum = 2

    for i in range(3, TARGET, 2):
        if probable_prime(i):
            sum += i

    print sum
