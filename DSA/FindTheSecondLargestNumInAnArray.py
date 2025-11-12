# Brute force method 1:
arr = [3,5,67,89,54,12,56,0]
first_lar = arr[0]
second_lar =arr[0]

for num in arr:
    if num > first_lar:
        first_lar = num
for num in arr:
    if num > second_lar and num != first_lar:
        second_lar = num
        
print(first_lar)
print(second_lar)

# Brute force method 2:
arr = [3,5,67,89,54,12,56,0]
first_lar = arr[0]
second_lar =arr[0]
for num in arr:
    first_lar = max(first_lar, num)

for num in arr:
    if num > second_lar and num != first_lar:
        second_lar = num

print(first_lar, second_lar)


# Optimal solution method 3:
arr = [3,5,67,89,54,12,56,0]
first_lar = float('-inf')
second_lar = float('-inf')

for num in arr:
    if num > first_lar:
        second_lar = first_lar
        first_lar = num
    elif num > second_lar and num != first_lar:
        second_lar = num

print(first_lar, second_lar)
