import csv
import sys

def word2Value(s):
    v = 0

    for c in s:
        v += ord(c) - ord('A') + 1

    return v

def triangle(n):
    return int((n * (n + 1)) / 2)

#print(word2Value('SKY'), triangle(10))

words = []
# Reads the csv-file
with open('words.txt', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        for w in row:
            words.append(word2Value(w))

t = [triangle(i) for i in range(1, 21)]

counter = 0

for i in words:
    if i in t:
        counter += 1

print(counter)
