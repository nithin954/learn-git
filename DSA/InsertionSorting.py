def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        print(key, arr[j])
        while j>=0 and arr[j]>key:
            arr[j+1] =arr[j]
            j-=1
        arr[j+1]=key
    return arr
    
a = [2,4,5,6,8,1,3,9,7]
print(insertion(a))