'''
018: Maximum Path Sum I

Newton Ni
'''

if __name__ == "__main__":

    grid = []
    with open('018.txt', 'r') as f:

        for line in f:
            grid.append([])

            for num in line.split(' '):
                grid[-1].append(int(num))

    
    while len(grid) > 1:
        
        for i in range(len(grid[-1]) - 1):
            left = grid[-1][i]
            right = grid[-1][i + 1]
            grid[-2][i] += max(left, right)

        grid.pop()

    print grid[0][0]


