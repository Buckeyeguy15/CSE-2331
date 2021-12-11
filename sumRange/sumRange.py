# Name: Robert Frenken
# Project: sumRange
# Description: Given a list of integers and a range, create a binary tree and find the sum of the range
import sys


class Node:

    # Constructor
    def __init__(self, data):
        self.data = data
        self.sum_of_children = 0
        self.left = None
        self.right = None

    def insert(self, child):
        # Determine to go left or right, and if to insert or keep going down
        # Will also keep track of the sum_of_children field as node gets inserted in tree
        if child < self.data:
            if self.left is None:
                self.left = Node(child)
                self.sum_of_children += self.left.data
            else:
                self.sum_of_children += child
                self.left.insert(child)
        else:
            if self.right is None:
                self.right = Node(child)
                self.sum_of_children += self.right.data
            else:
                self.sum_of_children += child
                self.right.insert(child)

    def range_sum_BST(self, root, min, max):
        sum = 0
        if root is None:
            return sum
        # Determine whether to go left or right
        if root.data > min:
            sum += root.range_sum_BST(root.left, min, max)
        if root.data < max:
            sum += root.range_sum_BST(root.right, min, max)
        if min <= root.data <= max:
            sum += root.data
        return sum


dataXFile = open(sys.argv[1], 'r')
dataXWithEscape = []
for i in dataXFile:
    dataXWithEscape.append(i)
dataX = []
for i in dataXWithEscape:
    dataX.append(int(i.strip()))

rangeForSumFile = open(sys.argv[2], 'r').readlines()
rangeforSumStrip = []
for i in rangeForSumFile:
    rangeforSumStrip.append((i.strip()))


rangeforSumList = []
for i in rangeforSumStrip:
    rangeforSumList.append(i.split())

rangeforSum = []

for i in rangeforSumList:
    list = []
    list.append(int(i[0]))
    list.append(int(i[1]))
    rangeforSum.append(list)

root = Node(dataX[0])

for i in range(1, len(dataX)):
    root.insert(dataX[i])

for i in rangeforSum:
    sum = root.range_sum_BST(root, i[0], i[1])
    print('Range: ' + str(i) + '. Sum: ' + str(sum))

