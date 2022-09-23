from collections import deque

def bfs(y, x):
    global used, area
    area =0
    q = deque()
    q.append([y, x])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>3 or nx>3: continue
            if arr[ny][nx] == 1 and used[ny][nx]==0:
                used[ny][nx] = 1
                area +=1
                q.append([ny, nx])

    return area




arr = [list(map(int, input().split())) for _ in range(4)]
used = [[False]*4 for _ in range(4)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
AREA = 0
MAX = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] == 1:
            AREA = bfs(i, j)
            if AREA>MAX:
                MAX = AREA

print(MAX)
