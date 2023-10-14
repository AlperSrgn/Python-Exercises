# Given an array of integers, find the sum of its elements.
# For example, if the array arr = [1,2,3], 1 + 2 + 3 = 6 so return 6.

def ArraySum(arr):
    sum = 0
    for j in arr:
        sum+=j
    print("Array: {}".format(arr))
    print("Sum of elements: {}".format(sum))


array = []
size = int(input("Size of array: "))
for i in range(size):
    elements = int(input())
    array.append(elements)

ArraySum(array)

