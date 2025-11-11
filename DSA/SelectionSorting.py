def selection_sorting(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if arr[j]<arr[index]:
                index = j
        arr[i], arr[index] = arr[index],arr[i]
    return arr
    
a = [1,2,4,7,9,0,3,5,6]

print(selection_sorting(a))
                