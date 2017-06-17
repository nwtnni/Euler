'''
034: Digit Factorials

Newton Ni
'''

factorial = {
    '0':1, '1': 1, '2': 2, '3': 6, '4': 24,
    '5': 120, '6':720, '7': 5040,
    '8': 40320, '9': 362880
    }

def add(a, b): return a + b

if __name__ == "__main__":

    total = 0
    for i in range(2540160):
        digit_factorial = reduce(add, [factorial[d] for d in str(i)])
        if i == digit_factorial: total += i
    print total

