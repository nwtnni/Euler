'''
017: Number Letter Counts

Newton Ni
'''

one = {
    1: 'one', 2: 'two', 3: 'three', 
    4: 'four', 5: 'five', 6: 'six', 
    7: 'seven', 8: 'eight', 9: 'nine'
    }    

ten = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 
    50: 'fifty', 60: 'sixty', 70: 'seventy', 
    80: 'eighty', 90: 'ninety'
    }

weird = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen'
    }

def ones(n):
    n %= 10
    return len(one[n]) if n != 0 else 0

def tens(n):
    n %= 100

    if n < 10:
        return 0
    elif n == 10:
        return len(weird[n])
    elif n < 20:
        remainder = n % 10
        return len(weird[n]) - len(one[remainder])
    else:
        n -= n % 10
        return len(ten[n])

def hundreds(n):
    remainder = n % 100
    n %= 1000
    n /= 100

    if n > 0:
        return len(one[n]) + 10 if remainder != 0 else len(one[n]) + 7
    else:
        return 0

def thousands(n):
    n /= 1000
    return len(one[n]) + 8 if n > 0 else 0

if __name__ == "__main__":

    sum = 0
    for n in range(1, 1001):
        sum += thousands(n) + hundreds(n) + tens(n) + ones(n)

    print sum
