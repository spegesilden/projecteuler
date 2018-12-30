def toBinary(x):
    if x == 0:
        return 0

    s = ''
    n  = x

    while n >= 1:
        if n % 2 == 0:
            s += '0'
            n = n / 2
        else:
            s += '1'
            n = (n - 1) / 2
    
    s = s[::-1]

    return int(s)

def isPal(x):
    s10 = str(x)
    s2 = str(toBinary(x))

    return s10 == s10[::-1] and s2 == s2[::-1]

s = 0

#print(isPal(1))

for i in range(10 ** 6):
    if isPal(i):
        print(i)
        s += i

print(s)
