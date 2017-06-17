'''
036: Double-base Palindromes

Newton Ni
'''

LIMIT = 1000000

def to_binary(n):
    b = ''
    while n > 0:
        b = '1' + b if n % 2 == 1 else '0' + b
        n /= 2
    return b

def is_palindrome(n): return n == n[::-1]

if __name__ == "__main__":

    total = 0
    for i in range(LIMIT):
        if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
            total += i
    print total
