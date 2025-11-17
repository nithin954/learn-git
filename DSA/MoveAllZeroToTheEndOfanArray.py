# Moving all zero to the end of an arry using two pointers:

arr = [0,1,0,2,3,0,4,5,6,0,7]

i=0
j = len(arr)-1

while i<j:
    if arr[i]!=0:
        i+=1
    else:
        arr[i],arr[j] = arr[j],arr[i]
        j-=1
print(arr)


#two-pointer forward method:

arr = [0,1,0,2,3,0,4,5,6,0,7]

i = 0
for j in range(len(arr)):
    if arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

print(arr)

