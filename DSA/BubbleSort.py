def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2, -1, -1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


a = [3,5,1,6,2,7,4,9,8]
print(bubble_sort(a))