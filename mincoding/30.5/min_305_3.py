arr = [1, 5, 4, 2, -5, -7]
n = int(input())

for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        if arr[i]<arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[n-1])