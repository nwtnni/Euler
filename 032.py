'''
032: Pandigital Products

Newton Ni
'''

from itertools import permutations

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":

    products = []
    for permutation in permutations(DIGITS):

        n = reduce(lambda s, n: str(s) + str(n), list(permutation))
        
        product = int(n[5:])

        if int(n[:2]) * int(n[2:5]) == product or int(n[0]) * int(n[1:5]) == product:
            if product not in products:
                products.append(product)

    print sum(products)
