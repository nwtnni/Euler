'''
043: Sub-string Divisibility

Newton Ni
'''

from itertools import permutations

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
DIVISIBILITY = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17}

def substring_divisible(n):
    for start in range(1, 8):
        if int(str(n)[start:start + 3]) % DIVISIBILITY[start] != 0:
            return False
    return True

if __name__ == "__main__":

    total = 0
    for permutation in permutations(DIGITS):
        num = reduce(lambda a, b: str(a) + str(b), permutation)
        total += int(num) if substring_divisible(num) else 0
    print total

    
