import math

def isPrime(x):
    if x < 3:
        return x == 2

    n = int(math.sqrt(x) + 1)

    for i in range(2, n+1):
        if x % i == 0:
            return False

    return True

def primeFactors(x):
    if x == 1:
        return []

    divisors = set()

    d = 2
    n = x

    while n > 1:
        if n % d == 0:
            divisors.add(d)
            n //= d
        else:
            d += 1

    return divisors

def conssecutive(n, i):
    if i == 4:
        return i
    elif len(primeFactors(n)) == 4:
        return conssecutive(n+1, i+1)
    else:
        return i

condition = True
n = 2

while condition:
    i = conssecutive(n, 0)

    if i == 2:
        print(n, i, primeFactors(n))

    if i == 4:
        print(n, i)
        condition = False
    else:
        #print(n, i)
        n += i + 1

print(n)
