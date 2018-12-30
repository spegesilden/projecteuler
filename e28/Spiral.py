def spiral(n):
    sum = 1
    a = 1

    for i in range(3, n+1):
        if i % 2 == 1:
            for k in range(4):
                a += i-1
                sum += a

    return sum

print(spiral(1001))
