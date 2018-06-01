import random

PRIMES = [
    2, 3, 5, 7, 11, 13,
    17, 19, 23, 29, 31,
    37, 41, 43, 47, 53,
    59, 61, 67, 71, 73,
    79, 83, 89, 97
    ]


def decompose(n):

    d = n - 1
    r = 0

    while (d % 2 == 0):
        r += 1
        d = d // 2
    return r, d


def probable_prime(n, k=5):

    if n < 12:
        return True if n in PRIMES else False

    r, d = decompose(n)

    for i in range(k):

        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        print(x)

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


def generate_primes(n):

    if n <= 25:
        return PRIMES[:n]

    prime_list = list(PRIMES)
    i = 99

    while len(prime_list) < n:
        if probable_prime(i, 5):
            prime_list.append(i)
        i += 2

    return prime_list
