def checkChars(x1, x2):
    digits1 = [c for c in str(x1)]
    digits2 = [c for c in str(x2)]

    for c in digits1:
        if c in digits2:
            digits2.remove(c)
        else:
            return False

    return len(digits2) == 0


def isPerm(x, n):
    for i in range(2, n+1):
        if not checkChars(x, i*x):
            return False

    return True

x = 1

while not isPerm(x, 6):
    x += 1

print(x)
