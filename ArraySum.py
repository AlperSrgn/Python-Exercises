# Given an array of integers, find the sum of its elements.
# For example, if the array arr = [1,2,3], 1 + 2 + 3 = 6 so return 6.

arr = []
size = int(input("Size of array: "))
sum = 0
for i in range(size):
    elements = int(input())
    arr.append(elements)

for j in arr:
    sum+=j

print("Array: {}".format(arr))
print("Sum of elements: {}".format(sum))