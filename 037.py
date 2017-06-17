'''
037: Truncatable Primes

Newton Ni
'''

from primes_util import probable_prime

LEFT_DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
RIGHT_DIGITS = [1, 3, 7, 9]

def add(a, b): return a + b

def left_append(arr): return [int(str(b) + str(a)) for b in LEFT_DIGITS for a in arr]
def right_append(arr): return [int(str(a) + str(b)) for b in RIGHT_DIGITS for a in arr]

if __name__ == "__main__":
        
    left = [2, 3, 5, 7]
    right = [2, 3, 5, 7]
    total = []

    while True:
        left = filter(probable_prime, left_append(left))
        right = filter(probable_prime, right_append(right))
        total.extend((set(left).intersection(set(right))))
        if len(total) == 11: break
    print reduce(add, total)
