def partition(num, low, high):
    pivot = num[low]
    i,j = low, high 
    while i<j:
        while num[i]<=pivot and i<=high-1:
            i+=1
        while num[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            num[i],num[j] = num[j], num[i]
    num[low], num[j] = num[j], num[low]
    return j

def quick_sort(num, low, high):
    if low<high:
        pv_index = partition(num, low, high)
        quick_sort(num,low, pv_index-1)
        quick_sort(num, pv_index+1, high)
    return num
    
    
print(quick_sort([4,3,2,1], 0, 3))