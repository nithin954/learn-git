#Brute force method 1:
arr = [1,2,3,4,5,5,5,6,3,2,8,9]

my_dict = {}
my_list=[]
for i in arr:
    my_dict[i] = my_dict.get(i,0)+1
    
for k,v in my_dict.items():
    if v==1:
        my_list.append(k)
    
print(my_dict)
print(my_list)

# Shorter Version Using Counter method 2:
from collections import Counter
arr = [1,2,3,4,5,5,5,6,3,2,8,9]

count = Counter(arr)
unique = [k for k,v in count.items() if v==1]
print(count)
print(unique)

