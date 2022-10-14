N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    arr[i][1] = int(arr[i][1])
    arr[i][2] = int(arr[i][2])
    arr[i][3] = int(arr[i][3])

arr = sorted(arr, key=lambda x: (-x[3], -x[2], -x[1]))
print(arr[0][0])
print(arr[-1][0])
