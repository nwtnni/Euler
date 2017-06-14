'''
022: Names Scores

Newton Ni
'''

letter_score = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4,
        'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16,
        'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26
        }

if __name__ == "__main__":

    with open('022.txt', 'r') as f:
        names = f.readline().replace('"','').split(",")
        names.sort()
        
    score = 0
    for i in range(len(names)):
        score += sum(letter_score[letter] for letter in names[i]) * (i + 1)

    print score



