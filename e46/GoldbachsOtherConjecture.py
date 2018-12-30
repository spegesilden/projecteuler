import math

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

def isGold(n):
    if isPrime(n):
        return False

    for p in range(2, n):
        if isPrime(p):
            a1 = (n - p) // 2
            a2 = int(math.sqrt(a1))
            if a1 == a2 * a2:
                return True

    return False

n = 4

while isPrime(n) or isGold(n):
    n += 1

print(n)
