'''
014: Longest Collatz Sequence

Newton Ni
'''

from sys import argv

if __name__ == "__main__":

    memo = {}
    record = 0
    record_n = 0
    n = 1

    while n < int(argv[1]):

        i = n
        seq = 0

        while i != 1:
            if i in memo:
                seq += memo[i]                
                break
            if i % 2 == 0:
                i /= 2
            else:
                i = i*3 + 1
            seq += 1

        memo[n] = seq
        record = seq if seq > record else record
        record_n = n if seq == record else record_n
        n += 1

    print record, record_n
