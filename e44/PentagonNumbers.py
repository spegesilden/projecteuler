def pentagonal(n):
    return int((n * (3 * n - 1) / 2))

def isSumPenta(n, m):
    p = pentagonal(n) + pentagonal(m)

    j = 1

    while pentagonal(j) < p:
        j += 1

    return p == pentagonal(j)

def isDiffPenta(n, m):
    p = pentagonal(n) - pentagonal(m)

    j = 1

    while pentagonal(j) < p:
        j += 1

    return p == pentagonal(j)

# pn = 7042750
# pm = 156900
n = 1
m = 1

while pentagonal(n) < 7042750:
    n += 1
while pentagonal(m) < 1560090:
    m += 1


print(isSumPenta(n, m), isDiffPenta(n,m), pentagonal(n) - pentagonal(m))
