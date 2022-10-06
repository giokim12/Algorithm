n = int(input())
dy = [0, 0, 0, -1, 1]
dx = [0, -1, 1, 0, 0]
arr = [[0]*501 for _ in range(501)]
starty = 0
startx = 0

def pear(y, x, idx, l):
    global starty, startx
    k = 1
    arr[y][x]=n
    while k<l:
        ny = y+dy[idx]*k
        nx = x+dx[idx]*k

        arr[ny][nx]=n

        k +=1

    starty += dy[idx]*l
    startx += dx[idx]*l


for tc in range(6):
    idx, llength = map(int, input().split())
    pear(starty, startx, idx, llength)


for i in range(501):
    for j in range(501):
        print(arr[i][j], end = ' ')
    print()
