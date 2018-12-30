def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

def combs(n, r):
    p = fac(n)
    q = fac(r) * fac(n - r)

    return p // q

count = 0

for n in range(1, 101):
    for r in range(n+1):
        c = combs(n, r)
        if c > 10 ** 6:
            count += 1

print(count)
