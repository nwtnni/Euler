'''
020: Factorial Digit Sum

Newton Ni
'''

from math import factorial

if __name__ == "__main__":

    print sum(int(i) for i in str(factorial(100)))
