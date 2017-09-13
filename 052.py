'''
052: Permuted Multiples

Newton Ni
'''

def to_chars(n): return [c for c in str(n)] 
def contains(a, b): return set(to_chars(a)) == set(to_chars(b))

if __name__ == "__main__":

    n = 1
    while True:
        multiples = [n * i for i in range(2, 7)]
        multiples = list(map(lambda i: contains(n, i), multiples))
        if multiples.count(True) != 5:
            n = n + 1
            continue
        else:
            print(n)
            break
