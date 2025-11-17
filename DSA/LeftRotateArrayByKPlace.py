


# Left rotate of array by k place by Brute force:
def lefttRotate(arr, k):
    k = k%len(arr)
    for _ in range(k):
        cat = arr.pop(0)
        arr.append(cat)
    return arr
    
arr = [1,2,3,4,5,6,7]
print(lefttRotate(arr, k=3))


# Left rotate of array by k place by Better Way(Slicing):


def lefttRotate(arr, k):
    n = len(arr)
    arr[:] = arr[k-n:] + arr[:k-n]
    return arr
    
arr = [1,2,3,4,5,6,7]
print(lefttRotate(arr, k=3))