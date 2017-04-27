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
    
