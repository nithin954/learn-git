# Brute force method:1
def twoSum(arr, target):
    n = len(arr)
    for i in range(n-1,-1,-1):
        for j in range(n):
            if arr[i]+arr[j]==target:
                return [i,j]
    
arr = [3,6,7,8,9,4]
target = 9

print(twoSum(arr, target))
# Optimised method: 2

def twoSum1(arr, target):
    n = len(arr)
    dt = {}
    for i in range(n):
        rem = target - arr[i]
        if rem in dt:
            return dt[rem], i
        dt[arr[i]]=i
print(twoSum(arr, target))