'''
026: Reciprocal Cycles

Newton Ni
'''

def multiplicative_order(n):

    order = 1
    while pow(10, order, n) != 1:
        order += 1
    return order


if __name__ == "__main__":

    max = 0
    max_i = 0
    for i in range(3, 1000):
        if i % 2 == 0 or i % 5 == 0:
            continue

        order = multiplicative_order(i)
        max_i = i if order > max else max_i
        max = order if order > max else max

    print max, max_i

