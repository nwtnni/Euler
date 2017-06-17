'''
035: Circular Primes

Newton Ni
'''

from primes_util import probable_prime

LIMIT = 1000000

def concat(a, b): return str(a) + str(b)

def rotate(n):
    rotations = [n]
    digits = list(str(n))

    for i in range(1, len(digits)):
        digits.append(digits.pop(0))
        rotations.append(int(reduce(concat, digits))) 
    return rotations

def is_circle(n):
    for rotation in rotate(n):
        if not probable_prime(rotation):
            return False
    return True

if __name__ == "__main__":
    
    circular_primes = 13
    for n in range(99, LIMIT, 2):
        if probable_prime(n) and is_circle(n):
            circular_primes += 1

    print circular_primes
