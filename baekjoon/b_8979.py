N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))
find_rank = []
for i in range(N):
    if arr[i][0]==M:
        find_rank = arr[i]

for i in range(N):
    if arr[i][1:] == find_rank[1:]:
        print(i+1)
        break

