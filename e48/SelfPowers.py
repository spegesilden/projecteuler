import math

a = 0

for i in range(1, 1000):
    a += (i ** i) % 10 ** 10

a %= 10 ** 10

print(a, len(str(a)))
