'''
022: Names Scores

Newton Ni
'''

from letters_util import score_word

if __name__ == "__main__":

    with open('022.txt', 'r') as f:
        names = f.readline().replace('"','').split(",")
        names.sort()
        
    score = 0
    for i in range(len(names)):
        score += score_word(names[i]) * (i + 1)

    print score



