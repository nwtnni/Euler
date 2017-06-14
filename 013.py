'''
013: Large Sum

Newton Ni
'''

if __name__ == "__main__":

    with open('013.txt', 'r') as f:
        sum = 0
        for line in f:
            sum += int(line[0:11])
        print sum
