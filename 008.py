'''
008: Largest Product in a Series

Newton Ni
'''

LIMIT = 13

def times(a, b): return a*b

if __name__ == "__main__":
    
    digits = []
    max = 0
    with open('008.txt', "r") as f:
        for line in f:
            for digit in line.strip():

                digit = int(digit)

                if (len(digits) != LIMIT):
                    digits.append(digit)
                else:
                    digits.pop(0)
                    digits.append(digit)
                    product = reduce(times, digits)
                    max = product if product > max else max
    print max
