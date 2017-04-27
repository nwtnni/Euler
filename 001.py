import sys

'''
001: Multiples of 3 and 5
'''

sum = 0;
for i in range(int(sys.argv[1])):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print sum
