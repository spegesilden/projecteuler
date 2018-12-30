def isAmicable(x):
    a = 0
    adiv = 0
    
    for i in divisors(x):
        a += i

    for i in divisors(a):
        adiv += i

    if adiv == x and a != x:
        return True

    return False

def theOtherNumber(x):
    a = 0

    for i in divisors(x):
        a += i

    return a

def divisors(x):
    div = [i for i in range(1,x) if x % i == 0]

    return div

amicables = set([])

for i in range(1,10000):
    if isAmicable(i):
        amicables.add(i)
        amicables.add(theOtherNumber(i))

result = 0

for i in amicables:
    print(i)
    result += i

print(result)

#a = 28
#
#print(divisors(a), theOtherNumber(a), theOtherNumber(theOtherNumber(a)), isAmicable(a))
