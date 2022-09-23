from collections import deque

def bfs(y1,x1):
    global cnt
    q = deque()
    q.append([y1, x1, 0])

    while q:
        now = q.popleft()
        y= now[0]
        x= now[1]
        level = now[2]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>height-1 or nx>width-1: continue
            if arr[ny][nx]==0:
                arr[ny][nx] = arr[y][x]+1
                q.append([ny,nx, level+1])
    return level


height, width = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(height)]
starty, startx = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


print(bfs(starty, startx))
