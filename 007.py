'''
007: 10001st Prime

Newton Ni
'''

from primes_util import probable_prime

LIMIT = 10001

if __name__ == "__main__":
        
    n = 2
    i = 3

    while (n < LIMIT):
        i += 2
        n += 1 if probable_prime(i) else 0

    print i
