'''
028: Number Spiral Diagonals

Newton Ni
'''

if __name__ == "__main__":

    n = 1001**2
    i = 1
    r = 2
    diagonal_sum = 1

    while i < n:
        for corner in range(4):
            i += r
            diagonal_sum += i
        r += 2

    print diagonal_sum



        


        
        


