'''
011: Largest Product in a Grid

Newton Ni
'''

DIM = 20
ADJ = 4
    
def horizontal(grid):

    record = 0

    for i in range(DIM):
        for j in range(DIM - ADJ):

            prod = 1
        
            for k in range(ADJ):
               prod *= grid[i][j + k]

            record = prod if prod > record else record

    return record

def vertical(grid):

    record = 0

    for i in range(DIM - ADJ):
        for j in range(DIM):

            prod = 1

            for k in range(ADJ):
                prod *= grid[i + k][j]

            record = prod if prod > record else record
    return record

def diagonalLeft(grid):

    record = 0

    for i in range(ADJ, DIM):
        for j in range(ADJ, DIM):

            prod = 1

            for k in range(ADJ):
                prod *= grid[i - k][j - k]

            record = prod if prod > record else record

    return record

def diagonalRight(grid):

    record = 0

    for i in range(DIM - ADJ):
        for j in range(DIM - ADJ):

            prod = 1

            for k in range(ADJ):
                prod *= grid[i + k][j + k]

            record = prod if prod > record else record

    return record

if __name__ == "__main__":

    grid = []

    with open("011.txt", "r") as f:

        tiles = f.readline().split(" ")
        counter = 0

        for i in range(DIM):
            grid.append([])

            for j in range(DIM):
                grid[i].append(int(tiles[counter]))
                counter += 1

    print grid

    print horizontal(grid)
    print vertical(grid)
    print diagonalLeft(grid)
    print diagonalRight(grid)

    print max(horizontal(grid), vertical(grid), diagonalLeft(grid), diagonalRight(grid))
