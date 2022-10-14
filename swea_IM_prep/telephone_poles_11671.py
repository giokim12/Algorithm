def wifi_reach(y, x, distance):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        j = 1
        while j<=distance:
            ny = y+dy[i]*j
            nx = x+dx[i]*j

            if ny<0 or nx<0 or ny>N-1 or nx>N-1 or arr[ny][nx] == 'A' or arr[ny][nx] == 'B' or arr[ny][nx] == 'C':
                break

            arr[ny][nx] = 'L'
            j+= 1


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                wifi_reach(i, j, 1)
            elif arr[i][j] == 'B':
                wifi_reach(i, j, 2)
            elif arr[i][j]=='C':
                wifi_reach(i, j, 3)

    # print(arr)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

