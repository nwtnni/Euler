'''
021: Amicable Numbers

Newton Ni
'''

from util import sum_of_divisors

if __name__ == "__main__":

    amicable = []
    for i in range(2, 10000):
        j = sum_of_divisors(i)
        if sum_of_divisors(j) == i and j < 10000 and i != j:
            amicable.extend([i, j])

    print sum(amicable) / 2

