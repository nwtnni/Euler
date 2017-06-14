'''
023: Non-abundant Sums

Newton Ni
'''

from math import sqrt

def sum_of_proper_divisors(n):
    divisors = []
    root = sqrt(n)
    for i in range(1, int(root) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)

    if root == int(root):
        divisors.remove(root)

    return sum(divisors) - n

def is_abundant(n):
    return sum_of_proper_divisors(n) > n

if __name__ == "__main__":

    MIN = 12
    MAX = 28124
    abundant = filter(lambda n: sum_of_proper_divisors(n) > n, range(MIN, MAX))
    not_abundant_sum = set(range(MAX))

    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            not_abundant_sum.discard(abundant[i] + abundant[j])

    print sum(not_abundant_sum)

    
