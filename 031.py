'''
031: Coin Sums

Newton Ni
'''

TARGET = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
memo = [[0 for i in range(TARGET + 1)] for j in range(len(COINS))]

if __name__ == "__main__":

    for i in range(len(COINS)):
        memo[i][0] = 1
    for j in range(TARGET + 1):
        memo[0][j] = 1

    for i in range(1, len(COINS)):
        for j in range(TARGET + 1):
            for coin in range(i + 1):
                if j >= COINS[coin]:
                    memo[i][j] += memo[coin][j - COINS[coin]]

    print memo[-1][-1]
