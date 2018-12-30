def genDigits(n):
    a = 1
    s = str(a)
    digits = []

    while len(s) < n:
        a += 1
        s += str(a)

    for i in range(7):
        index = 10 ** i
        digits.append(int(s[index - 1]))

    return digits

r = 1
digits = genDigits(1000000)

print(digits)

for d in digits:
    r *= d

print(r)
