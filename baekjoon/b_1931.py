N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (x[1], x[0]))
# print(arr)
cnt = 1
start_meet = arr[0][0]
end_meet = arr[0][1]
for i in range(1, len(arr)):

    if arr[i][0] >= end_meet:
        cnt += 1
        start_meet = arr[i][0]
        end_meet = arr[i][1]

print(cnt)