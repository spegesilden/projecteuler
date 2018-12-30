def index(x,n):
    mult = 10 ** n
    a = x * mult
    s = str(a)
    return s[n]

def length(x):
    a = format(float(100/x), '.200f')
    s = str(a)
    i = 2
    j = 3

    s1 = s[2]
    s2 = s[3]

    while s1 != s2:
        i = i + 1
        j = j + 2
        s1 = s[i]
        s2 = s[j]

    if s2 == '0':
        return 0

    for k in range(1,j+1):
        if s[j-k] == s[j]:
            i = j - k
            break

    return j - i

def decimal(x, y, r):
    result = [x, y, r, 0]
    xnew = x + 10*r

    if xnew < y:
        result[0] = 10 * x
        result[2] = 0
    else:
        a = x % y
        result[0] = a*10
        result[2] = a
        result[3] = int( (x - a) / y )

    return result

def period(x):
    a = decimal(1, x, 0)
    a = decimal(a[0], a[1], a[2])

    i = 1
    j = 2

    if x > 100:
        a = decimal(a[0], a[1], a[2])
        i = 2
        j = 3

    b = decimal(a[0], a[1], a[2])

    while a[0] != b[0]:
        if a[0] == 0:
            break
        i = i + 1
        j = j + 2

        a = decimal(a[0], a[1], a[2])

        b = decimal(b[0], b[1], b[2])
        b = decimal(b[0], b[1], b[2])

    if a[0] == 0:
        return 0

    a = decimal(1, x, 0)
    #s1 = a[2]
    dec = [0]

    for k in range(0,j):
        a = decimal(a[0], a[1], a[2])
        dec.append(a[0])

    for k in range(1, j+1):
        if dec[j-k] == b[0] and dec[j-k] > 0:
            #print(dec[j-k], s2)
            i = j - k
            break

    return j - i


d = 2
p = 0

#a = decimal(1, 999, 0)
#a = decimal(a[0], a[1], a[2])

#for i in range(2,10):
#    #a = decimal(a[0], a[1], a[2])
#    #print(a)
#    print(i, period(i))

for i in range(2, 1000):
    #print(i, period(i))
    ip = period(i)
    if  ip > p:
        p = ip
        d = i
    #    print(i, period(i))

print(d)
