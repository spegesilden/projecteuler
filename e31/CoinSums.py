coins = [1, 2, 5, 10, 20, 50, 100, 200]
t = [[0 for i in range(len(coins))] for i in range(201)]
t[0][0] = 1

for i in range(0, 201):
    for n, c1 in enumerate(coins):
        for m, c2 in enumerate(coins):
            if c1 >= c2 and c1 <= i:
                t[i][n] += t[i-c1][m]

for i in range(201):
    print(i, t[i])

print(sum(t[200][i] for i in range(len(coins))))
