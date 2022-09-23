from collections import deque

def bfs(starty, startx):
    q = deque()
    q.append([starty, startx])

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y+ dy[i]
            nx = x+ dx[i]

            if ny<0 or nx<0 or ny>3 or nx>3: continue
            # if ny== endy and nx==endx:
            #     cnt +=1
            #     return cnt
            if arr[ny][nx] == 0 and used[ny][nx] == 0:
                used[ny][nx]=1
                arr[ny][nx]= arr[y][x]+1
                q.append([ny, nx])



arr = [[0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]]

starty, startx = map(int, input().split())
endy, endx = map(int, input().split())
used = [[False]*4 for _ in range(4)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
used[starty][startx]=1

bfs(starty, startx)
print(f'{arr[endy][endx]}회')