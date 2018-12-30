import math

def isPan(x):
    s = str(x)
    digits = [str(i) for i in range(1, len(s) + 1)]

    for c in s:
        if c == '0':
            return False
        elif c in digits:
            digits.remove(c)

    return len(digits) == 0

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

pans = []

def genPans(n, lst = []):
    digits = lst[:]

    if n == len(digits):
        s = ''
        for d in digits:
            s += d
        pans.append(int(s))
        #if len(s) == 8:
        #    pans.append(int(s))
        return

    for i in range(1, n+1):
        if str(i) not in digits:
            genPans(n, digits + [str(i)])

#genPans(8)
#print(pans)

for i in range(1, 9):
    genPans(i)

pmax = 1

print('Generated!')

for p in pans:
    if isPrime(p) and p > pmax:
        pmax = p
        #print(pmax)

print(pmax)


#n = 987654322
#
#while not isPan(n) or not isPrime(n):
#    n -= 1
#
#print(n)
