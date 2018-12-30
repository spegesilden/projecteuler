seq = []

for a in range(2, 101):
    for b in range(2, 101):
        n = a ** b

        if not seq.__contains__(n):
            seq.append(n)

print(len(seq))
