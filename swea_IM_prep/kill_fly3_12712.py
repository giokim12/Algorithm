def kill1(y, x):
    global total1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    k = 0
    # idx = 0
    total1 += arr[y][x]
    while k<M-1:
        idx = 0
        k += 1
        while idx<4:
            ny = y+dy[idx]*k
            nx = x+dx[idx]*k

            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                idx +=1
                continue

            if idx>3:
                idx = 0
                break

            total1 += arr[ny][nx]
            idx += 1


def kill2(y, x):
    global total2
    dy = [-1, 1, -1, 1]
    dx = [-1, -1, 1, 1]
    k = 0
    # idx = 0
    total2 += arr[y][x]
    while k<M-1:
        idx = 0
        k += 1
        while idx<4:
            ny = y+dy[idx]*k
            nx = x+dx[idx]*k

            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                idx +=1
                continue

            if idx>3:
                idx = 0
                break

            total2 += arr[ny][nx]
            idx += 1

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    MAX = -21e8
    for i in range(N):
        for j in range(N):
            total1 = 0
            total2 = 0
            kill1(i, j)
            if total1>MAX:
                MAX = total1
            kill2(i, j)
            if total2>MAX:
                MAX = total2

    print(f'#{tc} {MAX}')