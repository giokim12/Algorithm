from collections import deque

def bfs(y, x):

    q = deque()
    q.append([y, x])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0>ny or 0>nx or ny>N-1 or nx>M-1: continue
            if arr[ny][nx]==1 and used[ny][nx]==0:
                used[ny][nx]=1
                q.append([ny, nx])




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[False]*M for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and used[i][j]==False:
            cnt +=1
            bfs(i, j)
print(cnt)