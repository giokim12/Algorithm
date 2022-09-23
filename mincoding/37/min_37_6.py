from collections import deque

def bfs(starty, startx):
    cnt =0
    q = deque()
    q.append([starty, startx])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or nx>5 or ny>3:
                continue

            if arr[ny][nx] !=1 and used[ny][nx]==0:
                if arr[ny][nx] == 2:
                    cnt +=1
                used[ny][nx]=1
                q.append([ny, nx])

    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]
used = [[False]*6 for _ in range(4)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
used[0][0]=1



print(bfs(0, 0))