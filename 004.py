'''
004: Largest Palindrome Product

Newton Ni
'''

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        val = str(i * j)
        if (max < i * j and val == val[::-1]):
            max = i * j
print max
