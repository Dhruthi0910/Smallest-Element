#find the second largest and the second smallest element from the array
def find_second_smallest_largest(arr):
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return "Array doesn't have enough unique elements"
    unique_arr.sort()
    
    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]
    
    return second_smallest, second_largest


arr1 = [12, 35, 1, 10, 37, 1]
result = find_second_smallest_largest(arr1)
print(result)