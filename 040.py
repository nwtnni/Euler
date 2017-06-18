'''
040: Champernowne's Constant

Newton Ni
'''

if __name__ == "__main__":

    targets = [0, 9, 99, 999, 9999, 99999, 999999]
    champernowne = ''
    i = 1

    while len(champernowne) < 1000000:
        champernowne += str(i)
        i += 1
    
    product = 1
    for target in targets:
       product *= int(champernowne[target])
    print product
