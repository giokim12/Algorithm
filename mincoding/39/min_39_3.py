n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x: x[1])

end_time = arr[0][1]
total = 1
for i in range(n):
    if arr[i][0] >= end_time:
        total += 1
        end_time = arr[i][1]
    elif arr[i][0] < end_time:
        continue

print(total)