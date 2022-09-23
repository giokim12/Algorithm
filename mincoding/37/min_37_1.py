from collections import deque
def bfs(y1, x1, y2, x2):
    global days
    q = deque()
    q.append([y1, x1, 1])
    q.append([y2, x2, 1])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]
        level = now[2]
        arr[y][x] = level

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if nx<0 or ny<0 or ny>N-1 or nx>N-1: continue
            if arr[ny][nx]==0:
                # arr[ny][nx]= arr[y][x]+1
                q.append([ny, nx, level+1])


N = int(input())
firsty, firstx, secondy, secondx = map(int, input().split())
arr = [[0]*N for _ in range(N)]
days = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

bfs(firsty, firstx, secondy, secondx)
for i in range(N):
    for j in range(N):
        print(arr[i][j], end ='')
    print()