def maxOnes(arr):
    n = len(arr)
    count = 0
    max_count =0
    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            max_count = max(max_count, count)
            count=0
    max_count = max(max_count, count)
    return max_count

arr = [1,1,1,0,0,1,0,1,0,1,1,1,1]
print(maxOnes(arr))