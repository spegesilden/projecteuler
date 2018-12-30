import math

def tLeft(n):
    s = str(n)
    truncated = []

    for i in range(len(s)):
        tmp = ''
        for j in range(i+1):
            tmp += s[j]
        truncated.append(int(tmp))

    return truncated

def tRight(n):
    s = str(n)[::-1]
    truncated = []

    for i in range(len(s)):
        tmp = ''
        for j in range(i+1):
            tmp += s[j]
        r = tmp[::-1]
        truncated.append(int(r))

    return truncated

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

def isTPrime(x):
    if isPrime(x):
        for n in tLeft(x):
            if not isPrime(n):
                return False

        for n in tRight(x):
            if not isPrime(n):
                return False
        return True
    return False

s = '3797'

print(tLeft(3797))
tprimes = []
i = 10

while len(tprimes) < 11:
    if isTPrime(i):
        print(i)
        tprimes.append(i)
    i += 1

s = 0

for p in tprimes:
    s += p

print(s)


#isPrime = [True] * (10 ** 6)
#isPrime[0] = False
#isPrime[1] = False
#
#for i in range(3, 10 ** 6, 2):
#    if not isPrime[i]:
#        continue
#    for j in range(i ** 2, 10 ** 6, 2 * i):
#        isPrime[j] = False

