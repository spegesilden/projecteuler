def string2Value(s):
    result = 0
    for x in s:
        result += char2Value(x)
    return result

def char2Value(c):
    return ord(c) - 64

with open('names.txt', 'r') as f:
    s = f.readline().replace("\"","")
    names = s.split(',')

names.sort()
result = 0

for i, x in enumerate(names):
    result += (i + 1) * string2Value(x)

print(result)
