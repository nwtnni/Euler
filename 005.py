'''
005: Smallest Multiple

Newton Ni
'''

from primes_util import probable_prime

LIMIT = 20

if __name__ == "__main__":
    
    # Increment by the LCM of primes
    n = 0
    while (True):
        n += 9699690
        for i in range(LIMIT, 1, -1):
            if (n % i != 0): break
        else:
            print n
            break
