'''
055: Lychrel Numbers

Newton Ni
'''

def reverse(n): return int((str(n))[::-1])
def is_palindrome(n): return n == reverse(n)
def next(n): return n + reverse(n)

if __name__ == "__main__":
   
    count = 0
    for n in range(10000):
        for i in range(49):
            n = next(n)
            if is_palindrome(n):
                break    
        else:
            count = count + 1 
    print(count)
