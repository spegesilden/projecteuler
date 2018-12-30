def isPan(x):
    digits = []
    s = str(int(x))

    for c in s:
        a = int(c)
        if a == 0:
            return False
        elif a in digits:
            return False
        else:
            digits.append(a)

    return True

l = [str(i) for i in range(1,10)]

def isProduct(p, n, m):
    sp = str(p)
    sn = str(n)
    sm = str(m)

    s = sp + sn + sm
    a = int(s)

    return sorted(s) == l


letters = [i for i in range(2,10)]

pans = []
prods = []

for i in range(1, 10000):
    if isPan(i) and i not in pans:
        pans.append(i)

print("Generated!")

for n in pans:
    for m in pans:
        p = n * m
        if isProduct(p, n, m) and p not in prods:
            prods.append(p)

s = 0

for p in prods:
    s += p

print(s)
