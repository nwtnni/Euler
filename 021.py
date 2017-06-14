'''
021: Amicable Numbers

Newton Ni
'''

from math import sqrt

def sum_of_divisors(n):

    divisors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sum(divisors) - n

if __name__ == "__main__":

    amicable = []
    for i in range(2, 10000):
        j = sum_of_divisors(i)
        if sum_of_divisors(j) == i and j < 10000 and i != j:
            amicable.extend([i, j])

    print sum(amicable) / 2

