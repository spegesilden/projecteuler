import math

isPrime = [True] * ((10 ** 6) + 1)
isPrime[0] = False
isPrime[1] = False

for i in range(3, 10 ** 6, 2):
    if not isPrime[i]:
        continue
    for j in range(i ** 2, 10 ** 6, 2 * i):
        isPrime[j] = False

primelist = []

for i in range(2, 10 ** 6 + 1):
    if i % 2 == 1 or i == 2:
        if isPrime[i]:
            primelist.append(i)

primeset = set(primelist)

#print(953 in primeset)

print('Generated!')

best = [-1, -1]
i = 0 

while i < len(primelist):
    p = primelist[i]
    j = 1
    while p <= 10 ** 6 and i + j < len(primelist):
        p += primelist[i+j]
        j += 1
        if p in primeset and j > best[0]:
            best = [j, p]
            print(best)
    i += 1

print(best)

def consPrimes(n):
    if n < 3:
        return []

    i = 0

    while primelist[i] <= n and i <= len(primelist):
        cons = []
        p = primelist[i]
        s = 0
        j = i

        while s < n and j < len(primelist):
            cons.append(p)
            s += p
            j += 1
            p = primelist[j]

        if s == n:
            return cons
        i += 1

    return []


def isConsPrimeSum(n):
    s = sum(consPrimes(n))
    return s == n

#print(isConsPrimeSum(41), consPrimes(41), len(consPrimes(41)))
#print(isConsPrimeSum(953), consPrimes(953), len(consPrimes(953)))


#l = 317
#p = 310019
#
#for i in primelist:
#    if i == 310019:
#        print('Up to speed')
#    if i > 310019:
#        cons = consPrimes(i)
#        if len(cons) > l:
#            l = len(cons)
#            p = i
#            print(p, l)
#
#print(p)
