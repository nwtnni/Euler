'''
047: Distinct Primes Factors

Newton Ni
'''

from math import sqrt

def distinct_factors(n):
    
    factors = set([n])

    while True:
        next_round = set()
        for factor in factors:
            for i in range(2, int(sqrt(factor)) + 1):
                if factor % i == 0:
                    next_round.add(factor / i) 
                    next_round.add(i)

        if len(next_round) == 0: 
            break
        else:
            factors = next_round
    return len(factors)

if __name__ == "__main__":
    
    consecutive = 4
    n = 0
    while True:
        n += 1
        for i in range(n, n + consecutive):
            if distinct_factors(i) != consecutive: break
        else:
            print n
            break

