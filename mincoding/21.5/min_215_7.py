arr = [[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 0],
       [0, 1, 2, 0, 2, 1, 0],
       [0, 0, 1, 2, 1, 0, 0],
       [0, 0, 2, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       ]

a, b = map(int, input().split())

arr[a][b]= 1

def whitewin(y, x):
    flg = 0
    directy = [-1, 0, 0, 1]
    directx = [0, -1, 1, 0]

    for i in range(4):
        ny = y + directy[i]
        nx = x + directx[i]

        if nx<0 or ny<0 or nx>6 or ny>6: continue

        elif arr[ny][nx]==1:
            flg += 1
            continue

    if flg == 4:
        return 1
    else: return 0

cnt = 0
for s in range(7):
    for t in range(7):
        if arr[s][t] == 2:
            cnt += whitewin(s, t)

print(cnt)