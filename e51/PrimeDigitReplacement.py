import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def generateNumbers(n):
    condition = True

    for digit in n:
        if digit > -1:
            condition = False

    if condition:
        return [n]

    numbers = []

    for i in range(len(n)):
        if n[i] > -1:
            nMod = n[:]
            nMod[i] = -1
            if nMod not in numbers:
                numbers.append(nMod)

    for a in numbers:
        for b in generateNumbers(a):
            if b not in numbers:
                numbers.append(b)

    numbers.append(n)

    return numbers

def replace(lst):
    places = [False for i in range(len(lst))]

    for i, d in enumerate(lst):
        if d == -1:
            places[i] = True

    minimum = []

    for n in range(10):
        s = ''
        for i, b in enumerate(places):
            if b == True:
                s += str(n)
            else:
                s += str(lst[i])
        a = int(s)
        condition = n == 0 and lst[0] == -1
        if isPrime(a) and not condition:
            minimum.append(a)

    return minimum

def digitReplacements(n):
    replacements = [n]
    nlst = [int(d) for d in str(n)]
    m = [0, None]

    for lst in generateNumbers(nlst):
        for a in replace(lst):
            l = len(str(a))
            if m[0] < l:
                if a not in replacements:
                    m[0] = l
                    m[1] = min(a)
                    for i in a:
                        if i not in replacements:
                            replacements.append(i)

    return replacements

k = 23
m = [5, 6, -1, -1, 3]
#m = [-1, 3]

print(digitReplacements(k))

#print(replace(m))
