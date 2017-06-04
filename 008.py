'''
008: Largest Product in a Series

Newton Ni
'''

from sys import argv

digits, max = [], 0
with open(argv[1], "r") as f:
    for line in f:
        for digit in line:

            if digit.isdigit():
                digit = int(digit)
            else:
                break

            if (len(digits) == int(argv[2])):

                digits.pop(0)
                digits.append(digit)
                x = 1
                for i in range(len(digits)):
                    x *= digits[i]
                if (x > max):
                    max = x
            else:
                digits.append(digit)

print max
