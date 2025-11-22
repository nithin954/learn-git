def missingnumber1(arr):
    n = len(arr)
    for i in range(n):
        if i!=arr[i]:
            return i


arr = [0,1,2,3,5,6,7]
print(missingnumber1(arr))

def missingNumber2(arr):
    n = len(arr)
    dt = {}
    for i in range(n):
        dt[i]=0
    for i in range(n):
        dt[arr[i]]=1
    for k,v in dt.items():
        if v==0:
            return k
        
print(missingNumber2(arr))


def missingNumber3(arr):
    length = len(arr)
    actual_sum = sum(arr)
    expected_sum = length * (length + 1) // 2
    missing_number = expected_sum - actual_sum
    return missing_number

print(missingNumber3(arr))

