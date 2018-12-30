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

def pMult(x):
    n = x
    s = str(n)
    counter = 1

    while len(s) < 9:
        counter += 1
        s += str(n*counter)

    return int(s)

def isPMult(x):
    return isPan(pMult(x))

l = 0
m = 0

for i in range(1,10 ** 5):
    n = pMult(i)
    if isPan(n):
        m = i
        l = max(n, l)
        print(i, n, l)

print(m, l)
print(pMult(192), isPan(192))
