def omok(y, x):
    dy = [1, 0, 1, 1]
    dx = [0, 1, -1, 1]
    for i in range(4):
        cnt = 1
        j = 1
        while True:
            ny = y + dy[i]*j
            nx = x + dx[i]*j
            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1 or arr[ny][nx] == '.':
                break

            if arr[ny][nx] == 'o':
                cnt += 1
                j += 1
                if cnt >= 5:
                    return True

    return False


T = int(input())

for testcase in range(1,T+1):
    flg = 0
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if omok(i,j)==True:
                    flg = 1
                    break

        if flg == 1:
            break


    if flg:
        print(f'#{testcase} YES')
    else:
        print(f'#{testcase} NO')
