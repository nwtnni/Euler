'''
001: Multiples of 3 and 5

Newton Ni
'''

LIMIT = 1000

if __name__ == "__main__":
    
    sum = 0;
    for i in range(LIMIT):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    print sum
