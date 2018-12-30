import csv
import sys

array = [[None for i in range(0,15)] for k in range(0,15)]
maxSums = [[None for i in range(0,15)] for k in range(0,15)]
#path = [null for i in range(0,15)]


# Reads the csv-file
f = open('numbers.txt', 'rt')
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


for i in range(0,15):
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

for i in range(0,15):
    if maxSums[14][maxSumIndex] < maxSums[14][i]:
        maxSumIndex = i

print(maxSums[14][maxSumIndex])
