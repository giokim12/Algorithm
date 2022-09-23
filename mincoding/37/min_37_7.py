from collections import deque
# from copy import deepcopy
def bfs(starty, startx, goal):
    q = deque()
    q.append([starty, startx])
    used = [[False]*width for _ in range(height)]
    used[starty][startx]=0

    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or nx>width-1 or ny>height-1: continue

            if arr[ny][nx]==goal and used[ny][nx]==0:
                used[ny][nx]= used[y][x]+1
                return used[ny][nx]
            elif arr[ny][nx] == '.' and used[ny][nx]==0:
                used[ny][nx] = used[y][x]+1
                q.append([ny, nx])


height, width = map(int, input().split())
arr= [list(input().split()) for _ in range(height)]
# arr1 = deepcopy(arr)
# arr12 = deepcopy(arr)
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
cheeze = 0
meetfriend = 0

for i in range(height):
    for j in range(width):
        if arr[i][j]=='S':
            cheeze = bfs(i, j, 'C')
# print(cheeze)
# print(arr)


for i in range(height):
    for j in range(width):
        if arr[i][j]=='C':
            meetfriend = bfs(i, j, 'D')
# print(meetfriend)
print(cheeze+meetfriend)
# print(cheeze)
# print(arr1)
