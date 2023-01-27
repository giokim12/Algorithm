arr = list(map(int, input().split()))

arr = sorted(arr)
# print(arr)
total = 0
for i in range(len(arr)):
    total += arr[i]*(len(arr)-i)

print(total)
