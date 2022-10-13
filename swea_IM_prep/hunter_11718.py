T = int(input())

for tc in range(1, T+1):

    def hunt(y, x):
        global total_kills

        for i in range(8): #먼저 쏠 방향 정하고
            j = 1
            while True: #일직선으로 끝까지 쏘기
                ny = y+dy[i]*j
                nx = x+dx[i]*j

                if ny<0 or nx<0 or ny>N-1 or nx>N-1 or arr[ny][nx]==3:
                    #범위 벗어나거나 벽 만나면
                    break

                if arr[ny][nx]==0:
                    #빈공간이면은 계속 쏘기
                    j+=1

                if arr[ny][nx]==2:
                    #토끼 만나면 죽이고 계속 쏘기
                    total_kills +=1
                    j += 1





    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_kills = 0
    #상하좌우 및 대각선 8방향
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j]==1: #사냥꾼이면은
                hunt(i, j)

    print(f'#{tc} {total_kills}')
