'''
050: Consecutive Prime Sum

Newton Ni
'''

from primes_util import generate_primes
from primes_util import probable_prime

if __name__ == "__main__":

    primes = generate_primes(100000)
    max_consecutive = 0
    max_total = 0

    for i in range(len(primes)):
        
        consecutive = 1
        total = primes[i]

        while total < 1000000:

            if probable_prime(total) and consecutive > max_consecutive:
                max_consecutive = consecutive
                max_total = total

            total += primes[i + consecutive]
            consecutive += 1

    print max_total



