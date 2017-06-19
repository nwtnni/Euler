'''
121: Disc Game Prize Fund

Newton Ni
'''

def add(a, b): return a + b
def left(turn, prev): return ((turn - 1.0) / turn) * prev 
def right(turn, prev): return (1.0 / turn) * prev 

if __name__ == "__main__":
    
    turns = 15
    cur = [1]

    for d in range(2, turns + 2):

        nxt = [left(d, cur[0])]
        for i in range(0, len(cur) - 1):
            nxt.append(right(d, cur[i]) + left(d, cur[i + 1]))
        nxt.append(right(d, cur[-1]))

        cur = nxt
    
    print 1.0 / reduce(add, cur[1 + turns/2:])
