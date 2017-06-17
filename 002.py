'''
002: Even Fibonacci Numbers

Newton Ni
'''

LIMIT = 4000000

if __name__ == "__main__":

    a, b, c = 1, 2, 0
    sum = 2

    while (a + b < 4000000):
        c = a + b
        if (c % 2 == 0):
            sum += c
        a, b = b, c

    print sum


