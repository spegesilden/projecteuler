import math

def divisors(x):
    div = [i for i in range(1,x) if x % i == 0]
    return div

def theSum(x):
    s = 0
    for i in divisors(x):
        s += i
    return s

def isPerfect(x):
    if theSum(x) == x:
        return True
    return False

def isDeficient(x):
    if theSum(x) < x:
        return True
    return False

def isAbundant(x):
    s = 0

    for i in range(1,x):
        if x % i == 0:
            s += i

    if x < s:
        return True
    return False

def canBeWritten(x):
    if x < 24:
        return False

    a = math.floor(x/2)+1

    for i in range(12,a+1):
        if isAbundant(i) and isAbundant(x-i):
            return True

    return False

result = 0
abundants = []
sumOfAbundants = set([])

for x in range(1,28123):
    if isAbundant(x):
        #print(x)
        abundants.append(x)

for x in abundants:
    for y in abundants:
        s = x + y
        sumOfAbundants.add(s)

for x in range(1,28124):
    if not sumOfAbundants.__contains__(x):
        result += x

print(result)

#a = 12
#
#print(isAbundant(a))
