def largestNum(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i]>max_num:
            max_num = arr[i]
    return max_num

arr = [6,2,7,9,-3,-45,67,-1,5]
print(largestNum(arr))



#case-2
arr = [1,2,45,-22,-87,4,6,9]
largest = arr[0]
len_arr = len(arr)
for i in range(len_arr):
    largest = max(largest, arr[i])
print(largest)


arr = [1,2,45,-22,-87,4,6,9]
largest = float('-inf')
len_arr = len(arr)
for i in range(len_arr):
    largest = max(largest, arr[i])
print(largest)