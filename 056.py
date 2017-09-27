'''
056: Powerful Digit Sum

Newton Ni
'''

LIMIT = 100

if __name__ == "__main__":

    n = 0

    for a in range(1, LIMIT):
        for b in range(1, LIMIT):
            s = sum([int(n) for n in str(pow(a, b))])
            n = s if s > n else n
    print(n)
