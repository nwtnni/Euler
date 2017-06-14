'''
024: Lexicographic Permutations

Newton Ni
'''

from itertools import permutations

if __name__ == "__main__":
    
    count = 0
    for n in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
       count += 1
       if count == 1000000:
           print n
           break

