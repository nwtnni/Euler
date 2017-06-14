'''
025: 1000 Digit Fibonacci Number

Newton Ni
'''

if __name__ == "__main__":

    fib = [1, 1]
    index = 2

    while len(str(fib[-1])) < 1000:
        index += 1
        fib.append(fib[index - 2] + fib[index - 3])

    print index
