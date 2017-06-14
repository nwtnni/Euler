import math as m
import random

def decompose(n):

    d = n - 1
    r = 0

    while (d % 2 == 0):
        r += 1
        d = d / 2
    return r, d

def probablePrime(n, k):

    if (n in [2, 3, 5, 7, 11]):
        return True

    r, d = decompose(n)
    
    for i in range(k):

        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if (x == 1 or x == n - 1):
            continue

        for j in range(r - 1):
            x = pow(x, 2, n)

            if (x == 1):
                return False
            elif (x == n - 1):
                break
        else:
            return False

    return True
    
def sum_of_divisors(n):

    divisors = []
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sum(divisors) - n
