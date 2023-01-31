n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

total = 100
cnt = 0
for i in range(n):
    total -=arr[i]
    if total <0:
        break
    else:
        cnt += 1
        continue

print(cnt)