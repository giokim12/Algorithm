arr = [[0]*101 for _ in range(101)]

for k in range(4):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            arr[i][j] += 1

cnt = 0
for s in range(101):
    for t in range(101):
        if arr[s][t] != 0:
            cnt += 1

print(cnt)