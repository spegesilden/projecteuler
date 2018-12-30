import csv
import sys

array = [[None for i in range(0,100)] for k in range(0,100)]
maxSums = [[None for i in range(0,100)] for k in range(0,100)]
maxPath = [0 for i in range(100)]

# Reads the csv-file
f = open('triangle.txt', 'rt')
try:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        j = 0
        for a in row:
            array[i][j] = int(a)
            j += 1
        i += 1
finally:
    f.close()

n = len(array)

for i in range(0,n):
    for j in range(0,i+1):
        if i == 0:
            maxSums[i][j] = array[i][j]
        elif j == 0:
            maxSums[i][j] = maxSums[i-1][j] + array[i][j]
        elif j == i:
            maxSums[i][j] = maxSums[i-1][j-1] + array[i][j]
        else:
            maxSums[i][j] = max(maxSums[i-1][j], maxSums[i-1][j-1]) + array[i][j]

#for i in range(0,15):
#    print(maxSums[i])

maxSumIndex = 0

for i in range(0,n):
    if maxSums[n-1][maxSumIndex] < maxSums[n-1][i]:
        maxSumIndex = i

print(maxSums[n-1][maxSumIndex])
print(maxPath)

sum = 0
for i in range(100):
    sum += array[i][maxPath[i]]

print(sum)
