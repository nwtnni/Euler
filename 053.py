'''
053: Combinatoric Selections

Newton Ni
'''

from math import factorial as f

def c(n, r): return int(f(n) / (f(r) * f(n - r)))

if __name__ == "__main__":
    
    threshold = 1000000
    count = 0

    for n in range(23, 101):
        for r in range(0, n + 1):
            if (c(n, r) > threshold):
                count = count + 1
    print(count)
