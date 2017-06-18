'''
038: Pandigital Multiples

Newton Ni
'''

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def concat(a, b): return int(str(a) + str(b))

def is_pandigital(n):
    n = str(n)
    for digit in DIGITS:
        if n.count(digit) != 1: return False
    return n.count('0') == 0


if __name__ == "__main__":
    
    max = 0
    for n in range(2, 10):
        for i in range(1, 10**(10/n)):
            product = reduce(concat, [i * j for j in range(1, n + 1)])
            max = product if is_pandigital(product) and max < product else max
    print max

          
        
