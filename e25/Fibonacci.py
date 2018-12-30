def fib(a):
    n = 1
    m = 1

    for i in range(a):
        tmp = m
        m += n
        n = tmp

    return n

def trace(n):
    s = str(n)
    result = 0

    for c in s:
        result += int(c)

    while result > 9:
        result = trace(result)

    return result

n = 1
m = 1
index = 2

while len(str(m)) < 1000:
    tmp = m
    m += n
    n = tmp
    index += 1

#print(index, m)

for i in range(30):
    f = fib(i)
    print(i+1, f, trace(f))
