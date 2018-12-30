def rotate(x):
    s = str(x)
    l = len(s)
    rotations = []

    for i in range(l):
        rotation =  ''
        for j in range(l):
            index = (i + j) % l
            rotation += s[index]
        rotations.append(int(rotation))

    return rotations


isPrime = [True] * (10 ** 6)
isPrime[0] = False
isPrime[1] = False

for i in range(3, 10 ** 6, 2):
    if not isPrime[i]:
        continue
    for j in range(i ** 2, 10 ** 6, 2 * i):
        isPrime[j] = False

counter = 1

for i in range(3, 10 ** 6, 2):
    for r in rotate(i):
        if not isPrime[r] or r % 2 == 0:
            break
    else:
        counter += 1

print(counter)
