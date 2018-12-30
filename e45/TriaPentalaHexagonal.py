def pentagonal(n):
    return int((n * (3 * n - 1) / 2))

def triangular(n):
    return int((n * (n + 1)) / 2)

def hexagonal(n):
    return n * (2 * n - 1)

def isPenta(p):
    j = 1

    while pentagonal(j) < p:
        j += 1

    return p == pentagonal(j)

def isHexa(h):
    j = 1

    while hexagonal(j) < h:
        j += 1

    return h == hexagonal(j)

p = set()
h = set()

limit = 10 ** 4

for i in range(1, limit):
    p.add(pentagonal(i))
    h.add(hexagonal(i))

n = 285
#print(triangular(n) in p, triangular(n) in h)

for i in range(286, limit):
    t = triangular(i)
    if t in h and t in p:
        print(t)
        n = t

print(n)
#print(t, triangular(t))
