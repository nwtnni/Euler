'''
049: Prime Permutations

Newton Ni
'''

from collections import Counter
from primes_util import probable_prime

def is_permutation(arr):
    counter = Counter(str(arr[0]))
    for digit in counter:
        if str(arr[1]).count(digit) != counter[digit]: return False
        if str(arr[2]).count(digit) != counter[digit]: return False
    return True

if __name__ == "__main__":
    
    for n in range(1001, 9995, 2):
        if not probable_prime(n):
            continue

        for diff in range(2, (10000 - n) / 2, 2):
            seq = [n + i * diff for i in range(3)]
            if is_permutation(seq) and probable_prime(seq[1]) and probable_prime(seq[2]):
                print reduce(lambda a, b: str(a) + str(b), seq)
