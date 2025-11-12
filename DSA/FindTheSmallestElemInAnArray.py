def minElem(arr):
    min_num = arr[0]
    len_arr = len(arr)
    for i in range(len_arr):
        if arr[i]<min_num:
            min_num = arr[i]
    return min_num

arr = [6,2,7,9,-3,-45,67,-1,5]
print(minElem(arr))

minimum = arr[0]
len_arr = len(arr)
for i in range(len_arr):
    minimum = min(minimum, arr[i])
print(minimum)

