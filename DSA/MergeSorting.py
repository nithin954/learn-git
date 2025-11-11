def merge_sorting(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sorting(left_arr)
    right_arr = merge_sorting(right_arr)
    return merge_arr(left_arr,right_arr)

def merge_arr(l,r):
    n,m = len(l),len(r)
    i,j = 0,0
    result =[]
    while i<n and j<m:
        if l[i]<r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    while i<n:
        result.append(l[i])
        i+=1
    
    while j<m:
        result.append(r[j])
        j+=1
    return result
    
a = [9,6,3,1,4,2,7,5,8]
print(merge_sorting(a))
            