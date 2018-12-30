import math

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

#def isPerm(n1, n2, n3):
def isPerm(n):
    n2 = n + 3330
    n3 = n2 + 3330
    s1 = str(n)
    s2 = str(n2)
    s3 = str(n3)

    if len(s1) != len(s2) or len(s2) != len(s3):
        return False

    if not isPrime(n) or not isPrime(n2) or not isPrime(n3):
        return False

    digits = [c for c in s1]

    for c in s2:
        if c not in digits:
            return False
    for c in s3:
        if c not in digits:
            return False

    return True

lst = []

for i in range(1000, 10000):
    if isPerm(i):
        lst.append(i)

a = lst[1]
s = str(a)

for i in range(1,3):
    s += str(a + i * 3330)

print(s, len(s))
