from collections import deque
def bfs():
    global used
    q = deque()
    for i in range(cnt):
        q.append(firecracker_place[i])
        # q.append([y1, x1, 0])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]
        level = now[2]

        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>3 or nx>4: continue
            if arr[ny][nx] == 0 and used[ny][nx]==0:
                used[ny][nx]=1
                q.append([ny, nx, level+1])

    return level




arr = [list(map(int, input().split())) for _ in range(4)]
dy = [0, 0, -1, -1, -1, 1, 1, 1]
dx = [-1, 1, -1, 0, 1, -1, 0, 1]
used = [[False]*5 for _ in range(4)]
cnt = 0

firecracker_place=[]
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            cnt +=1
            firecracker_place.append([i, j, 0])

print(bfs())