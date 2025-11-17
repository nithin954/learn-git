

def swappingArrayByKPlace(arr,k):
    i=0
    j=len(arr)-1


    while i<k:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr
arr = [1,2,3,4,5,6,7]
swappingArrayByKPlace(arr, k=1)
    



# Right rotate of array by 1 place:

a = [1,2,3,4,5,6,7]
n= len(a)
temp = a[n-1]

for i in range(n-2,-1,-1):
    a[i+1] = a[i]
a[0] = temp

print(a)
    

# Right rotate of array by k place:

def rotateArrayByKPlace(arr,k):
    i = 0
    j = k - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


# Right rotate of array by k place by Brute Force:


def rightRotate(arr, k):
    k = k%len(arr)
    for _ in range(k):
        catch = arr.pop()
        arr.insert(0,catch)
    return arr
arr = [1,2,3,4,5,6,7]
print(rightRotate(arr, k=3))


# Right rotate of array by k place by Better Way (Slicing):
def rightRotate(arr, k):
    n = len(arr)
    arr[:] = arr[n-k:] + arr[:n-k]
    print(arr)
    
arr = [1,2,3,4,5,6,7]
print(rightRotate(arr, k=3))



# Right rotate of array by k place Optimised:
def rightRotate(arr,l,r):
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    return arr
    
arr = [1,2,3,4,5,6,7]
k=3
n=len(arr)
arr = (rightRotate(arr, n-k, n-1))
arr = (rightRotate(arr, 0,n-k-1))
print(rightRotate(arr,0, n-1))

# Same as above without return

def rightRotate(arr,l,r):
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    
arr = [1,2,3,4,5,6,7]
k=3
n=len(arr)
(rightRotate(arr, n-k, n-1))
(rightRotate(arr, 0,n-k-1))
(rightRotate(arr,0, n-1))
print(arr)