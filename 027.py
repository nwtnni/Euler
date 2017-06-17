'''
027: Quadratic Primes

Newton Ni
'''

from primes_util import probable_prime

if __name__ == "__main__":
    
    max_primes = 0
    max_a = 0
    max_b = 0

    for a in range(-999, 1000):
        for b in range(1, 1000):

            i = 0

            def quadratic(n):
                return n*n + a*n + b 

            while probable_prime(quadratic(i)):
                i += 1
            
            if i + 1 > max_primes:
                max_primes = i + 1
                max_a = a
                max_b = b

    print max_a, max_b, max_primes, max_a * max_b



     
