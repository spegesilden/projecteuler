import math

def isRTriangle(a, b, c):
    return (a * a) + (b * b) == c * c

def combs(p):
    counter = 0
    triangles = []
    limitp = p - 2

    for a in range(1, limitp):
        limita = p - a - 1
        for b in range(1, limita + 1):
            c = p - a - b
            t = sorted([a, b, c])
            if isRTriangle(a, b, c) and t not in triangles:
                #print(a, b, c, t)
                triangles.append(t)
                counter += 1

    return counter

#print(combs(120))

count = 0
pmax = 0

for p in range(3, 1001):
    c = combs(p)
    if count < c:
        print(p, c)
        count = c
        pmax = p

print(pmax, count)
