def length(n):
    return len(str(n))

def fac(n):
    if n < 2:
        return 1
    #return n * fac(n-1)
    limit = length(n)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

facs = [fac(i) for i in range(10)]

def isDigitFac(a):
    if a < 3:
        return False

    sa = str(a)
    s = 0

    for c in sa:
        s += facs[int(c)]

    if s == a:
        return True

    return False

def digitFac(n):
    sa = str(n)
    s = 0

    for c in sa:
        s += facs[int(c)]

    return s

numbers = []

def genDFac(n, lst = []):
    digits = lst[:]

    if n == len(digits):
        s = sum(map(lambda d: facs[d], digits))

        if digits == sorted(map(int, str(s))):
            print(s, digitFac(s))
            numbers.append(s)
        return

    start = 0
    if len(lst) > 0:
        start = lst[-1]

    for i in range(start, 10):
        genDFac(n, digits + [i])


digitFacs = [[i, fac(i)] for i in range(10)]
s = 0
d = [0, 1]

for i in range(2, 9):
    genDFac(i)

print(sum(numbers))
