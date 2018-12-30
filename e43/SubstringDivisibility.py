import math

def isPan(x):
    s = str(x)
    digits = [str(i) for i in range(len(s))]

    for c in s:
        if c in digits:
            digits.remove(c)
        else:
            return False

    return len(digits) == 0

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

primes = [2, 3, 5, 7, 11, 13, 17]

def isSubDivisible(n):
    s = str(n)
    for i in range(1, len(s) - 2):
        chars = ''
        for j in range(3):
            chars += s[i+j]
        a = int(chars)
        #print(chars, a)
        if a % primes[i-1] > 0:
            return False

    return True

pans = []

def genPans(n, lst = []):
    digits = lst[:]

    if n == len(digits):
        s = ''
        for d in digits:
            s += d
        a = int(s)
        if len(str(a)) == n and isSubDivisible(a):
        #if isSubDivisible(a):
            pans.append(a)
        #if len(s) == 8:
        #    pans.append(int(s))
        return

    for i in range(n):
        if str(i) not in digits:
            genPans(n, digits + [str(i)])

#print(isSubDivisible(1406357289))

genPans(10)
print('Generated!')

#print(isSubDivisible(1406357289), len(str(1406357289)), 1406357289 in pans)


s = 0

for p in pans:
    print(p)
    s += p

print(s)
