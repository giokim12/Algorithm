N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

arr = sorted(arr, key=lambda x: int(x[0]))

for i in range(N):
    print(*arr[i])
