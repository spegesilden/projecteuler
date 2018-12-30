coins = [1, 2, 5, 10, 50, 100, 200]
t = [0 for i in range(201)]
t[0] = 1

for i in range(201):
    for c in coins:
        if c <= i:
            t[i] += t[i-c]

for i in range(10):
    print(i, t[i])

print(t[200])
