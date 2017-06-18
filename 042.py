'''
042: Coded Triangle Numbers

Newton Ni
'''

from letters_util import score_word

def format(word): return word.replace('"', '')

if __name__ == "__main__":

    triangles = [(n * (n + 1)) / 2 for n in range(100)]
    total = 0

    with open('042.txt', 'r') as f:
        words = map(format, f.readline().split(','))

    for word in words:
        score = score_word(word)
        total += 1 if score in triangles else 0
    print total
