def divisors(a):
    diva = []

    for i in range(2, a+1):
        if a % i == 0:
            diva.append(i)

    return diva

def commonDiv(p1, q1, p2, q2):
    divs = []
    m = max(p1, q1, p2, q2)

    for i in range(2, m):
        if p1 % i == 0 and q1 % i == 0 and q1 % i == 0 and q2 % i == 0:
            divs.append(i)

    return divs

def red(p1, q1):
    divpq1 = []
    m = max(p1, q1)

    for i in range(2, m):
        if p1 % i == 0 and q1 % i == 0:
            divpq1.append(i)

    p1n = p1
    q1n = q1

    for i in range(len(divpq1)):
        d = divpq1[len(divpq1)-1-i]
        if p1n % d == 0 and q1n % d == 0:
            p1n = int(p1n / d)
            q1n = int(q1n / d)

    return [p1n, q1n]

def isCan(p, q):
    if p % 10 == 0 and q % 10 == 0:
        return False

    digitsp = [c for c in str(p)]
    digitsq = [c for c in str(q)]

    n = 0
    m = 0
    contains = False

    #if digitsp[1] == digitsq[0]:
    #    contains = True
    for i in range(len(digitsp)):
        for j in range(len(digitsq)):
            if digitsp[i] == digitsq[j]:
                contains = True
                n = i
                m = j

    if contains:
        n = (n + 1) % 2
        m = (m + 1) % 2

        pair = [int(digitsp[n]), int(digitsq[m])]
        red1 = red(p, q)

        pnew = pair[0]
        qnew = pair[1]

        red2 = red(pnew, qnew)

        if red1[0] == red2[0] and red1[1] == red2[1]:
            return True

    return False

#print(isCan(49, 98), isCan(30, 50), isCan(12, 24))

denominators = []
reduced = []

for q in range(11, 100):
    for p in range(10, q):
        if isCan(p, q):
            denominators.append([p, q])
            #denominators.append(red(p, q))

q = 1
p = 1

for i in range(len(denominators)):
    r = red(denominators[i][0], denominators[i][1])
    #r = denominators[i]
    if r not in reduced:
        p *= r[0]
        q *= r[1]
        reduced.append(r)
        print(denominators[i], r)

print(p, q)
print(red(p, q)[1])
