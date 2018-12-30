def isSum(n):
    s = str(n)
    sum = 0

    for i in s:
        sum += int(i) ** 5

    return sum == n

sum = 0

for i in range(2, 1000000000):
    if isSum(i):
        print(i)
        sum += i

print(sum)
