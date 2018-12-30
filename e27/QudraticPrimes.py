import math

def isPrime(n):
    if n < 2:
        return False

    m = int(math.sqrt( n )) + 1

    for i in range(2, m):
        if n % i == 0:
            return False

    return True

def pol(n, a, b):
    result = n*n + n*a + b
    return result

def consPrimes(a, b):
    if not isPrime(b):
        return 0
    
    n = 1

    while isPrime(pol(n, a, b)):
        #print(pol(n,a,b), isPrime(pol(n, a, b)))
        n += 1

    return n - 1

c = 0
a = 0
b = 0

for i in range(-999, 1000):
    for j in range(-999, 1000):
        cons = consPrimes(i, j)
        if c < cons:
            c = cons
            a = i
            b = j

result = a * b

print(result)

#print(isPrime(41), consPrimes(1, 41))
