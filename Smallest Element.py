#Given an array we have to find the smallest element in the array
arr = [11,2,3,4,5]
minimum = arr[0]

for i in range(len(arr)):
  if arr[i] < minimum:
     minimum = arr[i]

print (minimum)