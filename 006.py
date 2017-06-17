'''
006: Sum Square Difference

Newton Ni
'''

LIMIT = 100

def add(a, b): return a + b

if __name__ == "__main__":
    
    squaresum = reduce(add, [n for n in range(1, LIMIT + 1)])**2
    sumsquare = reduce(add, [n**2 for n in range(1, LIMIT + 1)])
    print squaresum - sumsquare
