from pprint import pprint

coins = [1, 2, 5, 10, 20, 50, 100, 200]
#t = {c: [0] * 201 for c in coins}
t = [[0 for i in range(201)] for i in range(len(coins)+1)]
t[0][0] = 1


for i in range(201):
    for j in range(1, len(coins)+1):
        c = coins[j-1]
        if c <= i:
            t[j][i] = t[j][i-c] + t[j-1][i]
        else:
            t[j][i] = t[j-1][i]


pprint(list(zip(*t)))
