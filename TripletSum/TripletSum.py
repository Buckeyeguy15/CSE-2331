# Name: Robert Frenken
# Project: TripletSum
# Description: Given a list of integers and a sumVal, find and return a triplet of unique integers that sums to sumVal
import sys
dataXFile = open(sys.argv[1], 'r')
dataXWithEscape = []
for i in dataXFile:
    dataXWithEscape.append(i)
dataX = []
for i in dataXWithEscape:
    dataX.append(int(i.strip()))

dataXFile.close()
# print("This is dataX: " + str(dataX))
# print(type(dataX[0]))
sumVal = int(sys.argv[2])

hashTable = {}

for i in dataX:
    for j in dataX:
        # determine if they are distinct
        if not (i == j):
            result = i + j
            # add to hash table
            hashTable[i, j] = result

tupleOfSolutions = []

for k in dataX:
    for key in hashTable:
        i = key[0]
        j = key[1]
        if not (k == i or k == j):
            result = k + hashTable[key]
            if result == sumVal:
                tupleOfSolutions.append((i, j, k))
                break
if len(tupleOfSolutions) > 0:
    print(tupleOfSolutions[0])
else:
    print("No triplet adds up to " + str(sumVal))

